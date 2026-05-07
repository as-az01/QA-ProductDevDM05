import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("/data/mydatabase.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
            email TEXT
)
""")
            
# Insert data
cursor.execute("""
INSERT INTO users (name, email)
VALUES (?, ?)
""", ("Alice", "alice@example.com"))
            
cursor.execute("""
INSERT INTO users (name, email)
VALUES (?, ?)
""", ("Bob", "bob@example.com"))
            
# Commit changes
conn.commit()
            
# Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
            
print("Users in database:")
for row in rows:
    print(row)
                    
# Close connection
conn.close()