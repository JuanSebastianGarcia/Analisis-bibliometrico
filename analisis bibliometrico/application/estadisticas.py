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


#VARIABLES GLOBALES
data = None 

def AnalizarAutores():

    """
        Se extrae el primer autor de cada producto y se hace un contedo de ellos
        para poder mostrar un resultado

    """
    #extraer lista de autores
    print()
    


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