import psycopg2

sql1 = ("SELECT * FROM phone_book WHERE person_name LIKE 'A%'") # Starts with "A"
sql2 = ("SELECT * FROM phone_book WHERE person_phonenum LIKE '+7%0'") # Starts with +7 and ends with 0
sql3 = ("SELECT * FROM phone_book WHERE person_name LIKE '%en%'") # Contains "en"
sql4 =  ("SELECT * FROM phone_book WHERE person_name LIKE 'R%an'") # Starts with "R" and ends with "an"
sql5 = ("SELECT * FROM phone_book WHERE person_phonenum LIKE '_777%7%6'") # "777" goes after a single character and phone number ends with 6

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
    print()
    quiery(sql4)
    print()
    quiery(sql5)