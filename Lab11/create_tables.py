import psycopg2

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE phone_book (
            person_id SERIAL PRIMARY KEY,
            person_name VARCHAR(255) NOT NULL,
            person_phonenum VARCHAR(255) NOT NULL
        )
        """,
        )
    
    conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="7462"
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