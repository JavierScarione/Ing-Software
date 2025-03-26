import matplotlib.pyplot as plt

def collatz_iterations(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

# Rango de números a evaluar
n_values = range(1, 10001)
iterations = [collatz_iterations(n) for n in n_values]

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.scatter(n_values, iterations, s=1, color='blue')
plt.xlabel("Número inicial de la secuencia (n)")
plt.ylabel("Número de iteraciones para converger")
plt.title("Número de Collatz para valores de 1 a 10,000")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()