# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: old_primes.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-05-06 18:42:35 UTC (1746556955)

import os
import sys

lower = int(sys.argv[1]) if len(sys.argv) > 1 else 1
upper = int(sys.argv[2]) if len(sys.argv) > 1 else 50

os.system('cls')

print('Numeros primeos entre %d y %d son: \n' % (lower, upper))

if lower>upper:
    print("Por favor ingrese nuevamente dos valores")
    exit()
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print('%d ' % num)