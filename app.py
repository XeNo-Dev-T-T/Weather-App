import time
import streamlit as st
# Import the custom function from your other file
from weather_service import fetch_weather

# Replace with your real OpenWeather API Key
OPENWEATHER_API_KEY = "Your_Api_Key_Here"

st.title('Weather App')
st.caption('Built as a side project')

take_location = st.text_input('Enter Your City Name : ')

if "loading_started" not in st.session_state:
    st.session_state.loading_started = False
if "weather_data" not in st.session_state:
    st.session_state.weather_data = None

st.subheader("Confirm?")
col1, col2 = st.columns(2)

with col1:
    if st.button("🟢 Yes", type="primary", use_container_width=True):
        if take_location.strip() != '':
            st.session_state.loading_started = True
            st.session_state.weather_data = None # Clear old data
            st.rerun()
        else:
            st.error("Please enter a city name first!")

with col2:
    if st.button("🔴 No", type="secondary", use_container_width=True):
        st.session_state.loading_started = False
        st.session_state.weather_data = None
        st.rerun()  

# Run the animation and API request
if st.session_state.loading_started:    
    st.title("Loading Data...")
    progress_bar = st.progress(0)
    status_text = st.empty()

    for percent_complete in range(50):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
        status_text.text(f"Connecting to server... {percent_complete + 1}%")
        
    # Execute the backend API call midway through the animation
    result = fetch_weather(take_location, OPENWEATHER_API_KEY)
    st.session_state.weather_data = result

    for percent_complete in range(50, 100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
        status_text.text(f"Formatting response... {percent_complete + 1}%")
        
    progress_bar.empty()
    status_text.empty()
    st.session_state.loading_started = False
    st.rerun()

# Render Weather Dashboards below if results exist in Session State
if st.session_state.weather_data:
    weather = st.session_state.weather_data
    
    if weather["success"]:
        st.success(f"🎉 Displaying weather for {weather['city']}, {weather['country']}:")
        
        # Display nicely inside metrics cards
        m1, m2, m3 = st.columns(3)
        m1.metric("Temperature", f"{weather['temp']} °C")
        m2.metric("Feels Like", f"{weather['feels_like']} °C")
        m3.metric("Humidity", f"{weather['humidity']}%")
        
        st.info(f"💨 **Wind Speed:** {weather['wind_speed']} m/s  |  🌤️ **Conditions:** {weather['description']}")
    else:
        st.error(f"❌ Failed to fetch data: {weather['message']}")
