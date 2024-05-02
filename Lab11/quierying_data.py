import psycopg2

sql1 = ("SELECT person_name, person_phonenum, person_id  FROM phone_book ORDER BY person_name")
sql2 = ("SELECT person_name, person_phonenum, person_id FROM phone_book ORDER BY person_id")
sql3 = ("SELECT person_name, person_phonenum, person_id FROM phone_book ORDER BY person_phonenum")

def quiery(sql):
    
    conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="7462"
    )

    try:
      with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()

            print("The number of parts: ", cur.rowcount)
            for row in rows:
                print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    quiery(sql1)
    print()
    quiery(sql2)
    print()
    quiery(sql3)