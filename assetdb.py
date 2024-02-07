import sqlite3

def create_database():
    conn = sqlite3.connect('asset_management.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE assets
                 (id INTEGER PRIMARY KEY, name TEXT, type TEXT, value REAL, owner TEXT)''')

    # Save (commit) the changes
    conn.commit()

    # Close the connection
    conn.close()

def add_asset(name, type, value, owner):
    conn = sqlite3.connect('asset_management.db')
    c = conn.cursor()

    # Insert a row of data
    c.execute("INSERT INTO assets (name, type, value, owner) VALUES (?, ?, ?, ?)",
              (name, type, value, owner))

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
add_asset('Laptop', 'Electronics', 1200.00, 'rich 98')

# Get all assets
assets = get_assets()
for asset in assets:
    print(asset)
