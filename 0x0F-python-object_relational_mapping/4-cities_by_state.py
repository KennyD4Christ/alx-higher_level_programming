#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


def cities_by_state(username, password, db_name):
    """
    Connects to the MySQL database and lists all cities by state.
    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Name of the database
    """
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select all cities by state
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id
            """
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
    # Get MySQL username, password, and database name from
    # command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Call cities_by_state function with provided arguments
    cities_by_state(mysql_username, mysql_password, db_name)
