import streamlit as st
import pickle
import pandas as pd

with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Glovo Churn Predictor")

avg_delivery_time = st.slider("Avg. delivery time (min)", 15, 90, 35)
custservice_contacts = st.slider("Customer service contacts", 0, 10, 2)
friends_on_glovo = st.slider("Friends on Glovo", 0, 10, 5)
cancelled_orders = st.slider("Cancelled orders", 0, 10, 1)
orders_per_month = st.slider("Orders per month", 1, 10, 8)
num_categories = st.slider("Goods categories ordered", 1, 5, 3)

user = pd.DataFrame([{
    'orders_per_month': orders_per_month,
    'avg_delivery_time': avg_delivery_time,
    'num_categories': num_categories,
    'cancelled_orders': cancelled_orders,
    'custservice_contacts': custservice_contacts,
    'friends_on_glovo': friends_on_glovo
}])

prob = model.predict_proba(user)[0][1]

st.metric("Churn probability", f"{prob:.1%}")

if prob < 0.34:
    st.success("Low risk")
elif prob < 0.67:
    st.warning("Medium risk")
else:
    st.error("High risk")