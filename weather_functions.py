import argparse
import json
import datetime
import sys
# Load weather data from a file
def load_weather_data():
    with open('weather_data.json', 'r') as file:
        return json.load(file)

# Function to display all weather data
def display_all_weather_data(weather_data):
    for city, data in weather_data.items():
        print(f"{city}: {data['condition_percent']}% {data['current_condition']}")

# Function to display the forecast for a city
def display_forecast(city, weather_data):
    if city in weather_data:
        print(f"5-day forecast for {city}:")
        for day in weather_data[city]['forecast']:
            print(f"  Date: {day['date']}, Condition: {day['condition']}, High: {day['high']}°C, Low: {day['low']}°C")
    else:
        print(f"No forecast available for {city}.")

# Function to display detailed weather data for a city
def display_details(city, weather_data):
    if city in weather_data:
        print(f"Weather details for {city}:")
        print(f"  Current condition: {weather_data[city]['current_condition']}")
        print(f"  Condition percent: {weather_data[city]['condition_percent']}%")
        display_forecast(city, weather_data)
    else:
        print(f"No details available for {city}.")

def show_logs():    
    with open('command.log', 'r') as log_file:
        for line in log_file:
            print(line.strip())

def log_command(command):
    with open('command.log', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
        log_file.write(f"{timestamp}: {command}\n")