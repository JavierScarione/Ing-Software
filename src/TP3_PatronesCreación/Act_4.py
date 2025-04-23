
from abc import ABC, abstractmethod


class Factura(ABC):
    @abstractmethod
    def generar_factura(self):
        pass

class FacturaFactory:


    @staticmethod
    def crear_factura(importe_total, condicion_impositiva):

        if condicion_impositiva == "IVA Responsable":
            return FacturaIVAResponsable(importe_total)
        elif condicion_impositiva == "IVA No Inscripto":
            return FacturaIVANoInscripto(importe_total)
        elif condicion_impositiva == "IVA Exento":
            return FacturaIVAExento(importe_total)
        else:
            raise ValueError("Condición impositiva no válida")


class FacturaIVAResponsable(Factura):

    def __init__(self, importe_total):
        self.importe_total = importe_total

    def generar_factura(self):
        impuesto = self.importe_total * 0.21
        total_con_impuesto = self.importe_total + impuesto
        return f"Factura para IVA Responsable - Importe total: ${total_con_impuesto:.2f} (IVA incluido)"


class FacturaIVANoInscripto(Factura):

    def __init__(self, importe_total):
        self.importe_total = importe_total

    def generar_factura(self):
        return f"Factura para IVA No Inscripto - Importe total: ${self.importe_total:.2f}"


class FacturaIVAExento(Factura):

    def __init__(self, importe_total):
        self.importe_total = importe_total

    def generar_factura(self):
        return f"Factura para IVA Exento - Importe total: ${self.importe_total:.2f}"


# Ejemplos 
factura1 = FacturaFactory.crear_factura(1000, "IVA Responsable")
print(factura1.generar_factura())

factura2 = FacturaFactory.crear_factura(800, "IVA No Inscripto")
print(factura2.generar_factura())

factura3 = FacturaFactory.crear_factura(500, "IVA Exento")
print(factura3.generar_factura())