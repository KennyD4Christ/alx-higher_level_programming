#!/usr/bin/python3
"""Module containing a function to list all cities from a MySQL database.

This script retrieves city information from a MySQL database specified by
username, password, and database name provided as command-line arguments.

**Example Usage:**

python list_all_cities.py <username> <password> <database>
"""

import MySQLdb


def list_all_cities(username, password, database):
    """Connects to the MySQL database and lists all cities sorted by id.

    Args:
        username: Username for the MySQL database.
        password: Password for the MySQL database.
        database: Name of the MySQL database.

    Returns:
        None
    """

    try:
        # Connect to the MySQL database
        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=username, passwd=password, db=database)
        cursor = conn.cursor()

        # Execute a single query to fetch all cities and states (using JOIN)
        query = """
            SELECT cities.id, cities.name, states.name AS state_name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """

        cursor.execute(query)

        # Fetch all results
        cities = cursor.fetchall()

        # Print the results
        for city in cities:
            print(city)

    except MySQLdb.Error as err:
        print(f"Error connecting to database: {err}")

    finally:
        # Close the connection
        if conn:
            conn.close()

# Get username, password, and database name from command-line arguments


if __name__ == "__main__":
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
