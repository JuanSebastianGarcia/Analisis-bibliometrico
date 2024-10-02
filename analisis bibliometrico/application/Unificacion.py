import pandas as pd
import os


##variables globales
data_IEEE=[]
data_scopus=[]

#dataframe unificado 
datra=[]


#Metodo que carga los datos de la base scopus y unifica las columnas 
def cargarDatosScopus():

    global data_scopus

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'scopus.csv')

    data = pd.read_csv(file_path, nrows=10150, encoding='utf-8',
                       on_bad_lines='skip',
                       encoding_errors='replace')

    columnas_deseadas=['Authors', 'Title', 'Year', 'Issue', 'Page start', 'Page end', 'Abstract', 'Affiliations', 'ISBN', 'DOI', 'Link', 'EID', 'Publisher']    

    data_scopus=data[columnas_deseadas]


#Metodo que carga los datos de la base IEEE y unifica las columnas 
def cargarDatosIEEE():

    global data_IEEE

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'dataIEEE.csv')

    data = pd.read_csv(file_path, nrows=10150, encoding='utf-8',
                       on_bad_lines='skip',
                       encoding_errors='replace')
    
    columnas_deseadas = ['Authors', 'Publication Title', 'Publication Year', 'Issue', 'Start Page', 'End Page', 'Abstract', 'Author Affiliations', 'ISBNs', 'DOI', 'PDF Link', 'Document Identifier', 'Publisher']  # Reemplaza con los nombres de las columnas que deseas extraer

    data_IEEE=data[columnas_deseadas]
    
    

    





