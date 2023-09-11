import http.server
import socketserver

# GET / HTTP/1.1

PORT = 1111


class handler_manual (http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("REQUEST: ", self.requestline)
        if self.path == "/stoneface":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open("stoneface.html", "rb") as f:
                self.wfile.write(f.read())
        elif self.path == "/siksong_clown":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open("silksong_clown.html", "rb") as f:
                self.wfile.write(f.read())
        elif self.path == "/dalinar":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open("dalinar.html", "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b'Not Found')

socketserver.TCPServer.allow_reuse_address = True
myhttphandler = handler_manual

httpd = http.server.HTTPServer(("", PORT), myhttphandler)

print(f"Opening httpd server at port {PORT}")

httpd.serve_forever()

httpd.shutdown()