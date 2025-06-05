# 🏠 Home Credit Default Risk Prediction

This project aims to predict the likelihood of a client defaulting on a loan using machine learning techniques. The dataset is based on a real-world financial domain challenge, where accurate predictions assist in better credit risk management and lending decisions.

## 📁 Project Structure

| File                                      | Description                                                                 |
|-------------------------------------------|-----------------------------------------------------------------------------|
| `home_credit_data_preprocessing.ipynb`    | Data loading, cleaning, feature engineering, and missing/outlier handling. |
| `home_credit_eda_and_inference.ipynb`     | Exploratory Data Analysis (EDA), feature visualization, and model training.|
| `home_credit_modelling.ipynb`             | Model Evaluation, Model Ensembling, Model Selection and other techniques.  |

---

## 📊 Dataset

This project uses data related to home credit applications, including:
- Client demographic and financial information.
- Historical loan and payment behavior.

> *(Note: Dataset from the Kaggle Home Credit Default Risk competition)*

---

## ⚙️ Methods Used

### ✅ Data Preprocessing
- Handling missing values
- Encoding categorical variables
- Feature selection and transformation

### 📈 EDA
- Distribution analysis of key features
- Correlation heatmaps
- Class imbalance checks

### 🤖 Modeling
- Gradient Boosted Trees / XGBoost / LightGBM (depending on the final selection)
- Evaluation metrics: ROC-AUC, accuracy, precision, recall
- Feature importance interpretation

---
### Deployment
- Deployed the final model to Google Cloud Platform (GCP) with an HTTP interface, making it accessible for real-world use.
https://home-credit-1213.uc.r.appspot.com/predict 


## 🎯 Results

- The model achieved strong performance in identifying high-risk clients.
- Key predictors included:
  - External source scores
  - Credit history length
  - Type of income
- The model achieved a ROC-AUC score of 0.77, correctly distinguishing 77% of default cases from non-defaults for LightGBM model
---

## 🚀 How to Run

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn xgboost lightgbm
