import os

import psycopg2
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return get_template()


def get_template():
    conn = psycopg2.connect(os.environ['PG_DSN'])
    try:
        cur = conn.cursor()
        cur.execute('select * from templates')
        text = cur.fetchone()
        cur.close()
        return text[0]
    # connection usage
    finally:
        conn.close()
