import argparse
import os
import cmath

def fraiz():
    parser = argparse.ArgumentParser(description="calcular raiz")
    parser.add_argument("-n", "--number", type=int, help='debe ser un número')
    parser.add_argument("-f", "--fork", action="store true", help="calcula la raiz negativa")
    
    args = parser.parse_args()
    
    r = cmath.sqrt(args.number)

    if args.fork:
        rt = os.fork()
        
        if rt > 0:
            print(f'La raiz positiva es{r}')
        
        elif ft == 0:
            print(f'la raiz negativa es{-r}')
    if not args.fork:
        print(f'La raiz positiva es{r}')

fraiz()

