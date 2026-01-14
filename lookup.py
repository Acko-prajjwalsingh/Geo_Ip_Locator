import maxminddb
import ipaddress  # Built-in module for IP validation

db_file = 'GeoLite2-City.mmdb' 

def run_lookup():
    try:
        # 1. Open the database once at the start
        with maxminddb.open_database(db_file) as reader:
            print("--- MaxMind Pro Lookup (Type 'exit' to quit) ---")
            
            while True:
                ip_input = input("\nEnter an IP address: ").strip()
                
                if ip_input.lower() == 'exit':
                    print("Goodbye!")
                    break

                # 2. VALIDATION CHECK
                try:
                    ip_obj = ipaddress.ip_address(ip_input)
                except ValueError:
                    print(f"❌ Error: '{ip_input}' is not a valid IPv4 or IPv6 address.")
                    continue

                # 3. PRIVATE IP CHECK
                if ip_obj.is_private:
                    print(f"🏠 '{ip_input}' is a PRIVATE (Local) IP address.")
                    print("Note: Private IPs exist only within local networks and cannot be geolocated.")
                    continue
                
                # 4. DATABASE LOOKUP (Only runs if IP is valid and public)
                data = reader.get(ip_input)
                
                if data:
                    city = data.get('city', {}).get('names', {}).get('en', 'N/A')
                    country = data.get('country', {}).get('names', {}).get('en', 'N/A')
                    
                    subdivisions = data.get('subdivisions', [{}])
                    state = subdivisions[0].get('names', {}).get('en', 'N/A')
                    
                    location = data.get('location', {})
                    lat = location.get('latitude', 'N/A')
                    lon = location.get('longitude', 'N/A')
                    radius = location.get('accuracy_radius', 'N/A')

                    print("-" * 30)
                    print(f"📍 City:      {city}")
                    print(f"🏛️  State:     {state}")
                    print(f"🌍 Country:   {country}")
                    print(f"🎯 Accuracy:  {radius} km")
                    print(f"🗺️  Coords:    {lat}, {lon}")
                    print("-" * 30)
                else:
                    print(f"🔍 No geolocation data found in database for: {ip_input}")
                    
    except FileNotFoundError:
        print(f"Error: Could not find {db_file} in the current directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_lookup()