#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self):
        pass
    
    def calcular_factorial(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact
    
    def run(self, min, max):
        if min > max:
            print("El primer número debe ser menor o igual al segundo número")
            return
        for num in range(min, max + 1):
            print(f"Factorial {num}! es {self.calcular_factorial(num)}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Debe especificar un rango en formato 'desde-hasta', '-hasta' o 'desde-'")
        sys.exit()

    try:
        arg = sys.argv[1]
        if '-' in arg:
            partes = arg.split('-')
            if arg.startswith('-'):
                desde, hasta = 1, int(partes[1])
            elif arg.endswith('-'):
                desde, hasta = int(partes[0]), 60
            else:
                desde, hasta = map(int, partes)
        else:
            print("Formato inválido. Use 'desde-hasta', '-hasta' o 'desde-'")
            sys.exit()
        
        factorial_calculator = Factorial()
        factorial_calculator.run(desde, hasta)
    except ValueError:
        print("Debe especificar un rango válido en formato 'desde-hasta', '-hasta' o 'desde-'")


