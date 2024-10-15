import random
import time

# Generar un arreglo de tamaño 100 con números aleatorios
arreglo = [random.randint(0, 100) for _ in range(100)]

# Función para obtener el dígito máximo en un número del arreglo
def max_digit(arr):
    return max(arr)


# Función para hacer el conteo de dígitos en el arreglo
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Contar las ocurrencias de cada dígito
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Actualizar el conteo para que contenga las posiciones finales de los dígitos
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el arreglo de salida
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copiar el arreglo de salida al original
    for i in range(n):
        arr[i] = output[i]

# Función para aplicar Radix Sort
def radix_sort(arr):
    max_num = max_digit(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Ordenar el arreglo
radix_sort(arreglo)


if __name__ == "__main__":

    # Generar un arreglo de 10,000 números aleatorios
    array = [random.randint(0, 100) for _ in range(100)]

    # Marca el tiempo inicial
    start_time = time.time()

    # Ordena la lista usando Gnome Sort
    radix_sort(array)

    # Marca el tiempo final
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")
