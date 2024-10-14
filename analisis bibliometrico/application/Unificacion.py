import pandas as pd
import os


##variables globales
data_IEEE=None
data_scopus=None

#dataframe unificado 
data=None


#Metodo que carga los datos de la base scopus y unifica las columnas 
def cargarDatosScopus():

    global data_scopus

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'scopus.csv')

    data = pd.read_csv(file_path, nrows=10150, encoding='utf-8',
                       on_bad_lines='skip',
                       encoding_errors='replace')

    #columnas especificas a extraer de la data de scopus
    columnas_deseadas=['Authors', 'Title', 'Year', 'Issue', 'Page start', 'Page end', 'Abstract', 'Affiliations', 'ISBN', 'DOI', 'Link', 'EID', 'Publisher','Cited by','Source','Source title']    

    data_scopus=data[columnas_deseadas]





#Metodo que carga los datos de la base IEEE y unifica las columnas 
def cargarDatosIEEE():

    global data_IEEE

    #extraer direccion del archivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'dataIEEE.csv')

    #leer el archivo
    data = pd.read_csv(file_path, nrows=10150, encoding='utf-8',
                       on_bad_lines='skip',
                       encoding_errors='replace')
    
    #columnas especificas a extraer de la data de IEEE
    columnas_deseadas = ['Authors', 'Document Title', 'Publication Year', 'Issue', 'Start Page', 'End Page', 'Abstract', 'Author Affiliations', 'ISBNs', 'DOI', 'PDF Link', 'Document Identifier', 'Publisher','Article Citation Count','Publication Title']  

    data_IEEE=data[columnas_deseadas]

    data_IEEE['Source'] = 'IEEE Xplore'

    




    
#metodo encargado de renombrar las columnas de la base de IEEE y unificarla a la de scopus
def unificarDatos():

    global data_IEEE,data,data_scopus

    data_IEEE=data_IEEE.rename(columns={
        'Document Title':'Title',
        'Publication Year':'Year',
        'Start Page':'Page start',
        'End Page':'Page end',
        'Author Affiliations':'Affiliations',
        'ISBNs':'ISBN',
        'PDF Link':'Link',
        'Document Identifier':'EID',
        'Article Citation Count':'Cited by',
        'Publication Title':'Source title'
    })

    data = pd.concat([data_IEEE,data_scopus],ignore_index=True)
    
    print(data.iloc[0])
    

# Método encargado de generar el nuevo archivo con todos los datos unificados pero sin repetir
def crearNuevoCsvSinDuplicados():
    
    global data, data_IEEE

    # Eliminar los duplicados basados en la columna 'DOI'
    data = data.drop_duplicates(subset=['DOI'])

    # Rellenar los espacios vacíos (valores NaN) con 'Null'
    data = data.fillna('Null')

    # Extraer la dirección donde será guardado el archivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    direccion = os.path.join(base_dir, 'data', 'data.csv')

    # Guardar el archivo limpio en formato CSV
    data.to_csv(direccion, index=False)






cargarDatosIEEE()
cargarDatosScopus()
unificarDatos()
crearNuevoCsvSinDuplicados()
