from abc import ABC, abstractmethod


class Numero(ABC):

    @abstractmethod
    def imprimir_valor(self) -> None:
        pass

class OperacionDecorator(Numero):
    def __init__(self, numero: Numero) -> None:
        self._numero = numero

    def imprimir_valor(self) -> None:
        self._numero.imprimir_valor()


class SumarDosDecorator(OperacionDecorator):
    def imprimir_valor(self) -> None:
        super().imprimir_valor()
        print(f" + 2 = {self._numero.valor + 2}")


class MultiplicarPorDosDecorator(OperacionDecorator):

    def imprimir_valor(self) -> None:
        super().imprimir_valor()
        print(f" * 2 = {self._numero.valor * 2}")


class DividirPorTresDecorator(OperacionDecorator):
    def imprimir_valor(self) -> None:
        super().imprimir_valor()
        print(f" / 3 = {self._numero.valor / 3}")


class NumeroSimple(Numero):
    def __init__(self) -> None:
        self.valor = self._obtener_numero()

    def _obtener_numero(self) -> int:
        while True:
            try:
                valor = int(input("Ingrese un número (positivo y diferente de cero): "))
                if valor <= 0:
                    print("El número debe ser positivo y diferente de cero. Por favor, Inténtelo de nuevo.")
                else:
                    return valor
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

    def imprimir_valor(self) -> None:
        print(f"Número: {self.valor}")


# Ejemplos:
numero = NumeroSimple()
numero.imprimir_valor()

print("\nRealizando operaciones:")

numero_sumar_dos = SumarDosDecorator(numero)
numero_sumar_dos.imprimir_valor()

numero_multiplicar_por_dos = MultiplicarPorDosDecorator(numero)
numero_multiplicar_por_dos.imprimir_valor()
numero_dividir_por_tres = DividirPorTresDecorator(numero)
numero_dividir_por_tres.imprimir_valor()