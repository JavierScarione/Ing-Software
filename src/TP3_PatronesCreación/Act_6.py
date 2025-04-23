import time
from datetime import datetime
import copy
import os


from abc import ABC, abstractmethod


class Prototype(ABC):
    def __init__(self):
        time.sleep(3)
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None


    @abstractmethod
    def clone(self):
        pass



class Shopkeeper(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        time.sleep(3)
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        self.charisma = 30

    def clone(self):
        return copy.deepcopy(self)


class Warrior(Prototype):
    def __init__(self, height, age, defense, attack):
        self.stamina = 60

    def clone(self):
        return copy.deepcopy(self)


class Mage(Prototype):
    def __init__(self, height, age, defense, attack):
        self.mana = 100

    def clone(self):
        return copy.deepcopy(self)


os.system("clear")
print("Ejemplo de taller para patrón prototipo")

dt = datetime.now()
print('Comienzo creando un objeto Shopkeeper NPC: ', dt)
shopkeeper = Shopkeeper(180, 22, 5, 8)

dt = datetime.now()
print('Finaliza la creación del objeto Shopkeeper NPC: ', dt)
print('Atributos: ' + ', '.join("%s: %s" % item for item in vars(shopkeeper).items()))

dt = datetime.now()
print('Instanciando ahora trader: ', dt)
for i in range(5):
    shopkeeper = Shopkeeper(180, 22, 5, 8)
    dt = datetime.now()
    print(f'Creo Shopkeeper NPC {i} at: ', dt)

dt = datetime.now()
print('Finalizó de crear el grupo trader: ', dt)

dt = datetime.now()
print('Puedo hacerlo masivamente con 10 NPCs: ', dt)
shopkeeper_template = Shopkeeper(180, 22, 5, 8)
warrior_template = Warrior(185, 22, 4, 21)
mage_template = Mage(172, 65, 8, 15)
for i in range(3):
    shopkeeper_clone = shopkeeper_template.clone()
    warrior_clone = warrior_template.clone()
    mage_clone = mage_template.clone()
    dt = datetime.now()
    print(f'Finaliza la creación de tripletes mediante clone {i} at: ', dt)

dt = datetime.now()
print('Finalizó la creación de la población NPC: ', dt)



def procesamiento_carga_anidado(n):
    if n > 0:
        print(f"Anidamiento {n}")
        time.sleep(2)  
        procesamiento_carga_anidado(n-1)


print("Comenzando anidamientos:")
procesamiento_carga_anidado(20)
print("Finalizó anidamientos.")