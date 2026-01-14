# GeoLite IP Lookup Tool

A lightweight Python utility to perform offline IP geolocation lookups using the MaxMind DB format. This tool provides city, state, country, and coordinate data for any public IP address.

## Features
- **Offline Lookups:** Uses a local `.mmdb` database for near-instant results.
- **Interactive CLI:** Simply type an IP address to get location details.
- **Validation:** Automatically detects and filters out private/local IP addresses.

---

## Prerequisites

Before running this tool, you will need:
1. **Python 3.x** installed on your system.
2. **MaxMind GeoLite2 City Database** (See instructions below).

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/GeoLite.git](https://github.com/YOUR_USERNAME/GeoLite.git)
   cd GeoLite
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 📥 How to Download the Database

Due to licensing and file size, the `.mmdb` database is not included in this repository.

1. Go to the MaxMind GeoLite2 Download Page and sign up for a free account if needed.
2. Download the **GeoLite2 City** file (GZIP or ZIP).
3. Extract the archive and locate `GeoLite2-City.mmdb`.
4. Move `GeoLite2-City.mmdb` into the root of this project folder (same level as `lookup.py`).

## Usage

Ensure your virtual environment is active, then run:

```bash
python3 lookup.py
```
The CLI will prompt for an IP address and print city/country/coordinates. Type `exit` to quit.

## Example

Run the CLI and enter an IP address. Example session (user input shown after the prompt):

```text
Enter an IP address: 157.45.217.113
------------------------------
📍 City:      Bengaluru
🏛️  State:     Karnataka
🌍 Country:   India
🎯 Accuracy:  500 km
🗺️  Coords:    12.9753, 77.591
------------------------------
```

If you prefer a different path for the DB, edit the `db_file` variable at the top of `lookup.py`.
