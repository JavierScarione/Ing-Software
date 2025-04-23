import os
from abc import ABC, abstractmethod


class Director:

    def set_builder(self, builder):
        self._builder = builder

    def get_airplane(self):
        airplane = Airplane()

        airplane.set_body(self._builder.get_body())

        for _ in range(2):
            airplane.attach_engine(self._builder.get_engine())

        for _ in range(2):
            airplane.attach_wing(self._builder.get_wing())

        airplane.set_landing_gear(self._builder.get_landing_gear())

        return airplane


class Airplane:

    def __init__(self):
        self._engines = []
        self._wings = []
        self._body = None
        self._landing_gear = None

    def set_body(self, body):
        self._body = body

    def attach_engine(self, engine):
        self._engines.append(engine)

    def attach_wing(self, wing):
        self._wings.append(wing)

    def set_landing_gear(self, landing_gear):
        self._landing_gear = landing_gear

    def specification(self):
        print("Cuerpo: %s" % self._body.shape)
        print("Número de turbinas: %d" % len(self._engines))
        print("Número de alas: %d" % len(self._wings))
        print("Tipo de tren de aterrizaje: %s" % self._landing_gear.type)


class Builder(ABC):

    @abstractmethod
    def get_engine(self): pass

    @abstractmethod
    def get_wing(self): pass

    @abstractmethod
    def get_body(self): pass

    @abstractmethod
    def get_landing_gear(self): pass


class AirplaneBuilder(Builder):

    def get_engine(self):
        return Engine()

    def get_wing(self):
        return Wing()

    def get_body(self):
        return Body()

    def get_landing_gear(self):
        return LandingGear()


class Engine:
    pass


class Wing:
    pass


class Body:
    def __init__(self):
        self.shape = "Fuselaje estándar"


class LandingGear:
    def __init__(self):
        self.type = "Retráctil"


def main():
    airplane_builder = AirplaneBuilder()
    director = Director()
    director.set_builder(airplane_builder)
    airplane = director.get_airplane()
    airplane.specification()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avión\n")
    main()