# Step 1: Import Modules
import requests
import json

# Function to get Weather data
def get_weather(city):
    API_KEY = "0af251d9cd7937c07fa0bc56d4d9bff0"  # Use your OpenWeatherMap API key
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"  # Corrected URL
    
    # Step 3: Construct the full API URL
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)  # Make API request
        data = response.json()  # Convert response to JSON
        
        # Check if the response was successful
        if data["cod"] == 200:  # Corrected key check
            # Extract required details
            city_name = data["name"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_desc = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]
            
            # Display the result
            print(f"\nWeather in {city_name}:")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather Condition: {weather_desc}")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("City not found. Please enter a valid city name.")
    
    except Exception as e:
        print("Error:", str(e))

# Get user input for city name
city = input("Enter city name: ")  # Removed incorrect indentation
get_weather(city)  # Correct function call
