# Weather Forecast CLI

This is a command-line interface (CLI) application for displaying weather forecasts.

## Setup

1. Ensure Python 3.8 or higher is installed on your system.
2. Place `weather_functions.py` and `weather_main.py` in the same directory.
3. Create a `weather_data.json` file with the weather data in the following format:

```json
{
  "CityName": {
    "current_condition": "Sunny",
    "condition_percent": "10",
    "forecast": [
      {"date": "2023-11-07", "condition": "Partly Cloudy", "high": 20, "low": 10},
      // ... more forecast data
    ]
  },
  // ... other cities
}
```

## Usage

Run the `weather_main.py` script using Python with the desired arguments:

```bash
python weather_main.py --all
python weather_main.py --city "CityName"
python weather_main.py --city "CityName" --forecast
python weather_main.py --city "CityName" --details
python weather_main.py --show-logs
```

### Arguments

- `--all`: Display all weather data.
- `--city`: Specify the city name for which to display weather information.
- `--forecast`: Display the 5-day forecast for the specified city (must be used with `--city`).
- `--details`: Display all available weather details for the specified city (must be used with `--city`).
- `--show-logs`: Show command logs for a specified time period.

## Logs

Logs of the executed commands are stored in `command.log`, with each entry timestamped.

---

Enjoy your personalized weather forecast CLI!
