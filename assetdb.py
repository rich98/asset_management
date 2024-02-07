import sqlite3
from datetime import datetime

def create_database():
    conn = sqlite3.connect('asset_management.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE assets
                 (serial_number TEXT, id INTEGER PRIMARY KEY, name TEXT, type TEXT, value REAL, owner TEXT, last_updated TEXT, status TEXT, police_crime_number TEXT)''')

    # Save (commit) the changes
    conn.commit()

    # Close the connection
    conn.close()

def add_asset(serial_number, name, type, value, owner, status, police_crime_number=None):
    valid_statuses = ['active', 'storage', 'stock', 'damaged', 'missing', 'stolen', 'decommissioned']
    if status not in valid_statuses:
        raise ValueError(f"Invalid status. Expected one of: {', '.join(valid_statuses)}")

    if status == 'stolen' and police_crime_number is None:
        raise ValueError("A police crime number is required when the status is 'stolen'")

    conn = sqlite3.connect('asset_management.db')
    c = conn.cursor()

    # Get current time
    now = datetime.now()

    # Format time as string
    timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")

    # Insert a row of data
    c.execute("INSERT INTO assets (serial_number, name, type, value, owner, last_updated, status, police_crime_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (serial_number, name, type, value, owner, timestamp_str, status, police_crime_number))

    # Save (commit) the changes
    conn.commit()

    # Close the connection
    conn.close()

def get_assets():
    conn = sqlite3.connect('asset_management.db')
    c = conn.cursor()

    # Retrieve all assets
    c.execute("SELECT * FROM assets")
    assets = c.fetchall()

    # Close the connection
    conn.close()

    return assets

# Create the database and the table
create_database()

# Add an asset
add_asset('SN12345', 'Laptop', 'Electronics', 1200.00, 'Doe, John', 'active')

# Get all assets
assets = get_assets()
for asset in assets:
    print(asset)
