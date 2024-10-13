import os
import pandas as pd

MIN_RUN = 32

def insertion_sort(arr, left, right, key):
    """
    Realiza Insertion Sort en una sublista del DataFrame desde 'left' hasta 'right' (inclusive),
    utilizando una columna del DataFrame como clave para ordenar (nombre del autor en este caso).
    
    Parámetros:
    arr: DataFrame a ordenar.
    left: índice inicial de la sublista.
    right: índice final de la sublista.
    key: columna utilizada para la comparación.
    """
    for i in range(left + 1, right + 1):
        key_item = arr.iloc[i]
        j = i - 1
        
        # Desplaza los elementos mayores que key_item[key] hacia la derecha
        while j >= left and arr.iloc[j][key] > key_item[key]:
            arr.iloc[j + 1] = arr.iloc[j]
            j -= 1
        
        # Coloca el key_item en su posición correcta
        arr.iloc[j + 1] = key_item




def merge(arr, left, mid, right, key):
    """
    Fusiona dos sublistas ordenadas en un solo DataFrame ordenado.
    
    Parámetros:
    arr: DataFrame a fusionar.
    left: índice inicial de la primera sublista.
    mid: índice final de la primera sublista.
    right: índice final de la segunda sublista.
    key: columna utilizada para la comparación.
    """
    # Crea las sublistas
    left_part = arr.iloc[left:mid + 1].copy()
    right_part = arr.iloc[mid + 1:right + 1].copy()

    i = j = 0
    k = left
    
    # Fusiona las sublistas comparando elementos
    while i < len(left_part) and j < len(right_part):
        if left_part.iloc[i][key] <= right_part.iloc[j][key]:
            arr.iloc[k] = left_part.iloc[i]
            i += 1
        else:
            arr.iloc[k] = right_part.iloc[j]
            j += 1
        k += 1

    # Añade los elementos restantes de la sublista izquierda
    while i < len(left_part):
        arr.iloc[k] = left_part.iloc[i]
        i += 1
        k += 1

    # Añade los elementos restantes de la sublista derecha
    while j < len(right_part):
        arr.iloc[k] = right_part.iloc[j]
        j += 1
        k += 1





def tim_sort(df, key):
    """
    Implementa el algoritmo Timsort para ordenar un DataFrame basado en una columna clave.
    
    Parámetros:
    df: DataFrame a ordenar.
    key: columna utilizada para la comparación (en este caso 'Autor').
    """
    n = len(df)
    
    # Ordena pequeños subarrays (runs) usando Insertion Sort
    for i in range(0, n, MIN_RUN):
        insertion_sort(df, i, min(i + MIN_RUN - 1, n - 1), key)
    

    # Fusiona los runs ordenados mediante Merge Sort
    size = MIN_RUN
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            
            # Fusiona si hay elementos para combinar
            if mid < end:
                merge(df, start, mid, end, key)
        
        # Duplica el tamaño del run a fusionar
        size *= 2





# Ejemplo de uso
if __name__ == "__main__":

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, '..', 'data', 'data.csv')



    # Cargar el DataFrame desde el CSV
    df = pd.read_csv(file_path,nrows=20, encoding='utf-8',)
    
    # Columna clave (nombre del autor) para el ordenamiento
    columna_clave = 'Authors'

    # Convertir la columna clave 'Authors' a tipo string
    df['Authors'] = df['Authors'].astype(str)

    # Ordena el DataFrame usando Timsort en la columna clave
    tim_sort(df, columna_clave)
    
    # Muestra el DataFrame ordenado
    for i in range(len(df)):
        print('_________________________________________________')
        print(df.iloc[i])
