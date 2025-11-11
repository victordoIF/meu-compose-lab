from flask import Flask
import pymysql
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        connection = pymysql.connect(
            host=os.getenv('DB_HOST', 'db'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'senha123'),
            database=os.getenv('DB_NAME', 'meubanco'),
            cursorclass=pymysql.cursors.DictCursor
        )
        connection.close()
        return '<h1>Conexão OK!</h1>'
    except Exception as e:
        return f'<h1>Erro ao conectar</h1><p>{e}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
