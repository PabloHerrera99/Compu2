
import os
from PIL import Image
from http.server import BaseHTTPRequestHandler, HTTPServer
from multiprocessing import Process, Pipe

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