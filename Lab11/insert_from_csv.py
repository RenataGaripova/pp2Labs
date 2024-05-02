import psycopg2
import csv

f = open('/Users/Рената/PP2/Lab10/phone_book/students.csv')

def insert_data_from_csv(filename='students.csv'):
    conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="7462"
    )
    with conn.cursor() as cur:
            csvreader = csv.reader(f, delimiter=',')
            for row in csvreader:
                name, id, study_year, phone_number = row
    
                # Create new students
                cur.execute(f"""INSERT INTO phone_book (person_name, person_phonenum) VALUES 
                ('{name}', '{phone_number}');
                """)

                conn.commit()

if __name__ == '__main__':
    insert_data_from_csv()