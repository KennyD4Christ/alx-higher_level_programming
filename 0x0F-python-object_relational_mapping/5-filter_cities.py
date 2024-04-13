#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


def get_cities_by_state(username: str, password: str, database: str,
                        state: str) -> None:
    """
    Retrieves and prints the list of cities in the given state.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state (str): Name of the state.

    Returns:
        None
    """
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        cursor = db.cursor()
        cursor.execute("SELECT cities.name FROM cities JOIN states ON "
                       "cities.state_id = states.id WHERE states.name = %s "
                       "ORDER BY cities.id ASC", (state,))

        cities = cursor.fetchall()

        print(", ".join(city[0] for city in cities))

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        if 'db' in locals() and db.open:
            cursor.close()
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state = sys.argv[1:]

    get_cities_by_state(username, password, database, state)
