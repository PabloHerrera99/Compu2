import argparse

def leer():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", metavar = "F", type = str, help = "ingrese un archivo")
    args = parser.parse_args()

    try:
        with open(args.file, "r") as file:
            cont = file.read
            print("cantidad de lineas:" + len(cont))
            print("cantidad de palabras:" + len(cont.splitlines()))
