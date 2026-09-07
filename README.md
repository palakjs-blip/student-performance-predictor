# 🎓 Student Performance Predictor

A machine learning project that predicts a student's final academic performance based on demographic, social, study-related, and previous-period academic information.

## 📌 Project Overview

This project uses the **Student Performance dataset** to predict a student's final grade (`G3`) on a scale of 0–20.

The project covers the complete machine learning workflow:

- Data exploration and analysis
- Data preprocessing
- Categorical feature encoding
- Train-test splitting
- Regression model training
- Model evaluation
- Cross-validation
- Model comparison
- Streamlit deployment

## 🧠 Machine Learning Models

The following regression models were tested:

| Model | R² Score |
|---|---:|
| Linear Regression | 0.724 |
| Decision Tree Regressor | 0.733 |
| SVR | 0.585 |
| Random Forest Regressor | **0.865** |

The **Random Forest Regressor** performed best on the test set.

### Cross-Validation

The final preprocessing and Random Forest model were combined into a pipeline and evaluated using 5-fold cross-validation.

**Mean Cross-Validation R²: ~0.826**

## 📊 Features

The model uses information such as:

- Age and gender
- School and address
- Family information
- Parents' education and jobs
- Study time
- Previous failures
- School and family support
- Internet access
- Social activities
- Absences
- First-period grade (`G1`)
- Second-period grade (`G2`)

The target variable is:

**`G3` — Final Grade**

## 🖥️ Streamlit Application

The trained model is integrated into a Streamlit web application.

The application allows users to enter student information and receive a predicted final grade.

## 🚀 How to Run

Clone this repository and navigate to the project folder.

Install the required Python packages:

```bash
pip install streamlit pandas scikit-learn joblib
streamlit run app.py

📚 Dataset

This project uses the Student Performance dataset from the UCI Machine Learning Repository.

The dataset contains information about students' academic performance and demographic, social, and school-related factors.

⚠️ Disclaimer

This project is intended for educational and demonstration purposes. Predictions should not be treated as definitive measures of a student's future academic performance.

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Joblib
Streamlit
Git & GitHub