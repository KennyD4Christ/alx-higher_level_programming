#!/usr/bin/python3
"""Module containing a function to list cities from a specific state in a
MySQL database.

This script retrieves information about cities belonging to a specified
state from a MySQL database provided by username, password, and database name.
The state name is provided as an additional argument, ensuring safety against
SQL injection.

**Example Usage:**

python list_cities_by_state.py <username> <password> <database> <state_name>
"""

import MySQLdb


def list_cities_by_state(username, password, database, state_name):
    """Connects to the MySQL database and lists cities from a specified state,
    sorted by id.

    Args:
        username: Username for the MySQL database.
        password: Password for the MySQL database.
        database: Name of the MySQL database.
        state_name: The name of the state to search for.

    Returns:
        None
    """

    try:
        # Connect to the MySQL database
        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=username, passwd=password, db=database)
        cursor = conn.cursor()

        # Escape the user-provided state name to prevent SQL injection
        safe_state_name = cursor.escape(state_name).decode()

        # Execute a single query with a parameterized state name
        query = """
            SELECT cities.id, cities.name, states.name AS state_name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """

        cursor.execute(query, (safe_state_name,))

        # Fetch all results
        cities = cursor.fetchall()

        # Check if any cities were found
        if cities:
            # Print the results
            for city in cities:
                print(city)
        else:
            print(f"No city found in state {state_name}")

    except MySQLdb.Error as err:
        print(f"Error connecting to database: {err}")

    finally:
        # Close the connection
        if conn:
            conn.close()

# Get username, password, database name, and state name from
# command-line arguments


if __name__ == "__main__":
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
