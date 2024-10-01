import pandas as pd


##variables globales
data_sciencedirect=""
data_scopus=[]

bibliografias_scopus=[]
bibliografias_sciencedirect=[]

bibliografia_universal=[]


#Metodo que carga los datos de las rutas 
def cargarDatos():
    global data_scopus
    data_scopus = pd.read_csv('../data/scopus.csv', nrows=10150, encoding='utf-8',
                       on_bad_lines='skip',
                       encoding_errors='replace')



cargarDatos()

