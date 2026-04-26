"""
Airport Flight Data Analysis

A refined version of the original lesson code. This module validates airport/year
input, loads flight data from CSV files, and calculates summary statistics for
departing flights.

Expected CSV column order:
0 departure_airport
1 flight_number
2 scheduled_departure
3 actual_departure
4 destination
5 distance_miles
6 scheduled_arrival
7 actual_arrival
8 runway
9 weather
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path
from typing import Iterable, Optional



VALID_AIRPORTS: set[str] = {
    "LHR", "MAD", "CDG", "IST", "AMS", "LIS", "FRA", "FCO", "MUC", "BCN"
}

AIRPORT_NAMES: dict[str, str] = {
    "LHR": "London Heathrow",
    "MAD": "Madrid Adolfo Suárez-Barajas",
    "CDG": "Charles De Gaulle International",
    "IST": "Istanbul Airport International",
    "AMS": "Amsterdam Schiphol",
    "LIS": "Lisbon Portela",
    "FRA": "Frankfurt Main",
    "FCO": "Rome Fiumicino",
    "MUC": "Munich International",
    "BCN": "Barcelona International",
}


HOURS_IN_DATASET = 12
MIN_YEAR = 2000
MAX_YEAR = 2025

# 1. BASIC FUNCTION DEFINITION
def greet_user(name):
    """
    This is a docstring - it explains what the function does.
    This function greets a user with their name.
    """
    print(f"Hello, {name}! Welcome to the airport analysis system.")

# Call the function
greet_user("Student")

# 2. FUNCTIONS THAT RETURN VALUES
def get_airline_code(flight_number):
    """
    Extracts the airline code from a flight number.
    Returns the first two characters.
    """
    return flight_number[:2]

# Use the function
flight = "BA123"
airline = get_airline_code(flight)
print(f"Flight {flight} is operated by airline: {airline}")

# 3. VALIDATION FUNCTIONS (Perfect for your Task A!)
def validate_airport_code(code):
    """
    Validates airport code input.
    Returns True if valid, False otherwise.
    """
    valid_airports = ["LHR", "MAD", "CDG", "IST", "AMS", "LIS", "FRA", "FCO", "MUC", "BCN"]
    code = code.strip().upper()
    
    if len(code) != 3:
        print("Wrong code length - please enter a three-letter city code")
        return False
    elif code not in valid_airports:
        print("Unavailable city code - please enter a valid city code")  
        return False
    else:
        return True

def validate_year(year_input):
    """
    Validates year input.
    Returns the year as integer if valid, None if invalid.
    """
    try:
        year = int(year_input)
        if year < 2000 or year > 2025:
            print("Out of range - please enter a value from 2000 to 2025")
            return None
        else:
            return year
    except ValueError:
        print("Wrong data type - please enter a four-digit year value")
        return None

def get_user_input():
    """
    Gets and validates airport code and year from user.
    Returns tuple of (airport_code, year) when both are valid.
    """
    # Get valid airport code
    while True:
        airport_code = input("Please enter the three-letter code for the departure city required: ")
        if validate_airport_code(airport_code):
            airport_code = airport_code.strip().upper()
            break
    
    # Get valid year
    while True:
        year_input = input("Please enter the year required in the format YYYY: ")
        year = validate_year(year_input)
        if year is not None:
            break
    
    return airport_code, year

# 4. DATA ANALYSIS FUNCTIONS (For your Task B!)
def count_total_flights(data_list):
    """
    Counts the total number of flights in the dataset.
    """
    return len(data_list)

def count_runway_flights(data_list, runway_number):
    """
    Counts flights from a specific runway.
    """
    count = 0
    for flight in data_list:
        if flight[8] == str(runway_number):  # Runway is at index 8
            count += 1
    return count

def count_long_haul_flights(data_list, min_distance=500):
    """
    Counts flights over a specified distance.
    """
    count = 0
    for flight in data_list:
        distance = int(flight[5])  # Distance is at index 5
        if distance > min_distance:
            count += 1
    return count

def count_airline_flights(data_list, airline_code):
    """
    Counts flights for a specific airline.
    """
    count = 0
    for flight in data_list:
        flight_airline = flight[1][:2]  # First 2 chars of flight number
        if flight_airline == airline_code:
            count += 1
    return count

def count_weather_flights(data_list, weather_condition):
    """
    Counts flights in specific weather conditions.
    """
    count = 0
    for flight in data_list:
        weather = flight[9]  # Weather is at index 9
        if weather_condition.lower() in weather.lower():
            count += 1
    return count

def calculate_average_per_hour(data_list):
    """
    Calculates average flights per hour over 12 hours.
    """
    total_flights = len(data_list)
    average = total_flights / 12
    return round(average, 2)

def calculate_airline_percentage(data_list, airline_code):
    """
    Calculates percentage of flights for a specific airline.
    """
    airline_flights = count_airline_flights(data_list, airline_code)
    total_flights = len(data_list)
    percentage = (airline_flights / total_flights) * 100
    return round(percentage, 2)

def calculate_delay_percentage(data_list):
    """
    Calculates percentage of delayed flights.
    """
    delayed_count = 0
    for flight in data_list:
        scheduled = flight[2]  # Scheduled departure
        actual = flight[3]     # Actual departure
        if scheduled != actual:
            delayed_count += 1
    
    total_flights = len(data_list)
    percentage = (delayed_count / total_flights) * 100
    return round(percentage, 2)

def find_most_common_destinations(data_list):
    """
    Finds the most common destination(s).
    Returns list of destination codes.
    """
    # Count destinations
    dest_count = {}
    for flight in data_list:
        destination = flight[4]  # Destination is at index 4
        dest_count[destination] = dest_count.get(destination, 0) + 1
    
    # Find maximum count
    max_count = max(dest_count.values())
    
    # Get all destinations with max count
    most_common = []
    for dest, count in dest_count.items():
        if count == max_count:
            most_common.append(dest)
    
    return most_common

# 5. FULL AIRPORT NAME FUNCTION
def get_airport_full_name(airport_code):
    """
    Returns the full name of an airport given its code.
    """
    airport_names = {
        "LHR": "London Heathrow",
        "MAD": "Madrid Adolfo Suárez-Barajas", 
        "CDG": "Charles De Gaulle International",
        "IST": "Istanbul Airport International",
        "AMS": "Amsterdam Schiphol",
        "LIS": "Lisbon Portela",
        "FRA": "Frankfurt Main",
        "FCO": "Rome Fiumicino", 
        "MUC": "Munich International",
        "BCN": "Barcelona International"
    }
    return airport_names.get(airport_code, "Unknown Airport")

# 6. MAIN ANALYSIS FUNCTION (Bringing it all together!)
def analyze_flight_data(data_list, airport_code, year):
    """
    Performs complete analysis of flight data and displays results.
    """
    airport_name = get_airport_full_name(airport_code)
    
    print("*" * 70)
    print(f"File {airport_code}{year}.csv selected - Planes departing {airport_name} {year}")
    print("*" * 70)
    
    # Calculate all statistics
    total_flights = count_total_flights(data_list)
    runway1_flights = count_runway_flights(data_list, 1)
    long_haul = count_long_haul_flights(data_list)
    ba_flights = count_airline_flights(data_list, "BA")
    rain_flights = count_weather_flights(data_list, "rain")
    avg_per_hour = calculate_average_per_hour(data_list)
    af_percentage = calculate_airline_percentage(data_list, "AF")
    delay_percentage = calculate_delay_percentage(data_list)
    
    # Display results
    print(f"The total number of flights from this airport was {total_flights}")
    print(f"The total number of flights departing Runway one was {runway1_flights}")
    print(f"The total number of departures of flights over 500 miles was {long_haul}")
    print(f"There were {ba_flights} British Airways flights from this airport")
    print(f"There were {rain_flights} flights from this airport departing in rain")
    print(f"There was an average of {avg_per_hour} flights per hour from this airport")
    print(f"Air France planes made up {af_percentage}% of all departures")
    print(f"{delay_percentage}% of all departures were delayed")
    
    most_common = find_most_common_destinations(data_list)
    print(f"The most common destination(s): {most_common}")

# 7. EXAMPLE USAGE
print("\n=== Testing Our Functions ===")

# Sample data for testing
sample_data = [
    ["CDG", "BA123", "00:32", "00:32", "LHR", "713", "02:42", "02:42", "1", "18°C clear"],
    ["CDG", "AF456", "01:00", "01:05", "MAD", "650", "03:30", "03:35", "2", "20°C rain"],
    ["CDG", "BA789", "02:15", "02:15", "AMS", "245", "04:00", "04:00", "1", "15°C rain"],
    ["CDG", "FR321", "03:30", "03:30", "LHR", "344", "05:15", "05:15", "2", "18°C clear"]
]

# Test individual functions
print("Testing individual functions:")
print(f"Total flights: {count_total_flights(sample_data)}")
print(f"Runway 1 flights: {count_runway_flights(sample_data, 1)}")
print(f"Long haul flights: {count_long_haul_flights(sample_data)}")
print(f"BA flights: {count_airline_flights(sample_data, 'BA')}")
print(f"Rain flights: {count_weather_flights(sample_data, 'rain')}")
print(f"Average per hour: {calculate_average_per_hour(sample_data)}")
print(f"AF percentage: {calculate_airline_percentage(sample_data, 'AF')}%")
print(f"Delay percentage: {calculate_delay_percentage(sample_data)}%")

# Test full analysis
print("\n=== Full Analysis Test ===")
analyze_flight_data(sample_data, "CDG", 2024)
