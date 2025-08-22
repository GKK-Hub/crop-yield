import streamlit as st
import pandas as pd
import joblib

import os
MODEL_PATH = os.path.join(os.getcwd(), "SVR_best_model.pkl")
# Load trained pipeline
# MODEL_PATH = "SVR_best_model.pkl"
model = joblib.load(MODEL_PATH)

st.title("🌾 Rice Yield Prediction App")
st.write("Enter environmental and agricultural factors to predict rice yield (kg/ha).")

# --- Inputs matching training dataset columns ---
district = st.selectbox(
    "District",
    ["Chennai", "Coimbatore", "Madurai", "Thanjavur", "Tirunelveli",
     "Salem", "Erode", "Trichy", "Vellore", "Kanyakumari"]
)  # replace with full district list

year = st.number_input("Year", min_value=1990, max_value=2100, step=1)

precipitation = st.number_input("Precipitation (mm)", min_value=0.0, step=0.1)
maximum_temperature = st.number_input("Maximum Temperature (°C)", min_value=0.0, step=0.1)
minimum_temperature = st.number_input("Minimum Temperature (°C)", min_value=0.0, step=0.1)
actual_evapotranspiration = st.number_input("Actual Evapotranspiration (mm)", min_value=0.0, step=0.1)
water_deficit = st.number_input("Water Deficit (mm)", min_value=0.0, step=0.1)

total_kharif = st.number_input("Fertilizer Kharif (kg/ha)", min_value=0.0, step=1.0)
total_rabi = st.number_input("Fertilizer Rabi (kg/ha)", min_value=0.0, step=1.0)

rice_production = st.number_input("Rice Production (tons)", min_value=0.0, step=1.0)
rice_area = st.number_input("Rice Area (ha)", min_value=0.0, step=1.0)
rice_irrigated_area = st.number_input("Rice Irrigated Area (ha)", min_value=0.0, step=1.0)

# --- Prediction ---
if st.button("Predict Yield"):
    # ⚠️ Column names must match exactly
    input_data = pd.DataFrame([{
        "dist_name": district,
        "year": year,
        "precipitation": precipitation,
        "maximum_temperature": maximum_temperature,
        "minimum_temperature": minimum_temperature,
        "actual_evapotranspiration": actual_evapotranspiration,
        "water_deficit": water_deficit,
        "total_kharif": total_kharif,
        "total_rabi": total_rabi,
        "rice_production": rice_production,
        "rice_area": rice_area,
        "rice_irrigated_area": rice_irrigated_area
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"🌾 Predicted Rice Yield: **{prediction:.2f} kg/ha**")

# ===========
# New code
# ===========
# SHAP explainability
    # import shap
    # import matplotlib.pyplot as plt
        # --- SHAP Analysis ---
    # try:
    #     # Get the preprocessor and trained SVR inside the pipeline
    #     preprocessor = model.named_steps["preprocessor"]
    #     regressor = model.named_steps["svr"]   # ✅ fix here

    #     # Transform the input so SHAP gets numeric features only
    #     X_transformed = preprocessor.transform(input_data)

    #     # Create SHAP explainer for the SVR model
    #     explainer = shap.Explainer(regressor, X_transformed)

    #     # Compute SHAP values for the input
    #     shap_values = explainer(X_transformed)

    #     # Plot SHAP waterfall for this prediction
    #     st.subheader("🔍 SHAP Explanation")
    #     fig, ax = plt.subplots()
    #     shap.plots.waterfall(shap_values[0], show=False)
    #     st.pyplot(fig)

    # except Exception as e:
    #     st.error(f"SHAP analysis could not be generated: {e}")
        # --- SHAP Analysis ---
        # --- SHAP Analysis without district influence ---
        # --- SHAP Analysis: focus only on numeric features ---
    