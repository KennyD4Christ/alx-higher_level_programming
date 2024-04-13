#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


def filter_cities(username, password, db_name, state_name):
    """
    Connects to the MySQL database and lists all cities of a given state.
    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Name of the database
        state_name (str): Name of the state to filter cities by
    """
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query with parameter to select cities of the given state
    query = """
            SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id
            """
    cursor.execute(query, (state_name,))

    # Fetch result
    result = cursor.fetchone()[0]

    # Display results
    print(result)

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

    # Call filter_cities function with provided arguments
    filter_cities(mysql_username, mysql_password, db_name, state_name)
