import streamlit as st
import pandas as pd

# Import the functions and data from recommendation.py
from recommendation import products_df, customers_df, generate_gpt_recommendation, get_collaborative_recommendations

st.title("Product Recommendation System ")

# Create a dictionary to map company names to their IDs
company_name_to_id = dict(zip(customers_df['CompanyName'], customers_df['CustomerID']))

# Display a dropdown list with company names
company_name = st.selectbox("Select Company", list(company_name_to_id.keys()))

# Get the corresponding customer ID
customer_id = company_name_to_id[company_name]

# Retrieve selected customer data
selected_customer = customers_df[customers_df['CustomerID'] == customer_id].iloc[0]

st.write(f"**Customer Profile:**")
st.write(f"Company Name: {selected_customer['CompanyName']}")
st.write(f"Industry: {selected_customer['Industry']}")
st.write(f"Location: {selected_customer['Location']}")
st.write(f"Budget: ${selected_customer['Budget']}")

# Display GPT-based recommendations
#st.subheader("GPT-Based Recommendations")
#gpt_recommendations = generate_gpt_recommendation(selected_customer.to_dict())
#st.write(gpt_recommendations)

# Display Machine Learning-based recommendations
st.subheader("Product Recommendations based on Customer Purchase History:")
ml_recommendations = get_collaborative_recommendations(customer_id)

st.write("**Product Recommendations based on Customer Purchase History : **")
for product_id in ml_recommendations:
    product = products_df[products_df['ProductID'] == product_id].iloc[0]
    st.write(f"- **{product['ProductName']}**: {product['Description']} (Price: ${product['Price']})")
