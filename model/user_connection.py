import psycopg

class user_connection():
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=Lab_C user=postgres password=12345 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    # Primera Sentencia CRUD

    def read_all(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM "user"
            """)
            return data.fetchall()
        self.conn.commit()

    def read_one(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM "user" WHERE id = %s
            """,(id,))
            return data.fetchone()
        self.conn.commit()

    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "user"(name, phone) VALUES(%(name)s, %(phone)s)
            """, data)
        self.conn.commit()    

    def __def__(self):
        self.conn.close()