from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    # Diccionario que almacena el contenido HTML para cada ruta
    contenido = {
        '/': """<!DOCTYPE html>
                <html lang="es">
                <head><title>Pagina de Inicio</title></head>
                <body>
                    <h1>Bienvenido a la pagina de inicio, Soy Eduardo Marquez y este video es para el profe mariosky :DDD</h1>
                    <p>Esta es la pagina principal, seleccione una de los siguientes links</p>
                    <a href="/proyecto/web-uno">Proyecto Web Uno</a><br>
                    <a href="/proyecto/web-dos">Proyecto Web Dos</a><br>
                    <a href="/proyecto/web-tres">Proyecto Web Tres</a><br>
                </body>
                </html>""",
        '/proyecto/web-uno': """<!DOCTYPE html>
                                <html lang="es">
                                <head><title>Proyecto Web Uno :3</title></head>
                                <body>
                                    <h1>Proyecto: Web Uno :33</h1>
                                    <p>Este es el contenido del proyecto Web Uno.</p>
                                </body>
                                </html>""",
        '/proyecto/web-dos': """<!DOCTYPE html>
                                <html lang="es">
                                <head><title>Proyecto Web Dos :D</title></head>
                                <body>
                                    <h1>Proyecto: Web Dos :DD</h1>
                                    <p>Este es el contenido del proyecto Web Dos.</p>
                                </body>
                                </html>""",
        '/proyecto/web-tres': """<!DOCTYPE html>
                                <html lang="es">
                                <head><title>Proyecto Web Tres :0</title></head>
                                <body>
                                    <h1>Proyecto: Web Tres:00</h1>
                                    <p>Este es el contenido del proyecto Web Tres.</p>
                                </body>
                                </html>"""
    }

    def do_GET(self):
        # Obtener la ruta solicitada
        path = self.path

        # Verificar si la ruta solicitada existe en el diccionario
        if path in self.contenido:
            # Si la ruta existe, enviar respuesta con el contenido correspondiente
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(self.contenido[path].encode("utf-8"))
        else:
            # Si la ruta no existe, enviar un error 404
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write("<h1>Error 404: Página no encontrada</h1>")

if __name__ == "__main__":
    print("Starting server on port 8000")  # Puerto 8000
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
    server.serve_forever()
