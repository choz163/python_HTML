from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('html/index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/catalog':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('html/catalog.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/category':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('html/category.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/contacts':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('html/contact.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()

def run_server(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
