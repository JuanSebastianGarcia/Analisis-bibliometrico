import pandas as pd
import os


##variables globales
data_IEEE=None
data_scopus=None
data_scientdirect = None
data_unificado1= None
#dataframe unificado 
data=None
data2= None


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




def cargarDatosdata():
    global data_unificado1

    # Ruta del archivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'data.csv')

    # Leer el archivo con las primeras 10150 filas
    data = pd.read_csv(file_path, nrows=10000, encoding='utf-8', 
                       on_bad_lines='skip', 
                       encoding_errors='replace')   
    #columnas especificas a extraer de la data de scopus
    columnas_deseadas=['Authors', 'Title', 'Year', 'Issue', 'Page start', 'Page end', 'Abstract', 'Affiliations', 'ISBN', 'DOI', 'Link', 'EID', 'Publisher','Cited by','Source','Source title']    

    data_unificado1=data[columnas_deseadas]


def cargarDatosScientDirect():
    global data_scientdirect

    # Ruta del archivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'ScientDirect.csv')

    # Leer el archivo con las primeras 10150 filas
    data = pd.read_csv(file_path, nrows=2000, encoding='utf-8', 
                       on_bad_lines='skip', 
                       encoding_errors='replace')   
    #columnas especificas a extraer de la data de scopus
    columnas_deseadas=['author', 'title', 'year', 'abstract', 'isbn', 'doi', 'url' ]    

    data_scientdirect=data[columnas_deseadas]


    
#metodo encargado de renombrar las columnas de la base de IEEE y unificarla a la de scopus
def unificarDatos():

    global data_IEEE,data,data_scopus,data_scientdirect,data2,data_unificado1

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

    data_scientdirect=data_scientdirect.rename(columns={
        'author': 'Authors',
        'title': 'Title',
        'year': 'Year',
        'abstract': 'Abstract',
        'isbn': 'ISBN',
        'doi': 'DOI',
        'url': 'Link'
    })

    data2 = pd.concat([data_scientdirect,data_unificado1],ignore_index=True)
    
    print(data2.iloc[0])
    

# Método encargado de generar el nuevo archivo con todos los datos unificados pero sin repetir
def crearNuevoCsvSinDuplicados():
    
    global data, data_IEEE,data2, data_scientdirect

    # Eliminar los duplicados basados en la columna 'DOI'
    data = data.drop_duplicates(subset=['DOI'])

    # Rellenar los espacios vacíos (valores NaN) con 'Null'
    data = data.fillna('Null')

    # Extraer la dirección donde será guardado el archivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    direccion = os.path.join(base_dir, 'data', 'data.csv')

    # Guardar el archivo limpio en formato CSV
    data.to_csv(direccion, index=False)


    # Eliminar los duplicados basados en la columna 'DOI'
    data2 = data2.drop_duplicates(subset=['DOI'])

    # Rellenar los espacios vacíos (valores NaN) con 'Null'
    data2 = data2.fillna('Null')

    # Reemplazar los valores 'Null' en la columna 'Source' con la palabra especificada
    data2['Source'] = data2['Source'].replace('Null', "ScientDirect")

    # Extraer la dirección donde será guardado el archivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    direccion = os.path.join(base_dir, 'data', 'data.csv')
    direccion = os.path.join(base_dir, 'data', 'data.csv')

    # Guardar el archivo limpio en formato CSV
    data2.to_csv(direccion, index=False)


cargarDatosIEEE()
cargarDatosScopus()
cargarDatosdata()
cargarDatosScientDirect()
unificarDatos()
crearNuevoCsvSinDuplicados()

