import http.server
import socketserver as so

PORT = 8080
handler = http.server.SimpleHTTPRequestHandler

with so.TCPServer(("", PORT), handler) as httpd:
	print ("Server Running")
	httpd.serve_forever()
