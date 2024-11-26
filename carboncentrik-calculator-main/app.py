import streamlit as st

# Define emission factors for cities (corrected data)
EMISSION_FACTORS = {
    "Delhi": {
        "Petrol": 2.5,       # kgCO2/km
        "Diesel": 2.7,       # kgCO2/km
        "CNG": 1.5,          # kgCO2/km
        "Electricity": 1.1,  # kgCO2/kWh
        "Diet": 3.5,         # kgCO2/meal
        "Waste": 2.4,        # kgCO2/kg
        "Baby": 58           # tons CO2/year per child
    },
    "Mumbai": {
        "Petrol": 2.4,
        "Diesel": 2.6,
        "CNG": 1.4,
        "Electricity": 0.9,
        "Diet": 3.0,
        "Waste": 2.0,
        "Baby": 56
    },
    "Bangalore": {
        "Petrol": 2.3,
        "Diesel": 2.5,
        "CNG": 1.4,
        "Electricity": 0.8,
        "Diet": 3.2,
        "Waste": 1.9,
        "Baby": 54
    },
    "Chennai": {
        "Petrol": 2.4,
        "Diesel": 2.6,
        "CNG": 1.5,
        "Electricity": 1.0,
        "Diet": 3.3,
        "Waste": 2.2,
        "Baby": 57
    },
    "Kolkata": {
        "Petrol": 2.6,
        "Diesel": 2.8,
        "CNG": 1.6,
        "Electricity": 1.2,
        "Diet": 3.4,
        "Waste": 2.5,
        "Baby": 59
    },
    "Hyderabad": {
        "Petrol": 2.4,
        "Diesel": 2.6,
        "CNG": 1.5,
        "Electricity": 0.9,
        "Diet": 3.3,
        "Waste": 2.1,
        "Baby": 56
    },
    "Pune": {
        "Petrol": 2.3,
        "Diesel": 2.5,
        "CNG": 1.4,
        "Electricity": 0.8,
        "Diet": 3.1,
        "Waste": 2.0,
        "Baby": 55
    },
    "Ahmedabad": {
        "Petrol": 2.5,
        "Diesel": 2.7,
        "CNG": 1.5,
        "Electricity": 1.0,
        "Diet": 3.4,
        "Waste": 2.2,
        "Baby": 57
    },
    "Lucknow": {
        "Petrol": 2.5,
        "Diesel": 2.7,
        "CNG": 1.5,
        "Electricity": 1.1,
        "Diet": 3.5,
        "Waste": 2.3,
        "Baby": 57
    },
    "Kanpur": {
        "Petrol": 2.5,
        "Diesel": 2.7,
        "CNG": 1.5,
        "Electricity": 1.2,
        "Diet": 3.4,
        "Waste": 2.4,
        "Baby": 58
    },
    "Gurgaon": {
        "Petrol": 2.6,
        "Diesel": 2.8,
        "CNG": 1.6,
        "Electricity": 1.0,
        "Diet": 3.6,
        "Waste": 2.2,
        "Baby": 59
    },
    "Ghaziabad": {
        "Petrol": 2.5,
        "Diesel": 2.7,
        "CNG": 1.5,
        "Electricity": 1.1,
        "Diet": 3.5,
        "Waste": 2.3,
        "Baby": 57
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")

# Streamlit app code
st.title("Carbon Emission Calculator App ⚠️")
st.subheader("By Abhinav and Aryan")

# User inputs
st.subheader("🌍 Your City")
city = st.selectbox(
    "Select your city",
    [
        "Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Hyderabad", 
        "Pune", "Ahmedabad", "Lucknow", "Kanpur", "Gurgaon", "Ghaziabad"
    ]
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 Daily commute in a Petrol Vehicle (in km)")
    distance_petrol = st.slider("Distance (Petrol)", 0.0, 100.0, key="distance_petrol_input")

    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("🚗 Daily commute in a Diesel Vehicle (in km)")
    distance_diesel = st.slider("Distance (Diesel)", 0.0, 100.0, key="distance_diesel_input")

    st.subheader("🍽️ Number of meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")

col3, col4 = st.columns(2)

with col3:
    st.subheader("🚗 Daily commute in a CNG Vehicle (in km)")
    distance_cng = st.slider("Distance (CNG)", 0.0, 100.0, key="distance_cng_input")

with col4:
    st.subheader("🍽️ Waste generated per week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

# New input for the number of babies
st.subheader("👶 Carbon emitted by number of babies born per year(in tons)")
babies = st.number_input("Number of babies", 0, 10, key="babies_input")

# Normalize inputs
distance_petrol = distance_petrol * 365  # Convert daily distance to yearly
distance_diesel = distance_diesel * 365  # Convert daily distance to yearly
distance_cng = distance_cng * 365  # Convert daily distance to yearly
electricity = electricity * 12  # Convert monthly electricity to yearly
meals = meals * 365  # Convert daily meals to yearly
waste = waste * 52  # Convert weekly waste to yearly
baby_emissions = babies * EMISSION_FACTORS[city]["Baby"]  # Calculate baby emissions

# Calculate carbon emissions
petrol_emissions = EMISSION_FACTORS[city]["Petrol"] * distance_petrol
diesel_emissions = EMISSION_FACTORS[city]["Diesel"] * distance_diesel
cng_emissions = EMISSION_FACTORS[city]["CNG"] * distance_cng
electricity_emissions = EMISSION_FACTORS[city]["Electricity"] * electricity
diet_emissions = EMISSION_FACTORS[city]["Diet"] * meals
waste_emissions = EMISSION_FACTORS[city]["Waste"] * waste

# Convert emissions to tonnes and round off to 2 decimal points
petrol_emissions = round(petrol_emissions / 1000, 2)
diesel_emissions = round(diesel_emissions / 1000, 2)
cng_emissions = round(cng_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)
baby_emissions = round(baby_emissions, 2)

# Calculate total emissions
total_emissions = round(
    petrol_emissions + diesel_emissions + cng_emissions + electricity_emissions + diet_emissions + waste_emissions + baby_emissions, 2
)

if st.button("Calculate CO2 Emissions"):
    # Display results
    st.header("Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚗 Petrol: {petrol_emissions} tonnes CO2 per year")
        st.info(f"🚗 Diesel: {diesel_emissions} tonnes CO2 per year")
        st.info(f"🚗 CNG: {cng_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")
        st.info(f"👶 Babies: {baby_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        st.warning(
            "As of 2023, India's CO2 emissions per capita are around **2.0 to 2.2 tons**, up from **0.39 tons in 1972**. "
            "While renewable energy efforts have expanded, the country's reliance on coal continues to drive emissions growth. "
            "India aims for net-zero emissions by 2070, with ongoing efforts to balance development and decarbonization."
        )
        st.subheader("🌱 Tips to Reduce Your Carbon Emissions")
        st.write("""
1. **Use Public Transportation:** Opt for public transport like buses, trains, or metro services to reduce personal car usage and lower transportation emissions.
2. **Adopt Electric Vehicles:** Switch to electric cars or use electric scooters for short distances to cut down on petrol and diesel consumption.
3. **Energy Conservation at Home:** Use energy-efficient appliances, turn off lights when not in use, and consider switching to LED bulbs to reduce electricity consumption.
4. **Reduce, Reuse, Recycle:** Minimize waste generation by reducing plastic use, reusing items, and recycling waste to reduce your carbon footprint from waste management.
5. **Choose a Sustainable Diet:** Reduce meat consumption and opt for plant-based meals, which have a significantly lower carbon footprint than animal-based products.
6. **Sustainable Baby Care:** Choose eco-friendly baby products such as cloth diapers, biodegradable wipes, and organic baby food. Avoid disposable plastic items and consider second-hand baby clothes and toys to minimize environmental impact.
""")


