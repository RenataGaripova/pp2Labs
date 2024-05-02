import psycopg2

def insert_data_from_console():

    conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="7462"
    )

    N = int(input("How many rows do you want to insert? "))

    with conn.cursor() as cur:
        for i in range(N):
            new_name = input("Enter name: ")
            new_phonenum = input("Enter phone number: ")

            cur.execute(f"""INSERT INTO phone_book (person_name, person_phonenum) VALUES 
                ('{new_name}', '{new_phonenum}');
                """)

            conn.commit()

if __name__ == '__main__':
    insert_data_from_console()