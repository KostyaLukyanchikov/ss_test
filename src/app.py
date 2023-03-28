import os

import psycopg2
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
def root(request: Request):
    return get_template(request)


def get_text():
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


def get_template(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'text': get_text()})
