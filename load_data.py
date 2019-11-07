import sqlite3
from sqlite3 import Error


def execute_script_file(conn, file_name):
    try:
        scriptFile = open(actors_file, 'r')
        script = scriptFile.read()
        scriptFile.close()
        cursor = conn.cursor()
        print("Loading %s ..." % file_name)
        cursor.executescript(script)
        print("%s loaded." % file_name)
    except Error as e:
        print(e)
    finally:
        if cursor:
            cursor.close()


def migrate_database(db_file, actors_file, movies_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        execute_script_file(conn, actors_file)
        execute_script_file(conn, movies_file)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    db_file = r"./movies-actors.db"
    actors_file = r"./data_files/actors.sql"
    movies_file = r"./data_files/movies.sql"
    migrate_database(db_file, actors_file, movies_file)
