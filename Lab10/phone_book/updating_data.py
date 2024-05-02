import psycopg2

def update_name():
    sql = """ UPDATE phone_book
                SET person_name = %s
                WHERE person_id = %s"""
    
    return sql
    
def update_phone():
    sql = """ UPDATE phone_book
                SET person_phonenum = %s
                WHERE person_id = %s"""
    
    return sql

def update_rows(upd_data, id, sql):

    conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="7462"
    )

    updated_row_count = 0
    
    try:
        with  conn.cursor() as cur:
            # execute the UPDATE statement
            cur.execute(sql, (upd_data, id))
            updated_row_count = cur.rowcount
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count

if __name__ == '__main__':

    old_id = input("Enter id. ")
    choose = input("Enter 'name' if you want to change name. Otherwise, enter 'phone'. ")

    if choose == 'name':
        new_name = input('Enter new name.')

        query = update_name()

        update_rows(new_name, old_id, query)

    elif choose == 'phone':
        new_phone = input('Enter new phone number.')

        query = update_phone()

        update_rows(new_phone, old_id, query)
    
    else:
        print("Incorrect input data.")