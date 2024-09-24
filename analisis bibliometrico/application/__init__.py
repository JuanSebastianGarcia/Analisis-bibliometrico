##Leer archivo: Abre y carga los datos.
import os

##variables globales
contenido_sciencedirect=""
contenido_scopus=""

bibliografias_scopus=[]
bibliografias_sciencedirect=[]

#Metodo que carga los datos de las rutas 
def cargarDatos():

    global contenido_sciencedirect
    global contenido_scopus
    # Obtener la ruta absoluta del directorio donde se encuentra este script (_init_.py)
    ruta_base = os.path.dirname(os.path.abspath(__file__))


    # Definir las rutas relativas de los archivos en función de la ubicación de este script
    ruta_sciencedirect = os.path.join(ruta_base, 'data', 'ScienceDirect.txt')
    ruta_scopus = os.path.join(ruta_base, 'data', 'scopus.txt')

    # Leer y mostrar el contenido de cada archivo
    contenido_sciencedirect = leer_archivo(ruta_sciencedirect)
    contenido_scopus = leer_archivo(ruta_scopus)



# Función para leer y mostrar el contenido de los archivos con manejo de errores
def leer_archivo(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
        return contenido
    except FileNotFoundError:
            return f"Error: El archivo {ruta} no se encontró."
    except Exception as e:
        return f"Error: {str(e)}"



##Dividir en bloques: Separa los datos en cada bloque bibliográfico
def construirArreglos():
     
    construirArregloScopus()
    construirArregloScienceDirect()

    


#Metodo encargado de almacenar cada bibliografia por separado en un arreglo
def construirArregloScopus():
    # Inicializa el contenido temporal y el arreglo final
    contenido = ""
    global bibliografias_scopus

    # Recorrer línea por línea el contenido de Scopus
    for i, linea in enumerate(contenido_scopus.splitlines(), start=1):
        # Agregar la línea al contenido temporal
        contenido += linea + "\n"
        
        # Verificar si la línea contiene 'SOURCE: Scopus'
        if "SOURCE: Scopus" in linea:
            # Almacenar el contenido acumulado en el arreglo
            bibliografias_scopus.append(contenido.strip())

            # Vaciar el contenido temporal
            contenido = ""
        

def construirArregloScienceDirect():
    # Inicializa el contenido temporal y el arreglo final
    contenido = ""
    global bibliografias_sciencedirect

    # Recorrer línea por línea el contenido de ScienceDirect
    for i, linea in enumerate(contenido_sciencedirect.splitlines(), start=1):
        # Si la línea está vacía (doble salto de línea indica fin de una bibliografía)
        if linea.strip() == "":

            bibliografias_sciencedirect.append(contenido.strip())
            # Vaciar el contenido temporal
            contenido = ""

        else:
            # Si la línea no está vacía, agregarla al contenido temporal
            contenido += linea + "\n"



##Identificar estructura: Determina el formato de cada bloque.
##Procesar bloque: Reconstruye cada bloque en la estructura estándar.
##Guardar resultado: Escribe el resultado en un archivo final.



cargarDatos()
construirArreglos()

print(bibliografias_scopus)