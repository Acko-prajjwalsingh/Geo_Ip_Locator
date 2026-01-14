import maxminddb

db_file = 'GeoLite2-City.mmdb' 

def run_lookup():
    try:
        with maxminddb.open_database(db_file) as reader:
            print("--- MaxMind Clean Lookup (Type 'exit' to quit) ---")
            
            while True:
                ip = input("\nEnter an IP address: ").strip()
                if ip.lower() == 'exit':
                    break
                
                data = reader.get(ip)
                
                if data:
                    # Extracting specific fields safely using .get() to avoid crashes if a field is missing
                    city = data.get('city', {}).get('names', {}).get('en', 'N/A')
                    country = data.get('country', {}).get('names', {}).get('en', 'N/A')
                    
                    # Subdivisions is a list, so we grab the first item
                    subdivisions = data.get('subdivisions', [{}])
                    state = subdivisions[0].get('names', {}).get('en', 'N/A')
                    
                    location = data.get('location', {})
                    lat = location.get('latitude', 'N/A')
                    lon = location.get('longitude', 'N/A')
                    radius = location.get('accuracy_radius', 'N/A')

                    # Formatting the output
                    print("-" * 30)
                    print(f"📍 City:      {city}")
                    print(f"🏛️  State:     {state}")
                    print(f"🌍 Country:   {country}")
                    print(f"🎯 Accuracy:  {radius} km")
                    print(f"🗺️  Coords:    {lat}, {lon}")
                    print("-" * 30)
                else:
                    print(f"No data found for: {ip}")
                    
    except FileNotFoundError:
        print(f"Error: Could not find {db_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_lookup()