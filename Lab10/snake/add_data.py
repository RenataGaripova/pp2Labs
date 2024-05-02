import psycopg2

def add_data(username):

    conn = psycopg2.connect(
        host="localhost",
        database="snake_bd",
        user="postgres",
        password="7462"
    )

    with conn.cursor() as cur:

        cur.execute(f"""INSERT INTO Users (username) VALUES 
                ('{username}');
                """)

        cur.execute(f"""INSERT INTO User_scores (username, user_level, user_score) VALUES 
                ('{username}', {0}, {0});
                """)
        
        conn.commit()