class LaminaAcero:

    def __init__(self, espesor, ancho, tren_laminador):
        self.espesor = espesor
        self.ancho = ancho
        self.tren_laminador = tren_laminador

    def producir(self):
        self.tren_laminador.producir_lamina(self)


class TrenLaminador:
    def producir_lamina(self, lamina):
        pass


class TrenLaminador5Metros(TrenLaminador):
    def producir_lamina(self, lamina):
        print(f"Produciendo lámina de {lamina.espesor}\" de espesor y {lamina.ancho} metros de ancho en el tren laminador de 5 metros.")


class TrenLaminador10Metros(TrenLaminador):
    def producir_lamina(self, lamina):
        print(f"Produciendo lámina de {lamina.espesor}\" de espesor y {lamina.ancho} metros de ancho en el tren laminador de 10 metros.")


# Ejemplo1:
lamina = LaminaAcero(0.5, 1.5, TrenLaminador5Metros())
lamina.producir()

# Ejemplo2:
otra_lamina = LaminaAcero(0.5, 1.5, TrenLaminador10Metros())
otra_lamina.producir()