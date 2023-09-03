import json
from types import SimpleNamespace
from apiservice import get_chat_completion

promptTemplate = """Act as a personal trainer.
        The following, between ''' are my measuerments, goals, dietrestrictions, allergies, and if I'm diabetic.
        There are also recommendations from my doctor.
        Give me a four week meal plan that's a suitable diet.
        '''
        Gender: {gender}
        Age: {age}
        Height: {height} cm
        Weight: {weight} kg
        Waist: {waist} cm
        Goals: {goals}
        Doctor recommendations: {recommendations}
        Restrictions: {restrictions}
        Allergies: {allergies}
        Diabetic: {diabetic}
        '''
        Step 1: Write an overall analysis and recommendation, maxumum three sentences.
        Step 2: Give recommendations regarding type of diet, if fasting or any other methods are suitable, number of meals per day
        Return your answer in a JSON object containing:
        Analysis: This should be the answer from Step 1.
        Recommendations: This should be the answer from Step 2.
        MealPlan: List of 4 Weeks, each containing Week (as string), a list of days (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday), each containing Day (weekday name) and a list of meals based on the recommendations in Step 2.
        Cost: The Azure cost for this query, in US dollars
        """

def CreateDiet(gender, age, height, weight, waist, goals, recommendations, restrictions, allergies, diabetic):
    prompt = promptTemplate.format(gender=gender, age=age, height=height, weight=weight, waist=waist, goals=goals, recommendations=recommendations, restrictions=restrictions, allergies=allergies, diabetic=diabetic)

    response = get_chat_completion(prompt)
    report = response.choices[0].message.content

    return json.loads(report, object_hook=lambda d: SimpleNamespace(**d))
