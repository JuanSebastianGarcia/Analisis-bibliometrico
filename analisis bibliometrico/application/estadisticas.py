"""
Lista de las variables que hay que procesar 

    Primer autor del producto
    Año de publicación
    Tipo de producto (artículos, conferencias, capítulos de libro)
    Afiliación del primer autor
    Journal
    Publisher
    Base de datos
    Cantidad de citaciones por artículo

    cada variable tendra su forma de ser procesada
"""
#IMPORTS
import os
import pandas as pd
import matplotlib.pyplot as plt


#VARIABLES GLOBALES
data = None #contiene los datos ordenados

#hacer conteno de autores
def analizarAutores():

    """
        Se extrae el primer autor de cada producto y se hace un contedo de las veces 
        que aparece cada autor

    """
    global data

    #extraer el primer autor    
    autores = data['Authors'].apply(lambda x: x.split(';')[0].strip().split(',')[0])

    counting_autores={}

    #hacer un conteo de los autores
    for autor in autores:
        if autor in counting_autores:
            counting_autores[autor]+=1
        else:
            counting_autores[autor]=1

    imprimirGraficaAutores(counting_autores)


#Genera una grafica que muestra los autores
def imprimirGraficaAutores(counting_autores):
    """
        Deacuerdo al conteo de los autores hecho previamente, se imprimira una grafica de barras con los 
        15 autores mas nombrados
    """

    # Filtrar autores con más de 5 ocurrencias
    top_autores = sorted(counting_autores.items(), key=lambda x:x[1] , reverse=True)[:15]

    #se extraen los datos para la grafica
    keys = [autor for autor,_ in top_autores ]
    values = [conteo for _,conteo in top_autores]

    plt.bar(keys,values)

    # Añadir etiquetas
    plt.xlabel('Autores')
    plt.ylabel('Número de publicaciones')
    plt.title('Conteo de autores (más de 5 publicaciones)')

    # Mostrar el gráfico
    plt.xticks(rotation=90)  # Rotar etiquetas si son largas
    plt.show()


#carga lso datos del csv a la variable data
def cargarDatos():

    """
        Se lee el archivo csv con la data y se almacena en una variable
    """
    global data

    #extraer direccion del archivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'dataOrd.csv')

    #leer el archivo
    data = pd.read_csv(file_path, nrows=10150, encoding='utf-8',
                       on_bad_lines='skip',
                       encoding_errors='replace')


#estandariza el tipo de dato de cada columna 
def estandarizarTiposDatos():
    """
        Para evitar errores en la lectura de los datos y confundir tipos, se estandarizan los 
        tipos de datos desde el inicio
    """
    global data

    data['Authors'] = data['Authors'].astype(str).fillna('')


#hacer un conteo de los años de la publicacion de cada articulo
def contarAniosPublicacion():
    """
        realizar un conteo de los años de publicacion de cada articulo
    """

    global data #variable de datos

    years_couting={} #diccionario de años

    #conteo de años
    for year in data['Year']:
        if year in years_couting:
            years_couting[year]+=1
        else:
            years_couting[year]=1

    showYears(years_couting)




def showYears(years_couting:dict):
    """
        Mostrar el conteo de datos de cada año
    """

    #se extraen los datos para la grafica
    keys =list( years_couting.keys())
    values = list(years_couting.values())

    plt.bar(keys,values)

    # Añadir etiquetas
    plt.xlabel('años')
    plt.ylabel('numero de publicaciones por año')
    plt.title('publicacion de articulos en los años')

    # Mostrar el gráfico
    plt.xticks(rotation=90)  # Rotar etiquetas si son largas
    plt.show()




if __name__ =='__main__':

    #preparacion
    cargarDatos()
    estandarizarTiposDatos()

    #estadistica a autores
    #analizarAutores()

    #estadistica a los años
    contarAniosPublicacion()