#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) == 1:
    print("Debe especificar un rango en formato 'desde-hasta'")
    sys.exit()

try:
    desde, hasta = map(int, sys.argv[1].split('-'))
    if desde > hasta:
        print("El primer número debe ser menor o igual al segundo número")
        sys.exit()
    
    for num in range(desde, hasta + 1):
        print(f"Factorial {num}! es {factorial(num)}")
except ValueError:
    print("Debe especificar un rango válido en formato 'desde-hasta'")

