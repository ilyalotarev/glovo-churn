# Glovo Churn Predictor

A Streamlit app that predicts the likelihood of a Glovo customer churning based on their usage behavior.

## Features

Adjust sliders for the following inputs and get an instant churn probability:

- Average delivery time
- Number of customer service contacts
- Friends on Glovo
- Cancelled orders
- Orders per month
- Food categories ordered
- Average order value

The app outputs a churn probability score and classifies the user as **Low**, **Medium**, or **High** risk.

## Run locally

```bash
pip install -r requirements.txt
streamlit run churn_app.py
```

## Model

The underlying model (`churn_model.pkl`) is a pre-trained scikit-learn classifier.
