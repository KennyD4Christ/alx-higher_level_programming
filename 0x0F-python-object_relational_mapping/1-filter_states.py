#!/usr/bin/python3
"""
Script to list all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username, password, database = sys.argv[1:]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' "
                   "ORDER BY id")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Create a set to store unique names (ignoring case)
    unique_names = set(row[1].lower() for row in rows)

    # Print results with id and name
    for name in unique_names:
        for row in rows:
            if row[1].lower() == name:  # Match names (case-insensitive)
                print(f"({row[0]}, '{row[1]}')")  # Print id and name
                break  # Exit inner loop once a match is found

    # Close cursor and database connection
    cursor.close()
    db.close()
