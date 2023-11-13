import argparse
import os
import socket
from PIL import Image
from socketserver import ForkingMixIn
from http.server import BaseHTTPRequestHandler, HTTPServer
from multiprocessing import Process, Pipe

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow no está instalado. Intalelo")

class ImageProcessingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        archivo_imagen = '/Users/pabloherrera/Documents/GitHub/Compu2/TPs/Tp2/stormlight.jpeg' #Cambiar el path para que funcione
        imagen_procesada = self.procesar_imagen(archivo_imagen)
        self.send_response(200)
        self.send_header('Content-type', 'image/jpeg')
        self.end_headers()
        try:
            self.wfile.write(imagen_procesada)
        except BrokenPipeError:
            print("Cierre de conexion")

    def procesar_imagen(self, archivo_entrada): 
        print("Creando un pipe")
        parent_pipe, child_pipe = Pipe()
        p = Process(target=self.procesar_imagen_child, args=(archivo_entrada, child_pipe))
        p.start()
        imagen_procesada = parent_pipe.recv()
        p.join() 
        return imagen_procesada

    def procesar_imagen_child(self, archivo_entrada, conn): 
        print (f"Creando Hijo ID:{os.getpid()}")
        temp = 'temp.jpg'
        im = Image.open(archivo_entrada).convert('L')
        im.save(temp)
        with open(temp, 'rb') as f:
            imagen_procesada = f.read()
        conn.send(imagen_procesada)
        os.remove(temp)
        print("hijo terminado")

class ForkingHTTPServer(ForkingMixIn, HTTPServer):
    def __init__(self, server_address, RequestHandlerClass):
        if ':' in server_address[0]:                
            self.address_family = socket.AF_INET6
        else:
            self.address_family = socket.AF_INET
        super().__init__(server_address, RequestHandlerClass)

def run_server(ip, puerto):
    handler = ImageProcessingHandler
    server = ForkingHTTPServer((ip, puerto), handler)

    print(f"Servidor HTTP en http://{ip}:{puerto}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print(" Servidor detenido.")

def main():
    parser = argparse.ArgumentParser(description='Servidor HTTP concurrente para procesar imágenes')
    parser.add_argument('-i', '--ip',default='::', help='Dirección IP del servidor')
    parser.add_argument('-p', '--puerto', type=int, default=8000, help='Puerto del servidor')
    args = parser.parse_args()
    
    run_server(args.ip, args.puerto)


if __name__ == '__main__':
    main()
    
    #python3 tp2.py -i 127.0.0.1 -p 8080