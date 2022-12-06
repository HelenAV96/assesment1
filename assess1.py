import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='assessmentdb',
        user= 'postgres',
        password= 'musikklass96')


def list_data():
    con = get_db_connection()
    cur = con.cursor()
    print(f"SELECT * FROM contacts;")
    cur.execute(f"SELECT * FROM contacts;")
    rows = cur.fetchall()
    cur.close()
    con.close()
    return rows

def add_contact(first_name, last_name, title, organization):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute(f"INSERT INTO contacts VALUES ('{first_name}','{last_name}','{title}','{organization}');")
    cur.execute("COMMIT;")
    cur.close()
    con.close()

def delete_contact(first_name, last_name):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute(f"DELETE FROM contacts WHERE first_name = '{first_name}' and last_name ='{last_name}';")
    cur.execute("COMMIT;")
    cur.close()
    con.close()

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

