"""
    Javier Scarione, Ingeniería de Software II, 2025

    “copyright UADER_FCyT_IS2 © 2022,2024 todos los derechos reservados"

    Este script imprime todos los números primos entre dos valores dados como argumentos.
    Incluye manejo de errores y una clase para verificar primalidad con eficiencia mejorada.

"""

import os
import sys
import math

class PrimeChecker:
    """
    Clase que encapsula la lógica para determinar si un número es primo.
    """
    def compute(self, number: int) -> bool:
        if number <= 1:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

def main():
    try:
        lower = int(sys.argv[1]) if len(sys.argv) > 1 else 1
        upper = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    except ValueError:
        print("Por favor ingrese valores enteros válidos.")
        sys.exit(1)

    if lower > upper:
        print("Por favor ingrese nuevamente dos valores.")
        sys.exit(1)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Números primos entre {lower} y {upper} son:\n')

    checker = PrimeChecker()
    # Crear una lista de primos como strings
    primes = [str(num) for num in range(lower, upper + 1) if checker.compute(num)]

    # Imprimir todos en la misma línea
    print(" ".join(primes))

if __name__ == '__main__':
    main()
