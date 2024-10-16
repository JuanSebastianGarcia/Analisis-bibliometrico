import os, time
import pandas as pd

def quicksort(df):
    if len(df) <= 1:
        return df
    else:
        pivot = df.iloc[len(df) // 2]
        left = df[df.apply(lambda row: comparar_datos(pivot, row), axis=1)]
        middle = df[df.apply(lambda row: not comparar_datos(row, pivot) and not comparar_datos(pivot, row), axis=1)]
        right = df[df.apply(lambda row: comparar_datos(row, pivot), axis=1)]
        
        return pd.concat([quicksort(left), middle, quicksort(right)], ignore_index=True)




def comparar_datos(dato1, dato2):
    # Comparación por autor
    autor1 = dato1['Authors'].split(',')[0].strip().lower() if pd.notna(dato1['Authors']) else ''
    autor2 = dato2['Authors'].split(',')[0].strip().lower() if pd.notna(dato2['Authors']) else ''
    if autor1 != autor2:
        return autor1 > autor2

    # Comparación por año
    year1 = dato1['Year'] if pd.notna(dato1['Year']) else 0
    year2 = dato2['Year'] if pd.notna(dato2['Year']) else 0
    if year1 != year2:
        return year1 > year2

    # Comparación por afiliaciones
    afiliacion1 = dato1['Affiliations'].split(',')[0].strip().lower() if pd.notna(dato1['Affiliations']) else ''
    afiliacion2 = dato2['Affiliations'].split(',')[0].strip().lower() if pd.notna(dato2['Affiliations']) else ''
    if afiliacion1 != afiliacion2:
        return afiliacion1 > afiliacion2

    # Comparación por título de la fuente
    source_title1 = dato1['Source title'].strip().lower() if pd.notna(dato1['Source title']) else ''
    source_title2 = dato2['Source title'].strip().lower() if pd.notna(dato2['Source title']) else ''
    if source_title1 != source_title2:
        return source_title1 > source_title2

    # Comparación por base de datos
    source1 = dato1['Source'].strip().lower() if pd.notna(dato1['Source']) else ''
    source2 = dato2['Source'].strip().lower() if pd.notna(dato2['Source']) else ''
    if source1 != source2:
        return source1 > source2

    # Comparación por citaciones
    cited_by1 = dato1['Cited by'] if pd.notna(dato1['Cited by']) else 0
    cited_by2 = dato2['Cited by'] if pd.notna(dato2['Cited by']) else 0
    return cited_by1 > cited_by2

def convertir_columnas(df):
    df['Authors'] = df['Authors'].astype(str).fillna('')
    df['Affiliations'] = df['Affiliations'].astype(str).fillna('')
    df['Source title'] = df['Source title'].astype(str).fillna('')
    df['Source'] = df['Source'].astype(str).fillna('')
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce').fillna(0).astype(int)
    df['Cited by'] = pd.to_numeric(df['Cited by'], errors='coerce').fillna(0).astype(int)
    return df



if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'data.csv')
    df = pd.read_csv(file_path, nrows=8509, encoding='utf-8')
    
    df = convertir_columnas(df)
    
    start_time = time.time()
    
    df_sorted = quicksort(df)
    
    end_time = time.time()
    
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")

    # Extraer la dirección donde será guardado el archivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    direccion = os.path.join(base_dir, 'data', 'dataOrdv2.csv')

    # Guardar el archivo limpio en formato CSV
    df_sorted.to_csv(direccion, index=False)
    
