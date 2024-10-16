import random
import time

def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3  # Factor de reducción del gap
    sorted = False

    while not sorted:
        # Actualizar el gap
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True  # Asume que está ordenado, a menos que haya intercambios

        # Comparar y hacer intercambios si es necesario
        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]  # Intercambiar
                sorted = False  # Aún no está ordenado, se debe seguir iterando



# Ejemplo de uso
if __name__ == "__main__":

    # Generar un arreglo de 10,000 números aleatorios
    array = [random.randint(0, 100) for _ in range(100)]
      

    # Marca el tiempo inicial
    start_time = time.time()

    # Ordena la lista usando Timsort
    comb_sort(array)
    

    # Marca el tiempo final
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")