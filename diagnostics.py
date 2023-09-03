import json
from types import SimpleNamespace
from apiservice import get_chat_completion, get_completion

promptTemplate = """Act as a doctor.
        The following, between ''' are my measuerments and test results. Give me an analysis of my health, and recommended actions.
        '''
        Gender: {gender}
        Age: {age}
        Height: {height} cm
        Weight: {weight} kg
        Waist: {waist} cm
        Cholesterol: {cholesterol} mmol
        Blood Pressure: {bloodpressure} mm Hg
        '''
        Return your answer in a JSON object containing:
        Status: An overall health status, maximum three sentences.
        Analysis: List of the analyses, each containing Area, Analysis
        Recommendations: List of the recommendations, each containing TargetArea, Analysis, Category (Diet, Exercise, Both)
        Cost: The Azure cost for this query, in US dollars
        """

def AnalyseMeasurements(gender, age, height, weight, waist, cholesterol, bloodpressure):
    prompt = promptTemplate.format(gender=gender, age=age, height=height, weight=weight, waist=waist, cholesterol=cholesterol, bloodpressure=bloodpressure)

    response = get_chat_completion(prompt)
    report = response.choices[0].message.content

    return json.loads(report, object_hook=lambda d: SimpleNamespace(**d))
