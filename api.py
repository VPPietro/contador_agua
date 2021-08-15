from http.server import HTTPServer, SimpleHTTPRequestHandler


class HandlerClass(SimpleHTTPRequestHandler):
    def do_GET(self):
        SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-lenght']))

        data = b'<html><body><h1>POST!</h1></body></html>'
        self.wfile.write(bytes(data))
        return


Handler = HandlerClass

http = HTTPServer(('localhost', 8000), Handler)
http.serve_forever()
