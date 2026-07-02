# 🌤️ Weather App

A minimalistic Streamlit web application that fetches real-time weather details using the OpenWeather API.

## Features
- Clean user input with validation
- Animated progress bar during data fetching
- Live dashboard displaying temperature, humidity, and wind conditions

## File Structure
- `app.py`: Main Streamlit UI and app layout flow.
- `weather_service.py`: Backend integration function for the OpenWeather API.

## Quick Start

### 1. Install Dependencies
```bash
pip install streamlit requests
```

### 2. Configure Your API Key
Open `app.py` and replace the placeholder string with your real API token:
```python
OPENWEATHER_API_KEY = "YOUR_ACTUAL_OPENWEATHER_API_KEY"
```

### 3. Run the App
```bash
streamlit run app.py
```
