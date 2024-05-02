import psycopg2

sql_name = "DELETE FROM phone_book WHERE person_name = %s"
sql_phone = "DELETE FROM phone_book WHERE person_phonenum = %s"


def delete_data(data, sql):

    conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="7462"
    )

    rows_deleted = 0

    try:
      with conn.cursor() as cur:
            cur.execute(sql, (data,))
            rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted

if __name__ == '__main__':
    choose = input("Enter 'name' if you want to delete rows with specific name. Otherwise, enter 'phone': ")

    if choose == 'name':
        name_to_del = input("Enter name: ")
        delete_data(name_to_del, sql_name)
    elif choose == 'phone':
        phone_to_del = input("Enter phone: ")
        delete_data(phone_to_del, sql_phone)
    else:
        print("Incorrect input data.")