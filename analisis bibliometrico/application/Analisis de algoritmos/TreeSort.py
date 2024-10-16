import time
import random
import sys
sys.setrecursionlimit(2000)  # Aumentar el límite de recursión

# Definición del nodo del árbol
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


# Insertar un nuevo nodo en el árbol
def insertar_nodo(raiz, dato):
    if raiz is None:
        return Nodo(dato)
    
    # Insertar en el subárbol izquierdo
    if dato < raiz.dato:
        raiz.izquierda = insertar_nodo(raiz.izquierda, dato)
    else:
        # Insertar en el subárbol derecho
        raiz.derecha = insertar_nodo(raiz.derecha, dato)
    
    return raiz



# Recorrido inorden del árbol
def recorrido_inorden(raiz, resultado):
    if raiz is not None:
        recorrido_inorden(raiz.izquierda, resultado)
        resultado.append(raiz.dato)
        recorrido_inorden(raiz.derecha, resultado)



# Algoritmo Tree Sort
def tree_sort(arr):
      
    raiz = None

    # Insertar los elementos en el árbol
    for dato in arr:
        raiz = insertar_nodo(raiz, dato)
    
    # Recorrer el árbol en inorden para obtener los elementos ordenados
    resultado = []
    recorrido_inorden(raiz, resultado)
    return resultado





# Ejemplo de uso
if __name__ == "__main__":

    # Generar un arreglo de 10,000 números aleatorios
    array = [random.randint(0, 100) for _ in range(100)]
      

    # Marca el tiempo inicial
    start_time = time.time()

    # Ordena la lista usando Timsort
    tree_sort(array)


    # Marca el tiempo final
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")

