from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
#from gpiozero import CamJamKitRobot, DistanceSensor, LED, Button
#from signal import pause

hostName = "localhost"
serverPort = 8080
encoding = "utf-8"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("forward"):
          print("Go Forward")
          self.send_response(200)
          self.send_header("Content-type", "text/text")
          self.end_headers()
          self.wfile.write(bytes("Forward", encoding))
          x = 7
        elif self.path.endswith("backward"):
          print("Go Backward")
          self.send_response(200)
          self.send_header("Content-type", "text/text")
          self.end_headers()
          self.wfile.write(bytes("Backward", encoding))
        elif self.path.endswith("left"):
          print("Go left")
          self.send_response(200)
          self.send_header("Content-type", "text/text")
          self.end_headers()
          self.wfile.write(bytes("Left", encoding))
        elif self.path.endswith("right"):
          print("Go right")
          self.send_response(200)
          self.send_header("Content-type", "text/text")
          self.end_headers()
          self.wfile.write(bytes("Right", encoding))
        elif self.path.endswith("slow"):
          print("Go 10 percent slower")
          self.send_response(200)
          self.send_header("Content-type", "text/text")
          self.end_headers()
          self.wfile.write(bytes("Slow", encoding))
        elif self.path.endswith("fast"):
          print("Go 10 percent faster")
          self.send_response(200)
          self.send_header("Content-type", "text/text")
          self.end_headers()
          self.wfile.write(bytes("Fast", encoding))
        else:
          # Send a static file to the client
          self.send_response(200)
          root = os.path.join(os.path.dirname(os.path.abspath(__file__)))
          if self.path == '/':
            filename = root + '/index.html'
          else:
            filename = root + self.path
          if filename[-4:] == '.css':
            self.send_header('Content-type', 'text/css')
          elif filename[-5:] == '.json':
            self.send_header('Content-type', 'application/javascript')
          elif filename[-3:] == '.js':
            self.send_header('Content-type', 'application/javascript')
          elif filename[-4:] == '.ico':
            self.send_header('Content-type', 'image/x-icon')
          else:
            self.send_header('Content-type', 'text/html')
          self.end_headers()
          with open(filename, 'rb') as fh:
            html = fh.read()
            self.wfile.write(html)

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
