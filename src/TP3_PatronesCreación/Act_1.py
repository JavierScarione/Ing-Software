
class CalcularFactorial:
    _instance = None 

    def __new__(cls):

        if cls._instance is None:  
            cls._instance = super().__new__(cls)  
            cls._instance.result_cache = {}  
        return cls._instance

    def factorial(self, n):
        if n in self.result_cache:
            return self.result_cache[n]  
        if n == 0:
            result = 1
        else:
            result = n * self.factorial(n - 1)  
        self.result_cache[n] = result 


calcular = CalcularFactorial()
print(calcular.factorial(4))
print(calcular.factorial(6))