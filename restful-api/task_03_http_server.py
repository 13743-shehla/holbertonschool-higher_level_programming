import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP Request Handler to manage API endpoints.
    """

    def do_GET(self):
        """
        Handle GET requests for different endpoints.
        """
        if self.path == '/':
            # Default endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            # JSON data endpoint
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            # API status endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            # Information endpoint from expected output
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            # Undefined endpoint handling (404 Not Found)
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server():
    """
    Initialize and start the HTTP server on port 8000.
    """
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Server starting on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
