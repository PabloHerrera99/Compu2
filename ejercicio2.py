import argparse

def rep():
    parser = argparse.ArgumentParser("Ingrese un texto y una cantidad de repeticiones")
    parser.add_argument("secuencia", help = "La secuencia se repetira x cantidad de veces")
    parser.add_argument("var1", metavar="n", type = int, help="Ingrese numero entero positivo")
    args = parser.parse_args()
    print((args.secuencia + " ")* args.var1)
rep()
