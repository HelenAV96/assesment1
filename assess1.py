import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='assessmentdb',
        user= 'postgres',
        password= 'musikklass96')


def list_data(conn):
    conn = get_db_connection()
    cur = conn.cursor()
    print(f"SELECT * FROM contacts;")
    cur.execute(f"SELECT * FROM contacts;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def add_contact(conn, first_name, last_name, title, organization):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO contacts VALUES ('{first_name}','{last_name}','{title}','{organization}');")
    cur.execute("COMMIT;")
    cur.close()
    conn.close()

def delete_contact(conn, first_name, last_name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM contacts WHERE first_name = '{first_name}' and last_name ='{last_name}';")
    cur.execute("COMMIT;")
    cur.close()
    conn.close()

while True:
    print("Hello and welcome to contacts! Choose between the following command: LIST, INSERT,DELETE")
    command = input("What would you like to do?:")

    if command == INSERT:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        title =  input("Title: ")
        organization = input("organization: ")
        add_contact()

    elif command == DELETE:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        delete_contact()

    elif command == LIST:
        list_data()

