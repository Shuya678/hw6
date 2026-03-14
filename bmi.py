import streamlit as st

st.set_page_config(page_title="BMI Calculator", layout="centered")
st.title("BMI Calculator")

unit = st.radio("Choose units", ["Metric (m, kg)", "Imperial (ft/in, lb)"], horizontal=True)

def bmi_metric(height_m: float, weight_kg: float) -> float:
    return weight_kg / (height_m ** 2)

def bmi_imperial(height_ft: float, height_in: float, weight_lb: float) -> float:
    height_total_in = height_ft * 12 + height_in
    return 703 * weight_lb / (height_total_in ** 2)

def bmi_category(b: float) -> str:
    if b < 18.5:
        return "Underweight"
    if b < 25:
        return "Normal"
    if b < 30:
        return "Overweight"
    return "Obesity"

if unit.startswith("Metric"):
    c1, c2 = st.columns(2)
    with c1:
        height_m = st.number_input("Height (meters)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)
    with c2:
        weight_kg = st.number_input("Weight (kg)", min_value=10.0, max_value=400.0, value=65.0, step=0.5)

    if st.button("Calculate BMI"):
        b = bmi_metric(height_m, weight_kg)
        st.success(f"BMI = {b:.2f}  ({bmi_category(b)})")

else:
    c1, c2, c3 = st.columns(3)
    with c1:
        height_ft = st.number_input("Height (feet)", min_value=1, max_value=8, value=5, step=1)
    with c2:
        height_in = st.number_input("Height (inches)", min_value=0, max_value=11, value=7, step=1)
    with c3:
        weight_lb = st.number_input("Weight (lb)", min_value=20.0, max_value=900.0, value=150.0, step=1.0)

    if st.button("Calculate BMI"):
        if height_ft == 0 and height_in == 0:
            st.error("Height cannot be zero.")
        else:
            b = bmi_imperial(height_ft, height_in, weight_lb)
            st.success(f"BMI = {b:.2f}  ({bmi_category(b)})")