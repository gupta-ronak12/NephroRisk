import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("ckd_model.pkl", "rb"))

st.set_page_config(page_title="CKD Prediction App", layout="centered")
st.title("Chronic Kidney Disease Prediction App")
st.write("Enter patient details below:")

age = st.number_input("Age", min_value=0, max_value=120, step=1)
bp = st.number_input("Blood Pressure", min_value=0, max_value=250, step=1)
sg = st.number_input("Specific Gravity", format="%.3f")
al = st.number_input("Albumin")
hemo = st.number_input("Hemoglobin", format="%.1f")
sc = st.number_input("Serum Creatinine", format="%.2f")

htn = st.selectbox("Hypertension", ["No", "Yes"])
dm = st.selectbox("Diabetes Mellitus", ["No", "Yes"])
cad = st.selectbox("Coronary Artery Disease", ["No", "Yes"])
appet = st.selectbox("Appetite", ["Poor", "Good"])
pc = st.selectbox("Pus Cell", ["Abnormal", "Normal"])

htn = 1 if htn == "Yes" else 0
dm = 1 if dm == "Yes" else 0
cad = 1 if cad == "Yes" else 0
appet = 1 if appet == "Good" else 0
pc = 1 if pc == "Normal" else 0

if st.button("Predict"):

    input_data = np.array([[age, bp, sg, al, hemo, sc,
                            htn, dm, cad, appet, pc]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    st.write(f"Prediction Probability: {round(probability * 100, 2)}%")

    if prediction[0] == 1:
        st.error("High Risk of Chronic Kidney Disease")
    else:
        st.success("Low Risk of Chronic Kidney Disease")

st.markdown("---")
st.subheader("Model Feature Importance")

importance_df = pd.read_csv("feature_importance.csv")
st.dataframe(importance_df)