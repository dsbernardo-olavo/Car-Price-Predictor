import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Car Price Estimator", page_icon="🚗")

@st.cache_resource 
def load_data():
    model = joblib.load('car_price_model.pkl')
    df = pd.read_csv("CarPriceDataset.csv", sep=";")
    return model, df

model, df = load_data()

st.title("Car Price Estimator 🚗")
st.write("Provide the data below to get an estimated price for your car")

st.divider()

col1, col2 = st.columns(2)

with col1:

    brands = sorted(df['Brand'].unique())
    brand = st.selectbox("Brand", brands)

    models_filtered = sorted(df[df['Brand'] == brand]['Model'].unique())
    model_car = st.selectbox("Model", models_filtered)

    fuels = sorted(df['Fuel_Type'].unique())
    fuel = st.selectbox("Fuel Type", fuels)

    transmissions = sorted(df['Transmission'].unique())
    trans = st.selectbox("Transmission", transmissions)

with col2:

    year = st.number_input("Year", min_value=2000, max_value=2026, value=2020)

    engine_options = sorted(df['Engine_Size'].unique())
    engine = st.selectbox("Engine Size (L)", engine_options)

    door_options = sorted(df['Doors'].unique())
    doors = st.selectbox("Doors", door_options)

    owner_options = sorted(df['Owner_Count'].unique())
    owners = st.selectbox("Number of Previous Owners", owner_options)

    mileage = st.number_input("Mileage (km)", min_value=0, value=20000, step=1000)

st.divider()

if st.button("Estimate Market Price", use_container_width=True):

    input_data = pd.DataFrame([{
        'Brand': brand,
        'Model': model_car,
        'Year': year,
        'Engine_Size': engine,
        'Fuel_Type': fuel,
        'Transmission': trans,
        'Mileage': mileage,
        'Doors': doors,
        'Owner_Count': owners
    }])
    
    try:
        prediction = model.predict(input_data)
        
        st.balloons()
        st.success(f"### The estimated market price is: **${prediction[0]:,.2f}**")
              
    except Exception as e:
        st.error(f"Error processing the forecast: {e}")

st.markdown("---")
st.markdown("Developed by Bernardo Olavo | [GitHub] https://github.com/dsbernardo-olavo/ | [LinkedIn] https://www.linkedin.com/in/ds-bernardo-olavo/")
