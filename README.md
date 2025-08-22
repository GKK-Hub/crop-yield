# 🌾 Rice Yield Prediction App

A machine learning project that predicts **rice yield (kg/ha)** for districts in Tamil Nadu using environmental and agricultural factors. Built with Python and deployed as an interactive **Streamlit app**.

---

## 🗂️ Dataset

- Source: **ICRISAT** (International Crops Research Institute for the Semi-Arid Tropics)  
- Crop: **Rice**  
- Region: **Tamil Nadu, India**  
- Features include:
  - Average precipitation (mm)
  - Maximum & minimum temperatures (°C)
  - Actual and potential evapotranspiration (mm)
  - Water deficit (mm)
  - Fertilizer usage (Kharif & Rabi)
  - Rice area and production
  - Irrigated area
  - Year & district

> The dataset spans multiple years and districts, enabling robust time-series predictions.

---

## ⚙️ Project Structure

crop_yield/
├─ src/ # Python scripts for preprocessing, modeling, and Streamlit app
├─ eda/ # Exploratory Data Analysis notebooks and plots
├─ crop_yield-env/ # Python virtual environment (ignored in Git)
├─ requirements.txt # Python dependencies
├─ README.md # Project overview
└─ SVR_best_model.pkl # Trained Support Vector Regression model



---

## 🛠️ Tech Stack

- Python 3.10+
- NumPy, Pandas
- Scikit-learn (SVR, pipelines)
- Streamlit (for interactive UI)
- Joblib (for saving/loading models)
- Matplotlib/Seaborn (optional for EDA)
- Optional: SHAP for model interpretation

---

## 🚀 Features

- Predict **rice yield** by entering environmental and agricultural inputs.
- Interactive **Streamlit UI** for easy experimentation.
- Supports multiple districts in Tamil Nadu.
- Easily extendable to include additional features like rainfall forecasts or fertilizer recommendations.

---

## 📦 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/<your-username>/crop_yield.git
cd crop_yield
