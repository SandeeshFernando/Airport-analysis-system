# Airport-analysis-system
Airport Flight Analyzer is a Python lesson/coursework ,code organization analyzes flight departure data from a CSV dataset validating user inputs (airport code, year), then computing stats like total flights, runway usage, long-haul count, airline percentages, delay rates, weather conditions and common destinations across 10 major European airports

## Features

- Validates airport codes against the supported airport list.
- Validates years from 2000 to 2025.
- Loads flight data from a CSV file.
- Counts total flights and runway 1 departures.
- Counts long-haul flights over 500 miles.
- Counts British Airways and Air France flights.
- Calculates average flights per hour.
- Calculates delayed departure percentage.
- Finds the most common destination or destinations.
- Handles missing files and empty datasets more safely than the original version.

## Supported Airports

| Code | Airport |
|---|---|
| LHR | London Heathrow |
| MAD | Madrid Adolfo Suárez-Barajas |
| CDG | Charles De Gaulle International |


## Expected CSV Format

The program expects each row in the CSV file to follow this column order:

| Index | Column |
|---:|---|
| 0 | Departure airport |
| 1 | Flight number |
| 2 | Scheduled departure time |
| 3 | Actual departure time |
| 4 | Destination |
| 5 | Distance in miles |
| 6 | Scheduled arrival time |
| 7 | Actual arrival time |
| 8 | Runway number |
| 9 | Weather condition |

Example row:

```csv
CDG,BA123,00:32,00:32,LHR,713,02:42,02:42,1,18°C clear
```
| IST | Istanbul Airport International |
| AMS | Amsterdam Schiphol |
| LIS | Lisbon Portela |
| FRA | Frankfurt Main |
| FCO | Rome Fiumicino |
| MUC | Munich International |
| BCN | Barcelona International |
