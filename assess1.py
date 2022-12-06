import psycopg2

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

def add_contact(first_name, last_name):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute(f"INSERT INTO contacts VALUES ('{first_name}','{last_name}');")
    cur.execute("COMMIT;")
    cur.close()
    con.close()

def delete_contact(name):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute(f"DELETE FROM contacts WHERE name = '{name}';")
    cur.execute("COMMIT;")
    cur.close()
    con.close()