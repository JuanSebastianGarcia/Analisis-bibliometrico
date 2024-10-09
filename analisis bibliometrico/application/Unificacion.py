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
    columnas_deseadas=['Authors', 'Title', 'Year', 'Issue', 'Page start', 'Page end', 'Abstract', 'Affiliations', 'ISBN', 'DOI', 'Link', 'EID', 'Publisher','Cited by','Source']    

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
    columnas_deseadas = ['Authors', 'Publication Title', 'Publication Year', 'Issue', 'Start Page', 'End Page', 'Abstract', 'Author Affiliations', 'ISBNs', 'DOI', 'PDF Link', 'Document Identifier', 'Publisher','Article Citation Count']  

    data_IEEE=data[columnas_deseadas]
    
    data_IEEE['Database'] = 'IEEE Xplore'

    




    
#metodo encargado de renombrar las columnas de la base de IEEE y unificarla a la de scopus
def unificarDatos():

    global data_IEEE,data,data_scopus

    data_IEEE=data_IEEE.rename(columns={
        'Publication Title':'Title',
        'Publication Year':'Year',
        'Start Page':'Page start',
        'End Page':'Page end',
        'Author Affiliations':'Affiliations',
        'ISBNs':'ISBN',
        'PDF Link':'Link',
        'Document Identifier':'EID'

    })

    data = pd.concat([data_IEEE,data_scopus],ignore_index=True)

    print(data.iloc[0])
    


#Metodo encargado de generar el nuevo archivo con todos los datos unificados pero sin repetir
def crearNuevoCsvSinDuplicados():
    
    global data,data_IEEE

    #se eliminan los duplicados de la data
    data=data.drop_duplicates(subset=['DOI'])

    #extraer la direccion donde sera guardado el archivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    direccion = os.path.join(base_dir, 'data', 'data.csv')

    data.to_csv(direccion,index=False)







cargarDatosIEEE()
cargarDatosScopus()
unificarDatos()
crearNuevoCsvSinDuplicados()
