#!/usr/bin/python3
"""Module containing a function to list states starting with 'N' from a
   MySQL database.

This script retrieves state information from a MySQL database specified by
username, password, and database name provided as command-line arguments.
It filters states where the name starts with the letter 'N'.

**Example Usage:**

python list_states_by_name.py <username> <password> <database>
"""

import MySQLdb


def list_states_by_name(username, password, database):
    """Connects to the MySQL database and lists states where the name
        starts with 'N', sorted by id.

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

        # Execute the query to select states starting with 'N' sorted by id
        cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                       "ORDER BY id ASC")

        # Fetch all states
        states = cursor.fetchall()

        # Print the results
        for state in states:
            print(state)

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
