import psycopg

class user_connection():
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=Lab_C user=postgres password=12345 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "user"(name, phone) VALUES(%(name)s, %(phone)s)
            """, data)
        self.commit()    

    def __def__(self):
        self.conn.close()