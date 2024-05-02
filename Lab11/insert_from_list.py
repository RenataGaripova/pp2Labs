import psycopg2

some_data = [
    ("John Doe", "+77054567890"),
    ("Jane Smith", "+77055678901"),
    ("Alice Johnson", "+77056789012"),
    ("Bob Brown", "+77057890123"),
    ("Emily Davis", "+77088901234"),
    ("Michael Wilson", "+77089012345"),
    ("Sarah Martinez", "+77080123456"),
    ("David Anderson", "+77081234567"),
    ("Jessica Taylor", "+77082345678"),
    ("Christopher Thomas", "+77773456789"),
    ("Jennifer Lee", "+77774567890"),
    ("Matthew Garcia", "+77775678901"),
    ("Laura Hernandez", "+77776789012"),
    ("Kevin Miller", "+77777890123"),
    ("Amanda Rodriguez", "+77778901234")
]

def insert_from_list(lst):
    
    incorrect = []

    conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="7462"
    )

    with conn.cursor() as cur:
        for i in range(len(lst)):
            new_name = lst[i][0]
            new_phone= lst[i][1]
            if len(new_phone) == 12 and new_phone[0] == "+" and new_phone[1:].isdigit():
                cur.execute("SELECT * FROM phone_book WHERE person_name = %s", (new_name,))
                if cur.fetchone() == None:
                    cur.execute(f"""INSERT INTO phone_book (person_name, person_phonenum) VALUES 
                        ('{new_name}', '{new_phone}');
                        """)
                    print("New row was added.")
                    conn.commit()
                else:
                    cur.execute(""" UPDATE phone_book SET person_phonenum = %s WHERE person_name = %s""", 
                        (new_phone, new_name))
                    print("Old row was updated.")
                    conn.commit()
            else:
                incorrect.append(lst[i])

    return incorrect


if __name__ == '__main__':
    insert_from_list(some_data)