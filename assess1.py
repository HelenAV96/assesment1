import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='assessmentdb',
    user= 'postgres',
    password= 'musikklass96')


def read_data():
    con = get_db_connection()
    cur = con.cursor()
    print(f"SELECT * FROM contacts;")
    cur.execute(f"SELECT * FROM contacts;")
    rows = cur.fetchall()
    cur.close()
    con.close()
    return rows