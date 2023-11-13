import argparse
from PIL import Image
from Forking import ForkingHTTPServer
from Image import ImageProcessingHandler


try:
    from PIL import Image
except ImportError:
    print("Error: Pillow no está instalado. Intalelo")

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