from mysqldb import database
import mysql
import json
from http import server

db = database
db.nome_database = 'aguadatabase'
db.cria_db(db)

data = {
    'pietro': 250,
    'neto': 200,
    'giovanni': 150
}


class Handler(server.BaseHTTPRequestHandler):

    server_address = ('', 8000)

    def run(self, server_class=server.HTTPServer):
        self.aguadb = mysql.connector.connect(
            host = "localhost",
            user = "root2",
            password = "toor")
        httpd = server_class(self.server_address, self)
        httpd.serve_forever()

    def do_GET(self):
        cursor = self.aguadb.cursor(dictionary=True)
        cursor.execute(f"USE {db.nome_database}")
        cursor.execute(f"SELECT * FROM {db.nome_database}.usuario")
        data = cursor.fetchall()
        print(data)
        self.send_response(200)
        self.end_headers()
        # self.wfile.write(f'{data}')

handling = Handler
Handler.run(handling)
