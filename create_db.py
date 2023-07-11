import sqlite3
import time
import random

# Create an SQLite database and establish a connection
conn = sqlite3.connect("page_events.db")
cursor = conn.cursor()

# Create the "page_events" table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS page_events (
        id INTEGER PRIMARY KEY,
        project_id INTEGER,
        timestamp INTEGER,
        session_id TEXT,
        country TEXT,
        city TEXT,
        browser TEXT,
        operating_system TEXT,
        path TEXT
    )
""")

# Generate and insert 100 records into the "page_events" table
for i in range(100):
    project_id = random.randint(1, 10)
    current_timestamp = int(time.time())
    one_month_ago = current_timestamp - (30 * 24 * 60 * 60)  # 30 days in seconds
    one_second_before_month_start = current_timestamp - (current_timestamp % (24 * 60 * 60)) - 1
    timestamp = random.randint(one_month_ago, one_second_before_month_start)
    session_id = f"session_{i}"
    country = f"country_{i % 10}"
    city = f"city_{i % 5}"
    browser = f"browser_{i % 3}"
    operating_system = f"os_{i % 2}"
    path = f"path_{i}"

    cursor.execute("""
        INSERT INTO page_events
        (project_id, timestamp, session_id, country, city, browser, operating_system, path)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (project_id, timestamp, session_id, country, city, browser, operating_system, path))

conn.commit()

# Scenario1 Data Mockup
for i in range(5):
    project_id = 10
    current_timestamp = int(time.time())
    one_month_ago = current_timestamp - (30 * 24 * 60 * 60)  # 30 days in seconds
    random_timestamp = random.randint(one_month_ago, current_timestamp)
    session_id = f"session_{i}"
    country = f"country_{i % 3}"
    city = f"city_{i % 2}"
    browser = f"browser_{i % 2}"
    operating_system = f"os_{i % 2}"
    path = f"path_{i}"

    cursor.execute("""
        INSERT INTO page_events
        (project_id, timestamp, session_id, country, city, browser, operating_system, path)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (project_id, random_timestamp, session_id, country, city, browser, operating_system, path))

conn.commit()

# Generate and insert additional records into the "page_events" table
for i in range(10):
    project_id = 10
    current_timestamp = int(time.time())
    start_of_month = int(time.mktime(time.strptime(time.strftime('%Y-%m-01 00:00:00'), '%Y-%m-%d %H:%M:%S')))
    end_of_month = int(time.mktime(time.strptime(time.strftime('%Y-%m-01 00:00:00', time.localtime(current_timestamp + 2592000)), '%Y-%m-%d %H:%M:%S'))) - 1

    timestamp = random.randint(start_of_month, end_of_month)
    session_id = f"session_{i}"
    country = f"country_{i % 10}"
    city = f"city_{i % 5}"
    browser = f"browser_{i % 3}"
    operating_system = f"os_{i % 2}"
    path = f"path_{i}"

    cursor.execute("""
        INSERT INTO page_events
        (project_id, timestamp, session_id, country, city, browser, operating_system, path)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (project_id, timestamp, session_id, country, city, browser, operating_system, path))

conn.commit()

# Generate and insert additional records into the "page_events" table
for i in range(5):
    project_id = 10
    current_timestamp = int(time.time())
    previous_day = int(time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', time.localtime(current_timestamp - 86400)), '%Y-%m-%d %H:%M:%S')))

    timestamp = random.randint(previous_day, current_timestamp)
    session_id = f"session_{i}"
    country = f"country_{i % 10}"
    city = f"city_{i % 5}"
    browser = f"browser_{i % 3}"
    operating_system = f"os_{i % 2}"
    path = f"path_{i}"

    cursor.execute("""
        INSERT INTO page_events
        (project_id, timestamp, session_id, country, city, browser, operating_system, path)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (project_id, timestamp, session_id, country, city, browser, operating_system, path))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("SQLite database created with 100 records in the 'page_events' table.")
