import os, time
import pandas as pd
import sys
import matplotlib.pyplot as plt
sys.setrecursionlimit(8000)  # Aumentar el límite de recursión


def quicksort(df):
    if len(df) <= 1:
        return df
    else:
        # Selecciona un pivote (puede ser el elemento en la mitad)
        pivot = df.iloc[len(df) // 2]

        # Dividir en tres: menores, iguales y mayores al pivote
        left = df[df.apply(lambda row: comparar_datos(pivot, row), axis=1)]
        middle = df[df.apply(lambda row: not comparar_datos(row, pivot) and not comparar_datos(pivot, row), axis=1)]
        right = df[df.apply(lambda row: comparar_datos(row, pivot), axis=1)]

        
        # Recursivamente ordenar las particiones izquierda y derecha
        return pd.concat([quicksort(left), middle, quicksort(right)], ignore_index=True)




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

    return cited_by1 > cited_by2




def convertir_columnas(df):
    df['Authors'] = df['Authors'].astype(str).fillna('')
    df['Affiliations'] = df['Affiliations'].astype(str).fillna('')
    df['Source title'] = df['Source title'].astype(str).fillna('')
    df['Source'] = df['Source'].astype(str).fillna('')
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce').fillna(0).astype(int)
    df['Cited by'] = pd.to_numeric(df['Cited by'], errors='coerce').fillna(0).astype(int)
    return df



#metodo que inicia el proceso
if __name__ == "__main__":

    #extraer el archivo csv con la data a ordenar
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'data.csv')

    df = pd.read_csv(file_path, nrows=9246, encoding='utf-8')


    #estandarizar las columnas del dataframe
    df = convertir_columnas(df) 
    
    #ordenar el dataframe
    df_sorted = quicksort(df)
    
    # Extraer la dirección donde será guardado el archivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    direccion = os.path.join(base_dir, 'data', 'dataOrd.csv')


    # Guardar el archivo limpio en formato CSV
    df_sorted.to_csv(direccion, index=False)
    
