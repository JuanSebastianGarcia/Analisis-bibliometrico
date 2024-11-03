import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, 'data', 'Palabras_especiales.csv')

#cargar archivo
data = pd.read_csv(file_path,nrows=500,encoding='utf-8',
                       on_bad_lines='skip',
                       encoding_errors='replace')

#recorrer registro por registro
data['Sinonimos'] = data['Palabra'].apply(lambda x: str(x).split(' - ')[1:] if ' - ' in str(x) else [])
data['Palabra'] = data['Palabra'].apply(lambda x: str(x).split(' - ')[0])

#extraer los sinonimos de la columna palabra y colocarlos en una nueva columna
data.to_csv(file_path,index=False)