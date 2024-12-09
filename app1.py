import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

import streamlit as st
import pickle
import pandas as pd

# Page Navigation
st.set_page_config(page_title="Vehicle Attribute Insights", layout="wide")

# Custom CSS to style the app
st.markdown("""
    <style>
        /* Background and text colors */
        body {
            background-color: #97f1ee;
            color: #2c9cec;
        }
        
        /* Sidebar style */
        .sidebar .sidebar-content {
            background-color: #68ceef;
        }
        
        .sidebar .sidebar-header {
            color: #ffffff;
        }
        
        .sidebar .sidebar-item {
            color: #ffffff;
        }

        .sidebar .sidebar-item:hover {
            background-color: #2c9cec;
        }
        
        /* Title and headers */
        h1, h2, h3, h4 {
            color: #2c9cec;
        }

        /* Buttons */
        .stButton button {
            background-color: #68ceef;
            color: white;
            border-radius: 10px;
            font-weight: bold;
        }
        
        .stButton button:hover {
            background-color: #2c9cec;
        }

        /* Input fields */
        .stTextInput input, .stNumberInput input, .stSelectbox select, .stRadio input {
            background-color: #ffffff;
            color: #2c9cec;
        }

        .stTextInput input:focus, .stNumberInput input:focus, .stSelectbox select:focus, .stRadio input:focus {
            border-color: #2c9cec;
        }
    </style>
""", unsafe_allow_html=True)

page = st.sidebar.radio("Navigation", [
    "Introduction",
    "Dashboard",
    "Model Development",
    "Fuel Type Prediction",
    "Engine HP Prediction"
])

# 1. Introduction Page
if page == "Introduction":
    st.title("Predictive Modeling and Analysis of Vehicle Attributes")
    st.markdown("""
    ### Insights into Fuel Types, Engine Performance, and Market Trends
    This application showcases the power of predictive modeling in analyzing vehicle attributes. 
    It features:
    - A Tableau Dashboard providing visual insights.
    - A detailed guide on developing predictive models using Orange Data Mining.
    - Predictive tools for determining:
        - Vehicle fuel type based on attributes.
        - Engine horsepower based on vehicle specifications.
    """)

# 2. Dashboard Page
elif page == "Dashboard":
    st.title("Vehicle Attribute Insights Dashboard")
    st.markdown("""
    This dashboard provides a comprehensive analysis of vehicle data, offering insights into pricing, performance, fuel efficiency, and market trends. 
    Designed for automotive enthusiasts, analysts, and decision-makers, it combines key metrics and visualizations to reveal patterns across different makes, models, and years.
    """)
    # Add an image of the Tableau dashboard
    st.image("/Users/noofas/Desktop/Car_App/dash.png", caption="Snapshot of Tableau Dashboard", use_column_width=True)
    
    # Provide a link to the live Tableau dashboard
    tableau_url = 'https://public.tableau.com/app/profile/noof.as/viz/AutoInsightsDashboard/Dashboard2'
    st.markdown(f"[View Interactive Dashboard]({tableau_url})")

# 3. Model Development Page
elif page == "Model Development":
    st.title("Model Development Using Orange Data Mining")
    st.markdown("""
    ### How We Developed the Predictive Model
    - **Data Cleaning**: Preprocessed data to handle missing values and inconsistencies.
    - **Feature Selection**: Selected attributes such as engine size, vehicle type, and market category.
    - **Model Training**: Trained the model using Orange's visual workflow with classification techniques.
    - **Evaluation**: Evaluated performance metrics like accuracy and F1-score.
    """)
    st.image("/Users/noofas/Desktop/Car_App/Picture1.png", caption="Orange Data Mining Workflow")

# 4. Fuel Type Prediction Page
elif page == "Fuel Type Prediction":
    st.title("Vehicle Fuel Type Prediction")
    st.write("Enter the details of a vehicle to predict its fuel type.")

    # Load the pre-trained model from the pickle file
    with open('vehicle_fuel_type_model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Function to make predictions
    def predict_fuel_type(data):
        prediction = model.predict(data)
        return prediction

    # Collect user input with more user-friendly descriptions and placeholders
    st.subheader("Enter Vehicle Details for Prediction")
    st.markdown("Fill in the vehicle details below to get the predicted fuel type.")

    make = st.text_input("Make (e.g., BMW, Toyota)", placeholder="Enter the vehicle manufacturer")
    model_name = st.text_input("Model (e.g., 3 Series, Corolla)", placeholder="Enter the vehicle model")
    year = st.number_input("Year of Manufacture", min_value=1900, max_value=2024, value=2022, step=1)
    engine_hp = st.number_input("Engine Horsepower (HP)", min_value=0, value=180, step=10)
    engine_cylinders = st.number_input("Number of Engine Cylinders", min_value=2, max_value=12, value=4, step=1)
    transmission_type = st.radio("Transmission Type", ["Automatic", "Manual"])
    driven_wheels = st.radio("Driven Wheels", ["Rear Wheel Drive", "All Wheel Drive", "Front Wheel Drive"])
    number_of_doors = st.slider("Number of Doors", min_value=2, max_value=4, value=4, step=2)
    market_category = st.text_input("Market Category (e.g., Luxury, Performance)")
    vehicle_size = st.selectbox("Vehicle Size", ["Compact", "Midsize", "Large"])
    vehicle_style = st.selectbox("Vehicle Style", ["Sedan", "SUV", "Coupe", "Wagon", "Convertible", "Hatchback", "Truck", "Van"])
    highway_mpg = st.number_input("Highway Miles per Gallon (MPG)", min_value=0, value=40, step=1)
    city_mpg = st.number_input("City Miles per Gallon (MPG)", min_value=0, value=30, step=1)
    popularity = st.number_input("Popularity Index", min_value=0, value=3000, step=100)
    msrp = st.number_input("Manufacturer's Suggested Retail Price (MSRP)", min_value=0, value=35000, step=1000)

    # Make prediction when the button is pressed
    if st.button("Predict Fuel Type"):
        # Create a DataFrame from user input
        user_input = pd.DataFrame({
            'Make': [make],
            'Model': [model_name],
            'Year': [year],
            'Engine HP': [engine_hp],
            'Engine Cylinders': [engine_cylinders],
            'Transmission Type': [transmission_type],
            'Driven_Wheels': [driven_wheels],
            'Number of Doors': [number_of_doors],
            'Market Category': [market_category],
            'Vehicle Size': [vehicle_size],
            'Vehicle Style': [vehicle_style],
            'highway MPG': [highway_mpg],
            'city mpg': [city_mpg],
            'Popularity': [popularity],
            'MSRP': [msrp]
        })

        # Make prediction
        fuel_type = predict_fuel_type(user_input)

        # Display the result
        st.write(f"The predicted engine fuel type is: **{fuel_type[0]}**")

# 5. Engine HP Prediction Page
elif page == "Engine HP Prediction":
    st.title("Vehicle Engine Horsepower Prediction")
    st.markdown("Enter vehicle specifications to predict engine horsepower.")

    # Load the engine HP prediction model pipeline
    with open("random_forest_pipeline.pkl", "rb") as file:
        model_pipeline = pickle.load(file)

    # Collect input for engine horsepower prediction
    year = st.number_input("Year of Manufacture", min_value=1900, max_value=2024, value=2022, step=1)
    engine_cylinders = st.number_input("Number of Engine Cylinders", min_value=2, max_value=12, value=4, step=1)
    transmission_type = st.radio("Transmission Type", ["Automatic", "Manual"])
    vehicle_size = st.selectbox("Vehicle Size", ["Compact", "Midsize", "Large"])
    highway_mpg = st.number_input("Highway Miles per Gallon (MPG)", min_value=0, value=40, step=1)
    city_mpg = st.number_input("City Miles per Gallon (MPG)", min_value=0, value=30, step=1)
    msrp = st.number_input("Manufacturer's Suggested Retail Price (MSRP)", min_value=0, value=35000, step=1000)

    # Create input DataFrame for the prediction
    input_data = pd.DataFrame({
        'Year': [year],
        'Engine Cylinders': [engine_cylinders],
        'Transmission Type': [transmission_type],
        'Vehicle Size': [vehicle_size],
        'highway MPG': [highway_mpg],
        'city mpg': [city_mpg],
        'MSRP': [msrp]
    })

    # Ensure correct column order
    input_data = input_data.reindex(columns=model_pipeline.named_steps['preprocessor'].transformers_[1][2], fill_value=0)

    # Make prediction when the button is pressed
    if st.button("Predict Engine HP"):
        try:
            engine_hp = model_pipeline.predict(input_data)
            st.success(f"The predicted engine horsepower is: **{engine_hp[0]} HP**")
        except Exception as e:
            st.error(f"Error during prediction: {e}")
