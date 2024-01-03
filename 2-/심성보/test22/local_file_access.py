import http.server
import socketserver
import os

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

web_dir = os.path.join(os.path.dirname(__file__), "csv-server")
os.chdir(web_dir)

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Server running at port", PORT)
    httpd.serve_forever()
