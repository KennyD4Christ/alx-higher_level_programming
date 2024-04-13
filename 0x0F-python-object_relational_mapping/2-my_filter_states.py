#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa where
name matches the argument.
"""
import MySQLdb
import sys


def filter_states(username, password, db_name, state_name):
    """
    Connects to the MySQL database and filters states based on user input.
    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Name of the database
        state_name (str): State name to search for
    """
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select states matching the provided name
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id" \
        .format(state_name)
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Get MySQL username, password, database name, and state name from
    # command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call filter_states function with provided arguments
    filter_states(mysql_username, mysql_password, db_name, state_name)
