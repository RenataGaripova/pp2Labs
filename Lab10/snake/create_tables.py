import psycopg2

def create_tables():

    conn = psycopg2.connect(
        host="localhost",
        database="snake_bd",
        user="postgres",
        password="7462"
    )

    commands = (
        """
        CREATE TABLE Users (
            username VARCHAR(255) PRIMARY KEY,
            users_num SERIAL
        )
        """,
        """
        CREATE TABLE User_scores (
            username VARCHAR(255) PRIMARY KEY,
            user_level INTEGER,
            user_score INTEGER
        )
        """,
        )
    try:
        with conn.cursor() as cur:
            # execute the CREATE TABLE statement
            for command in commands:
                cur.execute(command)
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()