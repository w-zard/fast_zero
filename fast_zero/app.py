from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/html', response_class=HTMLResponse)
def read_html():
    return """
    <html>
      <head>
        <title> Nosso olá mundo! </title>
      </head>
      <body>
        <h1> Olá Mundo! </h1>
      </body>
    </html>"""
