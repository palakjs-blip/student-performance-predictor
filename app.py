import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# LOAD TRAINED MODEL
# =========================================================

model = joblib.load("student_model.pkl")
# Prediction history
if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []

st.write("Model expects these columns:")
st.write(model.feature_names_in_)
# =========================================================
# TITLE
# =========================================================

st.title("🎓 Student Performance Predictor")

st.markdown(
    """
    Predict a student's **final examination grade (G3)** out of 20
    using academic, personal, family and lifestyle information.
    """
)

st.info(
    "💡 Enter the student's information below and click "
    "**Predict Final Grade** to get the machine-learning prediction."
)


# =========================================================
# BASIC INFORMATION
# =========================================================

with st.expander("👤 Basic Information", expanded=True):

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "Student Name",
            placeholder="Enter student's name"
        )

        school = st.selectbox(
            "School",
            ["GP", "MS"],
            format_func=lambda x: {
                "GP": "GP - Gabriel Pereira",
                "MS": "MS - Mousinho da Silveira"
            }[x]
        )

        sex = st.selectbox(
            "Sex",
            ["F", "M"],
            format_func=lambda x: {
                "F": "Female",
                "M": "Male"
            }[x]
        )

        age = st.number_input(
            "Age",
            min_value=15,
            max_value=25,
            value=17
        )

    with col2:

        address = st.selectbox(
            "Home Address",
            ["U", "R"],
            format_func=lambda x: {
                "U": "Urban",
                "R": "Rural"
            }[x]
        )

        famsize = st.selectbox(
            "Family Size",
            ["LE3", "GT3"],
            format_func=lambda x: {
                "LE3": "3 or fewer people",
                "GT3": "More than 3 people"
            }[x]
        )

        Pstatus = st.selectbox(
            "Parents' Cohabitation Status",
            ["T", "A"],
            format_func=lambda x: {
                "T": "Living together",
                "A": "Living apart"
            }[x]
        )


# =========================================================
# FAMILY INFORMATION
# =========================================================

with st.expander("👨‍👩‍👧 Family Information"):

    col1, col2 = st.columns(2)

    with col1:

        Medu = st.selectbox(
            "Mother's Education Level",
            [0, 1, 2, 3, 4],
            format_func=lambda x: {
                0: "0 - No formal education",
                1: "1 - Primary education (up to 4th grade)",
                2: "2 - 5th to 9th grade",
                3: "3 - Secondary education",
                4: "4 - Higher education"
            }[x]
        )

        Mjob = st.selectbox(
            "Mother's Occupation",
            ["teacher", "health", "services", "at_home", "other"],
            format_func=lambda x: {
                "teacher": "Teacher",
                "health": "Healthcare",
                "services": "Services sector",
                "at_home": "At home",
                "other": "Other"
            }[x]
        )

        reason = st.selectbox(
            "Main Reason for Choosing This School",
            ["home", "reputation", "course", "other"],
            format_func=lambda x: {
                "home": "Close to home",
                "reputation": "School reputation",
                "course": "Preferred course",
                "other": "Other"
            }[x]
        )

        guardian = st.selectbox(
            "Primary Guardian",
            ["mother", "father", "other"],
            format_func=lambda x: {
                "mother": "Mother",
                "father": "Father",
                "other": "Other"
            }[x],
            help=(
                "Select the person recorded as the student's "
                "primary guardian in the dataset."
            )
        )

    with col2:

        Fedu = st.selectbox(
            "Father's Education Level",
            [0, 1, 2, 3, 4],
            format_func=lambda x: {
                0: "0 - No formal education",
                1: "1 - Primary education (up to 4th grade)",
                2: "2 - 5th to 9th grade",
                3: "3 - Secondary education",
                4: "4 - Higher education"
            }[x]
        )

        Fjob = st.selectbox(
            "Father's Occupation",
            ["teacher", "health", "services", "at_home", "other"],
            format_func=lambda x: {
                "teacher": "Teacher",
                "health": "Healthcare",
                "services": "Services sector",
                "at_home": "At home",
                "other": "Other"
            }[x]
        )

        famrel = st.selectbox(
            "Family Relationship Quality",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "1 - Very bad",
                2: "2 - Bad",
                3: "3 - Average",
                4: "4 - Good",
                5: "5 - Excellent"
            }[x]
        )


# =========================================================
# SCHOOL & STUDY INFORMATION
# =========================================================

with st.expander("📚 School & Study Information"):

    col1, col2 = st.columns(2)

    with col1:

        traveltime = st.selectbox(
            "Travel Time to School",
            [1, 2, 3, 4],
            format_func=lambda x: {
                1: "1 - Less than 15 minutes",
                2: "2 - 15 to 30 minutes",
                3: "3 - 30 minutes to 1 hour",
                4: "4 - More than 1 hour"
            }[x]
        )

        studytime = st.selectbox(
            "Weekly Study Time",
            [1, 2, 3, 4],
            format_func=lambda x: {
                1: "1 - Less than 2 hours",
                2: "2 - 2 to 5 hours",
                3: "3 - 5 to 10 hours",
                4: "4 - More than 10 hours"
            }[x]
        )

        failures = st.number_input(
            "Number of Past Class Failures",
            min_value=0,
            max_value=4,
            value=0
        )

        schoolsup = st.selectbox(
            "Extra Educational Support",
            ["yes", "no"],
            format_func=lambda x: "Yes" if x == "yes" else "No"
        )

        famsup = st.selectbox(
            "Family Educational Support",
            ["yes", "no"],
            format_func=lambda x: "Yes" if x == "yes" else "No"
        )

    with col2:

        paid = st.selectbox(
            "Extra Paid Classes",
            ["yes", "no"],
            format_func=lambda x: "Yes" if x == "yes" else "No"
        )

        activities = st.selectbox(
            "Extracurricular Activities",
            ["yes", "no"],
            format_func=lambda x: "Yes" if x == "yes" else "No"
        )

        nursery = st.selectbox(
            "Attended Nursery School",
            ["yes", "no"],
            format_func=lambda x: "Yes" if x == "yes" else "No"
        )

        higher = st.selectbox(
            "Wants to Pursue Higher Education",
            ["yes", "no"],
            format_func=lambda x: "Yes" if x == "yes" else "No"
        )

        internet = st.selectbox(
            "Internet Access at Home",
            ["yes", "no"],
            format_func=lambda x: "Yes" if x == "yes" else "No"
        )


# =========================================================
# SOCIAL & LIFESTYLE INFORMATION
# =========================================================

with st.expander("🏠 Social & Lifestyle Information"):

    col1, col2 = st.columns(2)

    with col1:

        romantic = st.selectbox(
            "Currently in a Romantic Relationship",
            ["yes", "no"],
            format_func=lambda x: "Yes" if x == "yes" else "No"
        )

        freetime = st.selectbox(
            "Free Time After School",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "1 - Very little free time",
                2: "2 - Little free time",
                3: "3 - Average",
                4: "4 - A lot of free time",
                5: "5 - Very much free time"
            }[x]
        )

        goout = st.selectbox(
            "Going Out With Friends",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "1 - Very rarely",
                2: "2 - Rarely",
                3: "3 - Sometimes",
                4: "4 - Often",
                5: "5 - Very often"
            }[x]
        )

        Dalc = st.selectbox(
            "Workday Alcohol Consumption",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "1 - Very low",
                2: "2 - Low",
                3: "3 - Moderate",
                4: "4 - High",
                5: "5 - Very high"
            }[x]
        )

    with col2:

        Walc = st.selectbox(
            "Weekend Alcohol Consumption",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "1 - Very low",
                2: "2 - Low",
                3: "3 - Moderate",
                4: "4 - High",
                5: "5 - Very high"
            }[x]
        )

        health = st.selectbox(
            "Current Health Status",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "1 - Very bad",
                2: "2 - Bad",
                3: "3 - Average",
                4: "4 - Good",
                5: "5 - Very good"
            }[x]
        )

        absences = st.number_input(
            "Number of School Absences",
            min_value=0,
            max_value=100,
            value=0
        )


# =========================================================
# PREVIOUS EXAM GRADES
# =========================================================

with st.expander("📝 Previous Examination Grades"):

    col1, col2 = st.columns(2)

    with col1:

        G1 = st.number_input(
            "First Period Grade (G1)",
            min_value=0,
            max_value=20,
            value=10,
            help="Grade obtained during the first period, out of 20."
        )

    with col2:

        G2 = st.number_input(
            "Second Period Grade (G2)",
            min_value=0,
            max_value=20,
            value=10,
            help="Grade obtained during the second period, out of 20."
        )


# =========================================================
# PREDICTION
# =========================================================

st.divider()

if st.button(
    "🔮 Predict Final Grade",
    use_container_width=True
):

    # Create DataFrame with exactly the same feature names
    # used during model training.

    input_data = pd.DataFrame({
        "school": [school],
        "sex": [sex],
        "age": [age],
        "address": [address],
        "famsize": [famsize],
        "Pstatus": [Pstatus],
        "Medu": [Medu],
        "Fedu": [Fedu],
        "Mjob": [Mjob],
        "Fjob": [Fjob],
        "reason": [reason],
        "guardian": [guardian],
        "traveltime": [traveltime],
        "studytime": [studytime],
        "failures": [failures],
        "schoolsup": [schoolsup],
        "famsup": [famsup],
        "paid": [paid],
        "activities": [activities],
        "nursery": [nursery],
        "higher": [higher],
        "internet": [internet],
        "romantic": [romantic],
        "famrel": [famrel],
        "freetime": [freetime],
        "goout": [goout],
        "Dalc": [Dalc],
        "Walc": [Walc],
        "health": [health],
        "absences": [absences],
        "G1": [G1],
        "G2": [G2]
    })

    # Make prediction
    st.write("Input given to model:")
    st.write(input_data)
    prediction = model.predict(input_data)

    predicted_grade = prediction[0]

    st.success(
    f"🎉 Predicted Final Grade (G3): "
    f"{predicted_grade:.2f} / 20"
    )

    # Save prediction to history
    st.session_state.prediction_history.append({
    "Student": name if name else "Unnamed",
    "G1": G1,
    "G2": G2,
    "Predicted G3": round(predicted_grade, 2)
    })

# =========================================================
# PREDICTION HISTORY
# =========================================================

st.divider()

st.header("📋 Prediction History")

if st.session_state.prediction_history:

    history_df = pd.DataFrame(
        st.session_state.prediction_history
    )

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True
    )

    if st.button("🗑️ Clear Prediction History"):
        st.session_state.prediction_history = []
        st.rerun()

else:

    st.write("No predictions made yet.")

# =========================================================
# PREDICTION VISUALIZATION
# =========================================================

st.divider()

st.header("📈 Prediction Visualization")

if len(st.session_state.prediction_history) >= 2:

    history_df = pd.DataFrame(
        st.session_state.prediction_history
    )

    chart_data = history_df[
        ["G1", "G2", "Predicted G3"]
    ].copy()

    chart_data.index = [
        f"Prediction {i + 1}"
        for i in range(len(chart_data))
    ]

    st.line_chart(chart_data)

    st.caption(
        "This chart shows how the predicted final grade changes "
        "with the previous examination grades across your predictions."
    )

else:

    st.info(
        "Make at least 2 predictions to see the visualization."
    )

# =========================================================
# ABOUT THE MODEL
# =========================================================

st.divider()

st.header("🧠 About the Model")

st.write(
    """
    This application uses a **Random Forest Regression** model trained
    on the UCI Student Performance dataset.

    The model uses academic, personal, family, school and lifestyle
    information to predict the student's final grade (**G3**).
    """
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Model", "Random Forest")

with col2:
    st.metric("Target", "G3")

with col3:
    st.metric("Input Features", "32")

with col4:
    st.metric("Grade Scale", "0–20")

st.info(
    "The categorical features are converted using One-Hot Encoding "
    "inside the preprocessing pipeline before being passed to the "
    "Random Forest model."
)


# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.header("📊 Model Performance")

performance_data = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Decision Tree",
        "Random Forest",
        "SVR"
    ],
    "MAE": [
        1.64666,
        1.27848,
        1.19189,
        2.029939
    ],
    "MSE": [
        5.65664,
        5.48101,
        3.985288,
        8.50626
    ],
    "R²": [
        0.7241,
        0.732699,
        0.80564,
        0.58516
    ]
})

st.dataframe(
    performance_data,
    use_container_width=True,
    hide_index=True
)

st.success(
    "🏆 Random Forest was selected because it achieved the highest "
    "R² score and the lowest MSE among the tested models."
)


# =========================================================
# CROSS-VALIDATION
# =========================================================

st.subheader("Cross-Validation")

st.metric(
    "Mean Cross-Validation R²",
    "0.826"
)

st.write(
    """
    Cross-validation gave a mean R² score of approximately **0.826**,
    indicating that the model was able to explain a substantial portion
    of the variation in final grades across different validation splits.
    """
)


# =========================================================
# DISCLAIMER
# =========================================================

st.divider()

st.caption(
    "⚠️ This prediction is an estimate generated by a machine-learning "
    "model. It should not be treated as an actual assessment of a "
    "student's ability or future performance."
)