import sqlite3

def fetch_data(sql):
    conn = sqlite3.connect("page_events.db")

    # Create a cursor
    cursor = conn.cursor()

    # Execute the SELECT query
    cursor.execute(sql)

    # Fetch the results
    results = cursor.fetchall()
    # Close the connection
    conn.close()
    return results

if __name__ == "__main__":
    # Connect to the database
    conn = sqlite3.connect("page_events.db")

    # Create a cursor
    cursor = conn.cursor()

    # Execute the SELECT query
    cursor.execute("""
        SELECT COUNT(DISTINCT session_id) AS visitors
        FROM page_events
        WHERE project_id = 10
        AND timestamp >= strftime('%s', 'now', 'start of month', '-1 month')
        AND timestamp <= strftime('%s', 'now', 'start of month', '-1 second')
    """)

    # Fetch the results
    results = cursor.fetchall()
    print(results)
    # Print the results
    for row in results:
        print(row)

    # Close the connection
    conn.close()