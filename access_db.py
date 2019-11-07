import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def get_longest_running_movie(conn):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM movies
                    ORDER BY runtime DESC 
                    LIMIT 1;""")

    rows = cur.fetchall()
    if rows and len(rows) > 0:
        print(rows[0])


def get_longest_running_movie(conn):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM movies
                    ORDER BY runtime DESC 
                    LIMIT 1;""")

    rows = cur.fetchall()
    if rows and len(rows) > 0:
        print(rows[0])


def get_movie_with_most_actors(conn):
    cur = conn.cursor()
    cur.execute("""WITH big_movie(nactors, movie_id) 
                    AS (
                        SELECT COUNT(DISTINCT imdb_id) AS nactors, 
                                movie_id
                        FROM actors 
                        GROUP BY movie_id
                        ORDER BY nactors DESC LIMIT 1
                        )
                    SELECT * FROM movies, big_movie WHERE movies.id=big_movie.movie_id;""")
    rows = cur.fetchall()
    if rows and len(rows) > 0:
        print(rows[0])


def get_movies_by_rating(conn):
    cur = conn.cursor()
    cur.execute("""select distinct rating from movies;""")
    ratings = cur.fetchall()
    for rating in ratings:
        print("Movies with rating %s " % rating[0])
        cur.execute("select * from movies where rating='%s';" % rating[0])
        movies = cur.fetchall()
        for movie in movies:
            print(movie)


def main():
    database = r"./movies-actors.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query longest running movie: ")
        get_longest_running_movie(conn)

        print("2. Query movie with most actors: ")
        get_movie_with_most_actors(conn)

        print("2. Query movies by rating: ")
        get_movies_by_rating(conn)


if __name__ == '__main__':
    main()
