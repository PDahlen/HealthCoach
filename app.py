from diagnostics import AnalyseMeasurements
from trainer import CreateTrainingProgram
from diet import CreateDiet

import streamlit as st

# streamlit run app.py

st.set_page_config(layout="wide")

st.title("Health Coach in a Box")

# ***** INPUT *****
with st.form('my_form'):
    with st.sidebar:
        # input fields for measurements
        sidecol1, sidecol2 = st.columns(2)
        with sidecol1:
            gender = st.radio(
                "Gender:",
                ('Female', 'Male'))
        with sidecol2:
            age = st.text_input('Age:', '51')

        sidecol3, sidecol4, sidecol5 = st.columns(3)
        with sidecol3:
            weight = st.text_input('Weight (kg)', '98')
        with sidecol4:
            height = st.text_input('Height (cm)', '184')
        with sidecol5:
            waist = st.text_input('Waist (cm)', '87')

        # input fields for blood test
        cholesterol = st.text_input('Cholesterol (mmol)', '4.9')
        bloodpressure = st.text_input('Blood pressure (mm Hg)', '120/81')

        # input fields for diet
        restrictions = st.radio(
            "Any food restrictions?",
            ('None', 'Pescetarian', 'Vegetarian', 'Vegan'))
        diabetic = st.checkbox('Diabetic')
        allergies = st.multiselect(
            'Any allergies',
            ['Milk', 'Eggs', 'Fish', 'Shellfish','Tree nuts', 'Peanuts', 'Wheat', 'Soybeans']
        )

        # input fields for goals
        goals = st.text_input('Goals', 'I want to lose 10 kg in 5 months')
        workouts = st.number_input('Workouts per week', 3)

    # ****** EXECUTION ******
        submitted = st.form_submit_button('Submit')

if submitted:
    # diagnostics
    diagnosticsReport = AnalyseMeasurements(gender, age, height, weight, waist, cholesterol, bloodpressure)

    # training
    trainingRecommendations = ''
    for recommendation in diagnosticsReport.Recommendations:
        if recommendation.Category == 'Exercise' or recommendation.Category == 'Both':
            trainingRecommendations += recommendation.Analysis

    trainingProgram = CreateTrainingProgram(gender, age, height, weight, waist, goals, workouts, trainingRecommendations)

    # diet
    dietRecommendations = ''
    for recommendation in diagnosticsReport.Recommendations:
        if recommendation.Category == 'Diet' or recommendation.Category == 'Both':
            dietRecommendations += recommendation.Analysis
    mealPlan = CreateDiet(gender, age, height, weight, waist, goals, dietRecommendations, restrictions, allergies, diabetic)

    # ***** DISPLAY *****
    col1, col2 = st.columns(2)
    with col1:
        st.header('Health')
        #st.write(diagnosticsReport.Cost)
        st.write(diagnosticsReport.Status)

    with col2:
        st.header('Recommendations')
        for recommendation in diagnosticsReport.Recommendations:
            st.write(recommendation.Analysis)

    st.divider()

    col3, col4 = st.columns(2)
    with col3:
        st.header('Training')
        #st.write(trainingProgram.Cost)
        st.write(trainingProgram.Analysis)
        st.subheader('Program')
        for day in trainingProgram.Workouts:
            st.write("**" + day.Day + "**")
            for exercise in day.Exercises:
                st.write(exercise.Exercise + ': ' + exercise.Sets + ' X ' + exercise.Reps)

    with col4:
        st.header('Diet')
        #st.write(mealPlan.Cost)
        st.write(mealPlan.Analysis)
        for week in mealPlan.MealPlan:
            if week.Week == "Week 1":
                st.subheader(week.Week)
                for day in week.Days:
                    st.write("**" + day.Day + "**")
                    for meal in day.Meals:
                        st.write(meal)
            else:
                with st.expander(week.Week):
                    for day in week.Days:
                        st.write("**" + day.Day + "**")
                        for meal in day.Meals:
                            st.write(meal)

