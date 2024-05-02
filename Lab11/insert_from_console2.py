import psycopg2

def insert_data_from_console():

    conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="7462"
    )

    N = int(input("How many rows do you want to insert or update? "))

    with conn.cursor() as cur:
        for i in range(N):
            
            new_name = input("Enter name: ")
            new_phonenum = input("Enter phone number: ")

            cur.execute("SELECT * FROM phone_book WHERE person_name = %s", (new_name,))
            if cur.fetchone() == None:
                cur.execute(f"""INSERT INTO phone_book (person_name, person_phonenum) VALUES 
                    ('{new_name}', '{new_phonenum}');
                    """)
                print("New row was added.")
                conn.commit()
            else:
                cur.execute(""" UPDATE phone_book SET person_phonenum = %s WHERE person_name = %s""", 
                    (new_phonenum, new_name))
                print("Old row was updated.")
                conn.commit()

if __name__ == '__main__':
    insert_data_from_console()