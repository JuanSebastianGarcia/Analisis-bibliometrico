import os
import pandas as pd
import time

MIN_RUN = 32

def insertion_sort(arr, left, right):
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
        while j >= left and comparar_datos(arr.iloc[j], key_item):
            arr.iloc[j + 1] = arr.iloc[j]
            j -= 1
        
        # Coloca el key_item en su posición correcta
        arr.iloc[j + 1] = key_item


def merge(arr, left, mid, right):
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
        
        if comparar_datos(right_part.iloc[j],left_part.iloc[i]):
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


def tim_sort(df):
    """
    Implementa el algoritmo Timsort para ordenar un DataFrame basado en una columna clave.
    
    Parámetros:
    df: DataFrame a ordenar.
    key: columna utilizada para la comparación (en este caso 'Autor').
    """
    n = len(df)
    
    # Ordena pequeños subarrays (runs) usando Insertion Sort
    for i in range(0, n, MIN_RUN):
        insertion_sort(df, i, min(i + MIN_RUN - 1, n - 1))
    

    # Fusiona los runs ordenados mediante Merge Sort
    size = MIN_RUN
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            
            # Fusiona si hay elementos para combinar
            if mid < end:
                merge(df, start, mid, end)
        
        # Duplica el tamaño del run a fusionar
        size *= 2

    return df



def comparar_datos(dato1, dato2):
    """
    Compara dos registros para determinar cuál está primero en orden alfabético, cronológico, por fuente,
    base de datos y finalmente por cantidad de citaciones.

    Parámetros:
    - dato1: Primer registro con información de autores, año, afiliaciones, fuente, base de datos y citaciones.
    - dato2: Segundo registro con información de autores, año, afiliaciones, fuente, base de datos y citaciones.

    Retorna:
    - True: Si dato1 es mayor que dato2.
    - False: Si dato1 es menor que dato2.
    """

    # Obtener el primer autor y manejar valores nulos o vacíos
    autor1 = (dato1.get('Authors', '').strip() or ' ')[0].lower()
    autor2 = (dato2.get('Authors', '').strip() or ' ')[0].lower()

    # Comparación directa de autores
    if autor1 != autor2:
        return autor1 > autor2

    # Si los autores son iguales, comparar por año
    year1 = dato1.get('Year', 0)
    year2 = dato2.get('Year', 0)

    if year1 != year2:
        return year1 > year2

    # Si los años también son iguales, comparar por afiliaciones
    afiliacion1 = (dato1.get('Affiliations', '').strip() or ' ')[0].lower()
    afiliacion2 = (dato2.get('Affiliations', '').strip() or ' ')[0].lower()

    if afiliacion1 != afiliacion2:
        return afiliacion1 > afiliacion2

    # Si las afiliaciones son iguales, comparar por el título de la fuente (Source title)
    source_title1 = (dato1.get('Source title', '').strip() or ' ')[0].lower()
    source_title2 = (dato2.get('Source title', '').strip() or ' ')[0].lower()

    if source_title1 != source_title2:
        return source_title1 > source_title2

    # Si los títulos de fuente también son iguales, comparar por la base de datos (Source)
    source1 = (dato1.get('Source', '').strip() or ' ')[0].lower()
    source2 = (dato2.get('Source', '').strip() or ' ')[0].lower()

    if source1 != source2:
        return source1 > source2

    # Si la base de datos es igual, comparar por la cantidad de citaciones (Cited by)
    cited_by1 = dato1.get('Cited by', 0)
    cited_by2 = dato2.get('Cited by', 0)

    return cited_by1 >= cited_by2



def convertir_columnas(df):
    """
    Convierte las columnas específicas del DataFrame al tipo de dato adecuado.
    
    - 'Authors', 'Affiliations', 'Source title', 'Source': Se convierten a cadenas (string).
    - 'Year', 'Cited by': Se convierten a enteros (int), manejando valores nulos como 0.
    
    Parámetros:
    - df: DataFrame a transformar.
    
    Retorna:
    - df: DataFrame con las columnas convertidas al tipo de dato adecuado.
    """

    # Convertir la columna 'Authors' a tipo string
    df['Authors'] = df['Authors'].astype(str).fillna('')

    # Convertir la columna 'Affiliations' a tipo string
    df['Affiliations'] = df['Affiliations'].astype(str).fillna('')

    # Convertir la columna 'Source title' a tipo string
    df['Source title'] = df['Source title'].astype(str).fillna('')

    # Convertir la columna 'Source' a tipo string
    df['Source'] = df['Source'].astype(str).fillna('')

    # Convertir la columna 'Year' a tipo entero, manejar NaN
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce').fillna(0).astype(int)

    # Convertir la columna 'Cited by' a tipo entero, manejar NaN
    df['Cited by'] = pd.to_numeric(df['Cited by'], errors='coerce').fillna(0).astype(int)

    return df



# Ejemplo de uso
if __name__ == "__main__":

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'data.csv')



    # Cargar el DataFrame desde el CSV
    df = pd.read_csv(file_path,nrows=500, encoding='utf-8',)
    
    df=convertir_columnas(df)
    # Ordena el DataFrame usando Timsort en la columna clave
    df_sorted=tim_sort(df)

    
    # Extraer la dirección donde será guardado el archivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    direccion = os.path.join(base_dir, 'data', 'dataOrd.csv')

    
    # Marca el tiempo inicial
    start_time = time.time()

    # Ordena la lista usando Timsort
    tim_sort(df)
    
    # Marca el tiempo final
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")




    # Guardar el archivo limpio en formato CSV
    df_sorted.to_csv(direccion, index=False)