import psycopg2, time

def create_table():
    # функция для подключения к базе данных
    cur.execute("""CREATE TABLE links(
        id BIGSERIAL NOT NULL PRIMARY KEY,
        long VARCHAR(256) NOT NULL,
        short VARCHAR(256) NOT NULL unique
        )""")
    conn.commit() 
while True:
    try:
        conn = psycopg2.connect(
            dbname = 'mydb',
            user = 'postgres',
            password = '0000',
            host = 'postgres', 
            port = 5432
        )
        cur = conn.cursor()
        
        print("Connecteing")
        break
    except Exception as error:
        print("Connecting error")
        print("Error:", error)
        time.sleep(2)
