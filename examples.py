"""
Example usage of the country_state_city library.
"""

from country_state_city import Country, State, City

def main():
    # Example of using Country
    print("=== Countries ===")
    country = Country.get_country_by_code('US')
    if country:
        print(f"Country: {country.name} ({country.iso2})")
        print(f"Flag: {country.flag}")
        print(f"Currency: {country.currency}")
        print(f"Timezones: {len(country.timezones)}")
        
        if country.timezones:
            print(f"First timezone: {country.timezones[0].name} "
                  f"({country.timezones[0].gmt_offset_name})")
    
    # Example of using State
    print("\n=== States ===")
    states = State.get_states_of_country('US')
    print(f"Number of states in US: {len(states)}")
    
    if states:
        print("First 5 states:")
        for state in states[:5]:
            print(f"- {state.name} ({state.iso_code})")
    
    # Example of using City
    print("\n=== Cities ===")
    cities = City.get_cities_of_state('US', 'CA')
    print(f"Number of cities in California: {len(cities)}")
    
    if cities:
        print("First 5 cities in California:")
        for city in cities[:5]:
            print(f"- {city.name}")

if __name__ == "__main__":
    main()