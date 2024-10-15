import random,time

def pigeonhole_sort(arr):
    # Encontrar el valor mínimo y máximo
    min_val = min(arr)
    max_val = max(arr)
    
    # Calcular el rango del arreglo
    rango = max_val - min_val + 1
    
    # Crear las casillas (pigeonholes)
    casillas = [[] for _ in range(rango)]
    
    # Colocar cada elemento en su casilla correspondiente
    for num in arr:
        casillas[num - min_val].append(num)
    
    # Recoger los elementos de las casillas y devolver el arreglo ordenado
    i = 0
    for casilla in casillas:
        for num in casilla:
            arr[i] = num
            i += 1



# Ejemplo de uso
if __name__ == "__main__":

    # Generar un arreglo de 10,000 números aleatorios
    array = [random.randint(0, 1000) for _ in range(8509)]
      

    # Marca el tiempo inicial
    start_time = time.time()

    # Ordena la lista usando Timsort
    pigeonhole_sort(array)
    
    # Marca el tiempo final
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")

