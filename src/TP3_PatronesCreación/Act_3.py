from abc import ABC, abstractmethod
class HamburguesaFactory(ABC):
    @abstractmethod
    def crear_hamburguesa(self, nombre):
        pass

class MostradorFactory(HamburguesaFactory):
    def crear_hamburguesa(self, nombre):
        return HamburguesaMostrador(nombre)

class ClienteFactory(HamburguesaFactory):
    def crear_hamburguesa(self, nombre):
        return HamburguesaCliente(nombre)

class DeliveryFactory(HamburguesaFactory):
    def crear_hamburguesa(self, nombre):
        return HamburguesaDelivery(nombre)

class Hamburguesa:
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def entregar(self):
        pass

class HamburguesaMostrador(Hamburguesa):
    def entregar(self):
        return f"La hamburguesa {self.nombre} está lista para ser recogida en el mostrador."

class HamburguesaCliente(Hamburguesa):
    def entregar(self):
        return f"La hamburguesa {self.nombre} ha sido entregada al cliente."

class HamburguesaDelivery(Hamburguesa):
    def entregar(self):
        return f"La hamburguesa {self.nombre} será enviada por delivery."

def main():
    factory = DeliveryFactory()

    hamburguesa = factory.crear_hamburguesa("Especial")

    print(hamburguesa.entregar())


if __name__ == "__main__":
    main()