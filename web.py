from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        """Analiza la URL solicitada."""
        return urlparse(self.path)

    def query_data(self):
        """Obtiene los parámetros de la query string."""
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        """Maneja la petición GET y envía la respuesta."""
        # Captura de los headers del request
        host = self.headers.get('Host')  # Extraer el valor del header 'Host'
        user_agent = self.headers.get('User-Agent')  # Extraer el valor del header 'User-Agent'

        # Verificar la ruta solicitada
        if self.path == '/':
            # Servir la página de inicio (home.html)
            self.send_response(200)  # Código de respuesta 200 OK
            self.send_header("Content-Type", "text/html")  # Establecer el tipo de contenido como HTML
            self.send_header("Server", "CustomPythonServer")  # Agregar header 'Server'
            self.send_header("Date", self.date_time_string())  # Agregar header 'Date'
            self.end_headers()  # Finaliza el envío de headers
            self.wfile.write(self.get_homepage().encode("utf-8"))  # Escribir la respuesta
        elif self.path.startswith('/proyecto/web-uno'):
            # Ruta específica para el proyecto web-uno
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Server", "CustomPythonServer")
            self.send_header("Date", self.date_time_string())
            self.end_headers()
            self.wfile.write(self.get_response(host, user_agent).encode("utf-8"))
        else:
            # Ruta no encontrada, responder con un error 404
            self.send_error(404, "Página no encontrada")

    def get_homepage(self):
        """Lee y devuelve el contenido del archivo home.html."""
        try:
            with open('home.html', 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return "<h1>Error: Página de inicio no encontrada</h1>"

    def get_response(self, host, user_agent):
        """Genera una respuesta dinámica según la ruta y query string."""
        parsed_url = self.url()  # Analiza la URL solicitada
        query_data = self.query_data()  # Obtiene los parámetros de la query string

        if parsed_url.path == '/proyecto/web-uno':
            autor = query_data.get('autor', 'desconocido')  # Obtiene el valor de 'autor' o 'desconocido' por defecto
            content = f"<h1>Proyecto: web-uno Autor: {autor}</h1>"  # Genera el contenido dinámico basado en la query string
        else:
            content = f"""
            <h1> Hola Web </h1>
            <p> URL Parse Result : {self.url()}         </p>
            <p> Path Original: {self.path}         </p>
            <p> Headers: {self.headers}      </p>
            <p> Query: {self.query_data()}   </p>
            <p> Host: {host}   </p>
            <p> User-Agent: {user_agent}   </p>
            """  # Contenido por defecto si la ruta no coincide

        return content


if __name__ == "__main__":
    print("Starting server on port 8000")  # Mensaje actualizado para reflejar el nuevo puerto
    server = HTTPServer(("localhost", 8000), WebRequestHandler)  # Cambiado el puerto de 8080 a 8000
    server.serve_forever()
