import random,time

def bucket_sort(arr):
    # Encontrar el valor máximo y mínimo
    min_val = min(arr)
    max_val = max(arr)
    
    # Definir el número de cubetas
    bucket_count = len(arr)
    # Crear las cubetas vacías
    buckets = [[] for _ in range(bucket_count)]
    
    # Distribuir los elementos en las cubetas
    for num in arr:
        # Determinar en qué cubeta colocar el número
        index = int((num - min_val) / (max_val - min_val + 1) * bucket_count)
        buckets[index].append(num)
    
    # Ordenar individualmente cada cubeta
    for bucket in buckets:
        bucket.sort()
    
    # Recoger los elementos de las cubetas en orden
    sorted_arr = []

    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr



# Ejemplo de uso
if __name__ == "__main__":

    # Generar un arreglo de 10,000 números aleatorios
    array = [random.randint(0, 1000) for _ in range(100)]
      

    # Marca el tiempo inicial
    start_time = time.time()

    # Ordena la lista usando Timsort
    array=bucket_sort(array)
    
    # Marca el tiempo final
    end_time = time.time()

    print(array)

    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")
