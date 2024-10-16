import random
import time

# Generar un arreglo de tamaño 100 con números aleatorios
arreglo = [random.randint(0, 100) for _ in range(100)]

# Función para comparar e intercambiar
def compare_and_swap(arr, i, j, asc):
    if (asc and arr[i] > arr[j]) or (not asc and arr[i] < arr[j]):
        arr[i], arr[j] = arr[j], arr[i]

# Función para construir una secuencia bitónica
def bitonic_merge(arr, low, cnt, asc):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            compare_and_swap(arr, i, i + k, asc)
        bitonic_merge(arr, low, k, asc)
        bitonic_merge(arr, low + k, k, asc)

# Función para ordenar una secuencia en forma bitónica
def bitonic_sort(arr, low, cnt, asc):
    if cnt > 1:
        k = cnt // 2
        bitonic_sort(arr, low, k, True)  # Ordenar la primera mitad de forma ascendente
        bitonic_sort(arr, low + k, k, False)  # Ordenar la segunda mitad de forma descendente
        bitonic_merge(arr, low, cnt, asc)

# Función principal para Bitonic Sort
def sort(arr):
    n = len(arr)
    bitonic_sort(arr, 0, n, True)

# Ordenar el arreglo
sort(arreglo)


if __name__ == "__main__":

    # Generar un arreglo de 10,000 números aleatorios
    array = [random.randint(0, 100) for _ in range(100000)]

    # Marca el tiempo inicial
    start_time = time.time()

    # Ordena la lista usando Gnome Sort
    sort(array)

    # Marca el tiempo final
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")

