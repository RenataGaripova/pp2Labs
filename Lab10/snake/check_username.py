import psycopg2

def check_username(username):

    conn = psycopg2.connect(
        host="localhost",
        database="snake_bd",
        user="postgres",
        password="7462"
    )

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        return cur.fetchone() is not None