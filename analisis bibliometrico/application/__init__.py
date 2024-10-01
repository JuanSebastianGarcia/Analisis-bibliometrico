import pandas as pd
import os


##variables globales
data_sciencedirect=""
data_scopus=[]

bibliografias_scopus=[]
bibliografias_sciencedirect=[]

bibliografia_universal=[]


#Metodo que carga los datos de las rutas 
def cargarDatosScopus():

    global data_scopus

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'scopus.csv')

    data_scopus = pd.read_csv(file_path, nrows=10150, encoding='utf-8',
                       on_bad_lines='skip',
                       encoding_errors='replace')
    
    print(data_scopus.iloc[0])
    

    



cargarDatosScopus()

