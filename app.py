import streamlit as st
import pandas as pd
import joblib

model = joblib.load('car_price_model.pkl')

st.title("Car Price Estimator")
st.write("Provide the vehicle data to get the estimated price")

brand = st.selectbox("Brand", ['Toyota', 'Kia', 'Chevrolet', 'Mercedes', 'Audi', 'Volkswagen', 'Ford', 'BMW', 'Honda', 'Hyundai'])
model_car = st.text_input("Model", "Corolla") 
year = st.number_input("Year", min_value=2000, max_value=2026, value=2015)
engine = st.number_input("Engine Size", 1.0, 5.0, 2.0)
fuel = st.selectbox("Fuel Type", ['Diesel', 'Petrol', 'Hybrid', 'Electric'])
trans = st.selectbox("Transmission", ['Manual', 'Automatic', 'Semi-Automatic'])
mileage = st.number_input("Mileage", value=50000)
doors = st.selectbox("Doors", [2, 4])
owners = st.slider("Owners Number", 1, 5, 1)

# Botão de previsão
if st.button("Estimate Price"):
    input_df = pd.DataFrame([{
        'Brand': brand, 'Model': model_car, 'Year': year,
        'Engine_Size': engine, 'Fuel_Type': fuel, 'Transmission': trans,
        'Mileage': mileage, 'Doors': doors, 'Owner_Count': owners
    }])
    
    prediction = model.predict(input_df)
    st.success(f"The estimated price is: ${prediction[0]:,.2f}")
