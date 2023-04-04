import argparse

def impar():
    parser = argparse.ArgumenParser(description="Ingrese un numero")
    parser.add_argument("var1", metavar="n", type = int, help="Ingrese numero entero positivo")
    args = parser.parse_args()
    print([i for i in range(1,args.var1*2,2)])

impar()