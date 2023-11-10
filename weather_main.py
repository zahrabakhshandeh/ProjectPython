from weather_functions import *
def setup_arg_parser():
    parser = argparse.ArgumentParser(
        description="Weather Forecast CLI", 
        allow_abbrev=False  # This disables abbreviation matching
    )
    parser.add_argument('--all', action='store_true', help='Display all weather data')
    parser.add_argument('--city', type=str, help='Specify the city name for which to display weather information')
    parser.add_argument('--forecast', action='store_true', help='Display the 5-day forecast for the specified city')
    parser.add_argument('--details', action='store_true', help='Display all available weather details for the specified city')
    parser.add_argument('--show-logs', action='store_true', help='Show command logs for a specified time period')
    return parser


def main():
    # Load weather data
    weather_data = load_weather_data()
    
    # Set up command-line argument parser
    parser = setup_arg_parser()
    args = parser.parse_args()

    # Handle command logs
    if not args.show_logs:
        command_line = " ".join(sys.argv)
        log_command(command_line)
  

    if args.show_logs:
        show_logs()

    elif args.all:
        display_all_weather_data(weather_data)
    elif args.city:
        city = args.city
        if city not in weather_data:
            print(f"{city}.")
        elif args.forecast:
            display_forecast(city, weather_data)
        elif args.details:
            display_details(city, weather_data)
        else:
            print(f"{city}: {weather_data[city]['current_condition']}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
