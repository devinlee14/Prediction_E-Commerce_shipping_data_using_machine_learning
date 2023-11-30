"""
Milestone 2
Nama: Devin Yaung Lee
Batch: HCK-009
// eda.py //
program ini menjadi base model EDA interface.
"""
import streamlit as st
import pandas as pd
import pickle

import streamlit as st
import pandas as pd
import pickle

def run():
    st.title("Predict the Shipping On Time")
    with open('model.pkl', 'rb') as file:
        full_process = pickle.load(file)

    # Collecting user input
    warehouse_block = st.selectbox('Warehouse Block', ['A', 'B', 'C', 'D', 'E'])
    mode_of_shipment = st.selectbox('Mode of Shipment', ['Flight', 'Ship', 'Road'])
    customer_care_calls = st.selectbox('Customer Care Calls', [1, 2, 3, 4, 5, 6, 7])
    customer_rating = st.selectbox('Customer Rating', [1, 2, 3, 4, 5])
    cost_of_the_product = st.number_input('Cost of the Product (in USD)', min_value=0)
    prior_purchases = st.selectbox('Prior Purchases', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    product_importance = st.selectbox('Product Importance', ['low', 'medium', 'high'])
    gender = st.selectbox('Gender', ['F', 'M'])
    discount_offered = st.number_input('Discount Offered (in %)', min_value=0)
    weight_in_gms = st.number_input('Weight (in grams)', min_value=0)

    # Creating a DataFrame with the user input
    data_inf = pd.DataFrame({
        'warehouse_block': [warehouse_block],
        'mode_of_shipment': [mode_of_shipment],
        'customer_care_calls': [customer_care_calls],
        'customer_rating': [customer_rating],
        'cost_of_the_product': [cost_of_the_product],
        'prior_purchases': [prior_purchases],
        'product_importance': [product_importance],
        'gender': [gender],
        'discount_offered': [discount_offered],
        'weight_in_gms': [weight_in_gms]
    })

    st.write('Review your input:')
    st.table(data_inf)

    if st.button('Predict'):
        # Make prediction
        prediction = full_process.predict(data_inf)
        if prediction == 0:
            st.success("The model predicts the shipment will not be on time!")
        else:
            st.success("The model predicts the shipment will be on time!")
    