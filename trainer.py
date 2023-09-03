import json
from types import SimpleNamespace
from apiservice import get_chat_completion

promptTemplate = """Act as a personal trainer.
        The following, between ''' are my measuerments, goals and how many times I want to workout per week, not counting cardio such as walks or runs.
        There are also recommendations from my doctor.
        Give me a workout regiment that's suitable.
        '''
        Gender: {gender}
        Age: {age}
        Height: {height} cm
        Weight: {weight} kg
        Waist: {waist} cm
        Goals: {goals}
        Workouts: {workouts} per week
        Doctor recommendations: {recommendations}
        '''
        Return your answer in a JSON object containing:
        Analysis: An overall analysis and recommendation, maximum three sentences.
        Workouts: This contains a list of Days, each Day object containing a name of Weekday, a list of Exercises containing Exercise, Sets (as string), Reps (as string) where Exercise is the name of the exercise
        Cost: The Azure cost for this query, in US dollars
        """

def CreateTrainingProgram(gender, age, height, weight, waist, goals, workouts, recommendations):
    prompt = promptTemplate.format(gender=gender, age=age, height=height, weight=weight, waist=waist, goals=goals, workouts=workouts, recommendations=recommendations)

    response = get_chat_completion(prompt)
    report = response.choices[0].message.content

    return json.loads(report, object_hook=lambda d: SimpleNamespace(**d))
