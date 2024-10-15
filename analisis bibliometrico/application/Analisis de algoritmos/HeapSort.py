import random
import time


# Función para ajustar el heap
def heapify(arr, n, i):
    largest = i  # Inicializar el nodo raíz como el más grande
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho

    # Verificar si el hijo izquierdo es más grande que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verificar si el hijo derecho es más grande que el más grande actual
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Cambiar y continuar ajustando si la raíz no es el más grande
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Función principal para realizar HeapSort
def heap_sort(arr):
    n = len(arr)

    # Construir el heap (reorganizar el arreglo)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Mover la raíz actual al final
        heapify(arr, i, 0)

# Ejemplo de uso
if __name__ == "__main__":

    # Generar un arreglo de 10,000 números aleatorios
    array = [random.randint(0, 100) for _ in range(100)]

    # Marca el tiempo inicial
    start_time = time.time()

    # Ordena la lista usando Gnome Sort
    heap_sort(array)

    # Marca el tiempo final
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")
