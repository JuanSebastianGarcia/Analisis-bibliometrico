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
data = None 

def analizarAutores():

    """
        Se extrae el primer autor de cada producto y se hace un contedo de ellos
        para poder mostrar un resultado

    """
    global data

    #extraer el primer autor    
    autores = data['Authors'].apply(lambda x: x.split(',')[0].split(';')[0].strip())

    counting_autores={}

    #hacer un conteo de los autores
    for autor in autores:
        if autor in counting_autores:
            counting_autores[autor]+=1
        else:
            counting_autores[autor]=1

    imprimirGraficaautores(counting_autores)


def imprimirGraficaautores(counting_autores):
    """
        Deacuerdo al conteo de los autores hecho previamente, se imprimira una grafica de barras con los autores que tengan 
        mas de 5 apariciones
    """

    # Filtrar autores con más de 5 ocurrencias
    autores_filtrados = {autor: conteo for autor, conteo in counting_autores.items() if conteo >= 5}

    keys = autores_filtrados.keys()
    values = autores_filtrados.values()

    plt.bar(keys,values)

    # Añadir etiquetas
    plt.xlabel('Autores')
    plt.ylabel('Número de publicaciones')
    plt.title('Conteo de autores (más de 5 publicaciones)')

    # Mostrar el gráfico
    plt.xticks(rotation=90)  # Rotar etiquetas si son largas
    plt.show()



    


def cargarDatos():

    """
        Se lee el archivo csv con la data y se almacena en una variable
    """
    global data

    #extraer direccion del archivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'dataIEEE.csv')

    #leer el archivo
    data = pd.read_csv(file_path, nrows=10150, encoding='utf-8',
                       on_bad_lines='skip',
                       encoding_errors='replace')
    

def estandarizarTiposDatos():
    """
        Para evitar errores en la lectura de los datos y confundir tipos, se estandarizan los 
        tipos de datos desde el inicio
    """
    global data

    data['Authors'] = data['Authors'].astype(str).fillna('')


cargarDatos()
estandarizarTiposDatos()
analizarAutores()