import psycopg2


def update_score(new_score, username):

    conn = psycopg2.connect(
        host="localhost",
        database="snake_bd",
        user="postgres",
        password="7462"
    )

    sql = """ UPDATE user_scores
                SET user_score = %s
                WHERE username = %s"""
    
    try:
        with  conn.cursor() as cur:
            # execute the UPDATE statement
            cur.execute(sql, (new_score, username))
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def update_level(new_level, username):

    conn = psycopg2.connect(
        host="localhost",
        database="snake_bd",
        user="postgres",
        password="7462"
    )

    sql = """ UPDATE user_scores
                SET user_level = %s
                WHERE username = %s"""
    
    try:
        with  conn.cursor() as cur:
            # execute the UPDATE statement
            cur.execute(sql, (new_level, username))
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)        