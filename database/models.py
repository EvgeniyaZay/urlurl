import psycopg2
from psycopg2 import Error
from pydantic.networks import HttpUrl
from database.cursor import cur, conn
from pydantic import BaseModel

class Item(BaseModel):
    url: HttpUrl

def write_data_db(long_url: str, short_url: str):
    try:    
        sql = f"""
        INSERT INTO "links"("long", "short")
        VALUES('{long_url}', '{short_url}')
        returning *   
        """
        # values = (short_url, long_url)
        cur.execute(sql)
        conn.commit()
    except (Exception, Error) as error:
        print("ERRRROOrr", error)

def get_links(code: str):
    # sql = f"""
    # CREATE INDEX index_name ON links (short) 
    # """ 
    cur.execute("SET enable_seqscan TO on")
    cur.execute(
        f"""
        EXPLAIN (ANALYZE, BUFFERS)
        SELECT "long"
        FROM "links"
        WHERE "short" = '{code}'
        """
    )
    return cur.fetchone()