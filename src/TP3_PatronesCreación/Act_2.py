class CalculadoraImpuestos:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calcular_impuestos(self, base_imponible):
        iva = base_imponible * 0.21  
        iibb = base_imponible * 0.05  
        contrib_municipales = base_imponible * 0.012  

        total_impuestos = iva + iibb + contrib_municipales  

        return total_impuestos


calculadora_singleton = CalculadoraImpuestos()
impuestos = calculadora_singleton.calcular_impuestos(1000.0)
print("Total de impuestos a pagar:", impuestos)