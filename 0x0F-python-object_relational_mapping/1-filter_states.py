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
    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' "
                   "GROUP BY id ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
