import argparse
import os

parser = argparse.ArgumentParser(description='Insert one file')
parser.add_argument('-f', type=str, help = 'the name of the file you want to open')
arg = parser.parse_args()
file = arg.f

r2, w2 = os.pipe()

with open(file, 'r') as file:
    contents = file.read()
    lines = contents.split('\n')

for line in lines:

    r, w = os.pipe()

    pid = os.fork()
    if pid == 0:
        os.close(w)
        inv = os.read(r, 1024)
        inv2 = (inv.decode()[::-1] + '\n')

        os.close(r)
        os.close(r2)
        os.write(w2, inv2.encode())
        os.close(w2)
        os._exit(0)
    else:
        os.close(r)
        print(line.encode())
        os.write(w, line.encode())
        os.close(w)

        os.waitpid(pid, 0)
os.close(w2)

while True:
    inv = os.read(r2, 1024)
    if not inv: 
        break
    print(inv.decode())
os.close(r2)
