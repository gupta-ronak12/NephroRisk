NephroRisk : Explainable Chronic Kidney Disease Prediction System

Problem Statement:
Chronic Kidney Disease (CKD) is a progressive medical condition that often goes undetected in its early stages due to subtle symptoms. Early prediction can significantly improve treatment outcomes and reduce long-term health risks.
The objective of this project is to build a machine learning-based system that predicts the likelihood of Chronic Kidney Disease using patient clinical parameters. The system also provides model explainability to understand which features influence the prediction.

Dataset Description:
The dataset contains 400 patient records with medical attributes such as Age, Blood Pressure, Specific Gravity, Albumin, Hemoglobin, Serum Creatinine, Hypertension, Diabetes Mellitus, Coronary Artery Disease, Appetite, and Pus Cell condition.

The target variable is “classification”, where:
1 represents CKD
0 represents Not CKD

The dataset includes both numerical and categorical features and contains missing values that required preprocessing before training.

Why Random Forest?

Random Forest was selected because it handles mixed numerical and categorical data effectively. It is robust against noise and overfitting, performs well on small to medium-sized datasets, and provides built-in feature importance for explainability. Compared to Logistic Regression, Decision Tree, and KNN, Random Forest achieved the best overall performance on this dataset.

Model Performance:

The final Random Forest model achieved 98.75% test accuracy.

Evaluation was performed using: Accuracy Score, Confusion Matrix and Classification Report

The model correctly classified CKD and Non-CKD cases with high precision and recall.

Project Workflow

Data Preprocessing - Relevant medical features were selected. Missing values were handled using median (for numerical features) and mode (for categorical features). Formatting inconsistencies were cleaned. Categorical variables were encoded into numerical form. Normalization was applied where necessary. The dataset was then split into training (80%) and testing (20%) sets.

Model Training - Multiple classification algorithms were trained and compared. Random Forest was selected as the final model based on superior performance.

Model Evaluation - The model was evaluated using confusion matrix analysis and classification metrics. Performance was verified with realistic test cases.

Model Explainability - Feature importance was extracted from the Random Forest model. The most influential predictors were:

Serum Creatinine
Specific Gravity
Albumin
Hemoglobin

These features align with medical understanding of CKD indicators, increasing model interpretability.

Deployment with Streamlit - The trained model was deployed using Streamlit to create an interactive web application. Users can enter patient details, receive CKD risk prediction, view probability scores, and examine model feature importance.

Streamlit was chosen because it allows fast and lightweight deployment of machine learning models without requiring frontend frameworks. It is ideal for building ML prototypes and interactive applications quickly.

Project Structure : 
NephroRisk folder contains:

app.py (Streamlit application)
CKD_Model_Training.ipynb (Model development notebook)
ckd_model.pkl (Saved trained model)
feature_importance.csv (Model explainability data)
kidney_disease.csv (Dataset)
requirements.txt (Project dependencies)
README.md

How to Run Locally?

Clone the repository.

Navigate to the project folder.

Create a virtual environment using: python -m venv venv

Activate the environment: venv\Scripts\activate (Windows)

Install dependencies: pip install -r requirements.txt

Run the application: streamlit run app.py

Open the browser at http://localhost:8501

Future Improvements:

Perform hyperparameter tuning
Add cross-validation
Deploy the application online
Integrate SHAP for deeper explainability
Expand dataset for better generalization
Add patient risk trend analysis

Learning Outcomes:

This project helped me understand how machine learning works beyond theory. I implemented the complete pipeline from data cleaning and handling missing values to encoding, normalization, model comparison, evaluation, explainability, and deployment.

It strengthened my practical skills in data preprocessing, debugging, model development, and building end-to-end machine learning systems. It also improved my ability to translate classroom concepts into real-world applications.

Why This Project Matters?

As a Data Science student, building complete systems is more valuable than training isolated models in notebooks. This project demonstrates the ability to take a real-world healthcare problem and convert it into a deployable, explainable prediction system.

It reflects practical understanding of the full machine learning lifecycle — from raw data to a working web application.