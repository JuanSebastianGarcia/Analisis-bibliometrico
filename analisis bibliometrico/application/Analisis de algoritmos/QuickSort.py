import random
import time

# Generar un arreglo de tamaño 100 con números aleatorios
arreglo = [random.randint(0, 100) for _ in range(100)]

# Implementación del algoritmo QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Ordenar el arreglo
arreglo_ordenado = quicksort(arreglo)


if __name__ == "__main__":

    # Generar un arreglo de 10,000 números aleatorios
    array = [random.randint(0, 100) for _ in range(100)]

    # Marca el tiempo inicial
    start_time = time.time()

    # Ordena la lista usando Gnome Sort
    quicksort(array)

    # Marca el tiempo final
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")