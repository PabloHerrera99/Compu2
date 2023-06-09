import os
import argparse

parser = argparse.ArgumentParser(description='ingrese 2 matrices 2x2')
parser.add_argument('-m1', nargs='*', type=int)
parser.add_argument('-m2', nargs='*', type=int)

args = parser.parse_args()
m1 = args.m1
m2 = args.m2

fifo_00 = '/tmp/fifo_00'

if not os.path.exists(fifo_00):
    os.mkfifo(fifo_00)


pid1 = os.fork()
if pid1 == 0:
    fifo = open(fifo_00, 'w')
    mat = str(m1[0]*m2[0]+m1[2]*m2[1])
    fifo.write(mat + '\n')
    fifo.close()
    os._exit(0)

pid2 =os.fork()
if pid2 == 0:
    fifo = open(fifo_00, 'w')
    mat = str(m1[1]*m2[0]+m1[3]*m2[1])
    fifo.write(mat + '\n')
    fifo.close()
    os._exit(0)

pid3 =os.fork()
if pid3 == 0:
    fifo = open(fifo_00, 'w')
    mat = str(m1[0]*m2[2]+m1[2]*m2[3])
    fifo.write(mat + '\n')
    fifo.close()
    os._exit(0)

pid4 =os.fork()
if pid4 == 0:
    fifo = open(fifo_00, 'w')
    mat = str(m1[1]*m2[2]+m1[3]*m2[3])
    fifo.write(mat + '\n')
    fifo.close()
    os._exit(0)

fifo = open(fifo_00, 'r')

os.waitpid(pid1, 0)
os.waitpid(pid2, 0)
os.waitpid(pid3, 0)
os.waitpid(pid4, 0)

cont = fifo.read()
fifo.close()
print(cont)