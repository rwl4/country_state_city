# Country State City Python Library

A Python library for accessing country, state, and city data.

## Installation

```bash
pip install country_state_city
```

## Usage

```python
from country_state_city import Country, State, City

# Get all countries
countries = Country.get_countries()

# Get a country by code
usa = Country.get_country_by_code('US')
print(f"Country: {usa.name}, Flag: {usa.flag}")

# Get all states of a country
states = State.get_states_of_country('US')
for state in states[:5]:
    print(f"- {state.name} ({state.iso_code})")

# Get all cities of a state
cities = City.get_cities_of_state('US', 'CA')
print(f"Number of cities in California: {len(cities)}")
```

## Features

- Access to country information (name, ISO code, flag, currency, etc.)
- Access to state/province information
- Access to city information
- Hierarchical relationship between countries, states, and cities
- Timezone information for countries

## Structure

- Country class: For working with country data
- State class: For working with state/province data
- City class: For working with city data
- Timezone class: For working with timezone data

## License

MIT

## Authors

Raymond Lucke (ray@raylucke.com)

## Credits

This library is inspired by and uses data from [country_state_city](https://github.com/paulpascal/country_state_city) by [Paul Pascal](https://github.com/paulpascal).