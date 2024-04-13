#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the
database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def filter_states(username, password, db_name):
    """
    Connects to the MySQL database and lists states starting with 'N'
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

    # Execute SQL query to select states starting with 'N'
    cursor.execute(
        "SELECT id, name FROM states WHERE name LIKE 'N%' ",
        "ORDER BY id ASC"
    )

    # Fetch all rows
    rows = cursor.fetchall()

    # Display results
    print("ID\tNAME")
    print("-" * 10)  # Separator line
    for row in rows:
        state_id, state_name = row
        print(f"{state_id}\t{state_name}")

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Get MySQL username, password, and database name from
    # command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Call filter_states function with provided arguments
    filter_states(mysql_username, mysql_password, db_name)
