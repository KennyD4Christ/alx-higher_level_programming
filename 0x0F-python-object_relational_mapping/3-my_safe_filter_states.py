#!/usr/bin/python3
"""Module containing a function to search for a state by name in a
MySQL database.

This script retrieves state information from a MySQL database specified by
username, password, and database name provided as command-line arguments.
It searches for states where the name matches the fourth argument provided.

**Example Usage:**

python search_state_by_name.py <username> <password> <database> <state_name>
"""

import MySQLdb


def search_state_by_name(username, password, database, state_name):
    """Connects to the MySQL database and searches for a state by name,
    sorted by id.

    Args:
        username: Username for the MySQL database.
        password: Password for the MySQL database.
        database: Name of the MySQL database.
        state_name: The state name to search for.

    Returns:
        None
    """

    try:
        # Connect to the MySQL database
        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=username, passwd=password, db=database)
        cursor = conn.cursor()

        # Escape the user-provided state name to prevent SQL injection
        # vulnerabilities
        safe_state_name = cursor.escape(state_name).decode()

        # Execute the query with formatted state name, sorted by id
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (safe_state_name,))

        # Fetch all states
        states = cursor.fetchall()

        # Print the results
        if states:
            for state in states:
                print(state)
        else:
            print("No state found")

    except MySQLdb.Error as err:
        print(f"Error connecting to database: {err}")

    finally:
        # Close the connection
        if conn:
            conn.close()

# Get username, password, database name, and state name from command-line
# arguments


if __name__ == "__main__":
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
