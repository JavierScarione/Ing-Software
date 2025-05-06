from abc import ABC, abstractmethod

class Componente(ABC):
    @abstractmethod
    def mostrar(self):
        pass


class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(f"Pieza: {self.nombre}")


class Subconjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self):
        print(f"Subconjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar()

producto_principal = Subconjunto("Producto Principal")

subconjunto_1 = Subconjunto("Subconjunto 1")
subconjunto_2 = Subconjunto("Subconjunto 2")
subconjunto_3 = Subconjunto("Subconjunto 3")

for i in range(4):
    subconjunto_1.agregar(Pieza(f"Pieza {i+1}"))
    subconjunto_2.agregar(Pieza(f"Pieza {i+5}"))
    subconjunto_3.agregar(Pieza(f"Pieza {i+9}"))

producto_principal.agregar(subconjunto_1)
producto_principal.agregar(subconjunto_2)
producto_principal.agregar(subconjunto_3)

print("Estructura del producto principal sin el subconjunto opcional:")
producto_principal.mostrar()

subconjunto_opcional = Subconjunto("Subconjunto Opcional")
for i in range(4):
    subconjunto_opcional.agregar(Pieza(f"Pieza Opcional {i+1}"))

producto_principal.agregar(subconjunto_opcional)

print("\nEstructura del producto principal agregando el subconjunto opcional:")
producto_principal.mostrar()