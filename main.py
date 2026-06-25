import json

def get_mock_weather(city):
    print(f"Fetching current weather data for: {city}...")
    # Simulated API response data
    mock_data = {
        "city": city,
        "temperature": "22°C",
        "condition": "Partly Cloudy",
        "humidity": "65%"
    }
    return mock_data

if __name__ == "__main__":
    print("=== Quick Weather CLI ===")
    city_input = "New York"
    weather = get_mock_weather(city_input)
    
    print(f"\nLocation: {weather['city']}")
    print(f"Temp: {weather['temperature']}")
    print(f"Condition: {weather['condition']}")
