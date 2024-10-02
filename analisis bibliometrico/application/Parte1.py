import pandas as pd



#METODO PARA CREAR LA DATA CON LAS COLUMNAS DESEADAS#



# Ruta del archivo original
archivo_original = 'C:/Users/brahi/Documents/Analisis/data/dataIEEE.csv' 

# Cargar el archivo CSV original
df = pd.read_csv(archivo_original)

# Especificar las columnas que deseas extraer
columnas_deseadas = ['Authors', 'Publication Title', 'Publication Year', 'Issue', 'Start Page', 'End Page', 'Abstract', 'Author Affiliations', 'ISBNs', 'DOI', 'PDF Link', 'Document Identifier', 'Publisher']  # Reemplaza con los nombres de las columnas que deseas extraer

# Crear un nuevo DataFrame con solo esas columnas
df_nuevo = df[columnas_deseadas]

# Guardar el nuevo DataFrame en un archivo CSV en la misma carpeta
archivo_nuevo = 'C:/Users/brahi/Documents/Analisis/data/archivo_limpio.csv'
df_nuevo.to_csv(archivo_nuevo, index=False)

print(f"Nuevo archivo CSV guardado en: {archivo_nuevo}")




# METODO PARA UNIFICAR LAS BASES DE DATOS SIN MODIFICAR EL ARCHIVO PRINCIPAL# 



# Cargar los dos archivos CSV
archivo1 = 'C:/Users/brahi/Documents/Analisis/data/scopus.csv'  
archivo2 = 'C:/Users/brahi/Documents/Analisis/data/archivo_limpio.csv'  

df1 = pd.read_csv(archivo1)
df2 = pd.read_csv(archivo2)

# Renombrar las columnas del segundo DataFrame para que coincidan con el primero
df2 = df2.rename(columns={
    'Authors': 'Authors',
    'Publication Title': 'Title',
    'Publication Year': 'Year',
    'Abstract': 'Abstract',
    # Agrega más renombramientos según sea necesario
})

# Concatenar los DataFrames
df_unificado = pd.concat([df1, df2], ignore_index=True)

# Guardar el DataFrame unificado en un nuevo archivo CSV
archivo_unificado = 'C:/Users/brahi/Documents/Analisis/data/archivo_unificado.csv'
df_unificado.to_csv(archivo_unificado, index=False)

print(f"Archivo CSV unificado guardado en: {archivo_unificado}")





#METODO PARA UNIFICAR LA BASE DE DATOS CON LAS MISMAS COLUMNAS EN COMUN#





import pandas as pd

# Cargar los dos archivos CSV
archivo1 = 'C:/Users/brahi/Documents/Analisis/data/archivo1.csv'  
archivo2 = 'C:/Users/brahi/Documents/Analisis/data/archivo2.csv'  

df1 = pd.read_csv(archivo1)
df2 = pd.read_csv(archivo2)

# Unificar las columnas de ambos DataFrames, seleccionando las columnas comunes
columnas_comunes = ['columna1', 'columna2', 'columna3']  

df1_comun = df1[columnas_comunes]
df2_comun = df2[columnas_comunes]

# Concatenar los DataFrames con las mismas columnas
df_unificado = pd.concat([df1_comun, df2_comun], ignore_index=True)

# Guardar el DataFrame unificado en un nuevo archivo CSV
archivo_unificado = 'C:/Users/brahi/Documents/Analisis/data chat/archivo_unificado_mismas_columnas.csv'
df_unificado.to_csv(archivo_unificado, index=False)

print(f"Archivo CSV unificado guardado en: {archivo_unificado}")



#METODO QUE QUITA LOS DUPLICADOS Y PONE NULL A LOS DATOS VACIOS#



import pandas as pd

# Cargar el archivo CSV
archivo = 'C:/Users/brahi/Documents/Analisis/data/archivo.csv' 
df = pd.read_csv(archivo)

# 1. Eliminar duplicados (filas completamente idénticas)
df_sin_duplicados = df.drop_duplicates()

# 2. Rellenar los espacios vacíos (valores NaN) con un valor por defecto
valor_relleno = 'Null'  
df_limpio = df_sin_duplicados.fillna(valor_relleno)

# Guardar el archivo limpio en un nuevo CSV
archivo_limpio = 'C:/Users/brahi/Documents/Analisis/data/archivo_limpio_sin_duplicados_y_relleno.csv'
df_limpio.to_csv(archivo_limpio, index=False)

print(f"Archivo CSV limpio guardado en: {archivo_limpio}")


  









