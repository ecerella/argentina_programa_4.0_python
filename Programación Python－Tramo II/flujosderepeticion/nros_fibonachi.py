
# Definir una función recursiva para calcular números Fibonacci
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

# Llamar a la función para obtener los primeros 10 números de Fibonacci
fibonacci_sequence = fibonacci(10)

# Imprimir la secuencia
print(fibonacci_sequence)
