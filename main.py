from http.server import BaseHTTPRequestHandler, HTTPServer
import http.server

hostName = "localhost"
serverPort = 8080

class MyServer(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Открыть файл main.html
        with open('main.html', 'rb') as f:
            # Прочитать содержимое файла
            html = f.read()

        # Отправить ответ с кодом состояния 200 и заголовком Content-Type
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        # Отправить содержимое файла в теле ответа
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
