import random
import time


# Implementación del algoritmo Gnome Sort
def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr


# Ejemplo de uso
if __name__ == "__main__":

    # Generar un arreglo de 10,000 números aleatorios
    array = [random.randint(0, 100) for _ in range(8509)]

    # Marca el tiempo inicial
    start_time = time.time()

    # Ordena la lista usando Gnome Sort
    gnome_sort(array)

    # Marca el tiempo final
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")
