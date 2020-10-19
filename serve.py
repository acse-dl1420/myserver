import http.server
import socketserver

PORT = 80


class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><head><title>Title goes here.</title></head>")
        self.wfile.write(b"<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        self.wfile.write((f"<p>You accessed path: {self.path}</p>"
                         ).encode('ascii'))
        self.wfile.write(b"</body></html>")


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
