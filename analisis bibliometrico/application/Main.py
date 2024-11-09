"""
    En esta clase el objetivo es poder orquestar las funcionalidades del proyecto en orden,
    con el fin de ver un flujo de proceso limpio y uno detras de otro para garantizar su 
    funcionalidad

    orden de ejecucion

"""
import tkinter as tk
from tkinter import messagebox
from Frecuencia import Frecuencia
from estadisticas import analizarAutores
from estadisticas import analizarFecha 
from estadisticas import contar_tipos_producto 
from estadisticas import analizarInstituciones
from estadisticas import analizarJournal 
from estadisticas import analizarPublisher 
from estadisticas import analizarBaseDatos 
from estadisticas import analizarArticuloMasCitado
from estadisticas import analizar_database_autor
from estadisticas import analizar_journal_articulo
from estadisticas import analizar_autores_journal
from estadisticas import analizar_journal_articulo_pais

class InterfazFrecuencia:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesamiento de Frecuencia de Palabras")
        self.root.geometry("700x800")

        # Crear los frames para organizar los botones
        frame_izquierda = tk.Frame(root)
        frame_izquierda.pack(side="left", padx=20, pady=20)

        frame_centro = tk.Frame(root)
        frame_centro.pack(side="left", padx=20, pady=20)

        # Elementos en frame izquierda

        # Etiqueta de descripción y botón para la nube de palabras
        self.label = tk.Label(frame_izquierda, text="Presiona el botón para generar la nube de palabras")
        self.label.pack(pady=10)

        self.procesar_button = tk.Button(frame_izquierda, text="Generar Nube de Palabras", command=self.iniciar_procesamiento)
        self.procesar_button.pack(pady=10)

        # Entrada y botón para analizar autores por año
        self.label_autor = tk.Label(frame_izquierda, text="Introduce el año para analizar autores:")
        self.label_autor.pack(pady=10)

        self.autor_entry = tk.Entry(frame_izquierda)
        self.autor_entry.pack(pady=5)

        self.analizar_button = tk.Button(frame_izquierda, text="Analizar Autores", command=self.analizar_autores)
        self.analizar_button.pack(pady=10)

        # Botón para analizar fechas
        self.procesar_button = tk.Button(frame_izquierda, text="Analizar Fechas", command=self.iniciar_analizarFecha)
        self.procesar_button.pack(pady=10)

        # Botón para contar tipo de producto
        self.procesar_button = tk.Button(frame_izquierda, text="Contar Tipo de Producto", command=self.iniciar_contar_tipo_producto)
        self.procesar_button.pack(pady=10)

        # Entrada y botón para analizar instituciones por año
        self.label_instituciones = tk.Label(frame_izquierda, text="Introduce el año para analizar instituciones:")
        self.label_instituciones.pack(pady=10)

        self.instituciones_entry = tk.Entry(frame_izquierda)
        self.instituciones_entry.pack(pady=5)

        self.instituciones_button = tk.Button(frame_izquierda, text="Analizar Instituciones", command=self.iniciar_analizar_instituciones)
        self.instituciones_button.pack(pady=10)

        # Entrada y botón para analizar Journal por año
        self.label_journal = tk.Label(frame_izquierda, text="Introduce el año para analizar journal:")
        self.label_journal.pack(pady=10)

        self.journal_entry = tk.Entry(frame_izquierda)
        self.journal_entry.pack(pady=5)

        self.journal_button = tk.Button(frame_izquierda, text="Analizar Journal", command=self.iniciar_analizar_journal)
        self.journal_button.pack(pady=10)

        # Entrada y botón para analizar Publisher por año
        self.label_publisher = tk.Label(frame_izquierda, text="Introduce el año para analizar el publisher:")
        self.label_publisher.pack(pady=10)

        self.publisher_entry = tk.Entry(frame_izquierda)
        self.publisher_entry.pack(pady=5)

        self.publisher_button = tk.Button(frame_izquierda, text="Analizar Publisher", command=self.iniciar_analizar_publiser)
        self.publisher_button.pack(pady=10)

        # Elementos en frame centro

        # Entrada y botón para analizar base de datos por año
        self.label_base_datos = tk.Label(frame_centro, text="Introduce el año para analizar la base de datos:")
        self.label_base_datos.pack(pady=10)

        self.base_datos_entry = tk.Entry(frame_centro)
        self.base_datos_entry.pack(pady=5)

        self.base_datos_button = tk.Button(frame_centro, text="Analizar Base de Datos", command=self.iniciar_analizar_base_de_datos)
        self.base_datos_button.pack(pady=10)

        # Entrada y botón para analizar el artículo más citado
        self.label_articulo = tk.Label(frame_centro, text="Introduce el año para analizar el artículo más citado:")
        self.label_articulo.pack(pady=10)

        self.articulo_entry = tk.Entry(frame_centro)
        self.articulo_entry.pack(pady=5)

        self.articulo_button = tk.Button(frame_centro, text="Analizar Artículo Más Citado", command=self.iniciar_analizar_ArticuloMasCitado)
        self.articulo_button.pack(pady=10)

        # Botón para analizar autores por base de datos
        self.database_autor_button = tk.Button(frame_centro, text="Analizar Database Autor", command=self.iniciar_database_autor)
        self.database_autor_button.pack(pady=10)

        # Botón para analizar los tres mejores journals
        self.journal_articulo_button = tk.Button(frame_centro, text="Analizar 3 Mejores Journal", command=self.iniciar_journal_articulo)
        self.journal_articulo_button.pack(pady=10)

        # Entrada y botón para analizar autores según la cantidad de journals
        self.label_cantidad_journal = tk.Label(frame_centro, text="Introduce la cantidad de journals para analizar el autor:")
        self.label_cantidad_journal.pack(pady=10)

        self.cantidad_journal_entry = tk.Entry(frame_centro)
        self.cantidad_journal_entry.pack(pady=5)

        self.analizar_autores_journal_button = tk.Button(frame_centro, text="Analizar Autores según Cantidad de Journals", command=self.iniciar_analizar_autores_journal)
        self.analizar_autores_journal_button.pack(pady=10)

        # Botón para ArticuloJournalPorPais
        self.journal_pais_button = tk.Button(frame_centro, text="Articulo Journal Por País", command=self.iniciar_journal_articulo_pais)
        self.journal_pais_button.pack(pady=10)

    def iniciar_procesamiento(self):
        try:
            frecuencia = Frecuencia()
            frecuencia.iniciar_ejecucion()
            messagebox.showinfo("Éxito", "Procesamiento completado. Nube de palabras generada.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el procesamiento: {e}")

    def analizar_autores(self):
        try:
            # Obtener el año ingresado
            year = int(self.autor_entry.get())
            # Instancia de Estadisticas y ejecución de analizarAutores
            analizarAutores(year)
            messagebox.showinfo("Éxito", f"Análisis de autores completado para el año {year}.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un año válido en formato numérico.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el análisis de autores: {e}")

    def iniciar_analizarFecha(self):
        try:
            analizarFecha()
            messagebox.showinfo("Éxito", "Procesamiento completado.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el procesamiento: {e}")


    def iniciar_contar_tipo_producto(self):
        try:
            contar_tipos_producto()
            messagebox.showinfo("Éxito", "Procesamiento completado.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el procesamiento: {e}")


    def iniciar_analizar_instituciones(self):
        try:
            # Obtener el año ingresado
            year = int(self.instituciones_entry.get())
            # Instancia de Estadisticas y ejecución de analizarAutores
            analizarInstituciones(year)
            messagebox.showinfo("Éxito", f"Análisis de autores completado para el año {year}.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un año válido en formato numérico.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el análisis de autores: {e}")

    def iniciar_analizar_journal(self):
        try:
            # Obtener el año ingresado
            year = int(self.journal_entry.get())
            # Instancia de Estadisticas y ejecución de analizarAutores
            analizarJournal(year)
            messagebox.showinfo("Éxito", f"Análisis de Journal para el año {year}.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un año válido en formato numérico.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el análisis de autores: {e}")


    def iniciar_analizar_publiser(self):
        try:
            # Obtener el año ingresado
            year = int(self.publisher_entry.get())
            # Instancia de Estadisticas y ejecución de analizarAutores
            analizarPublisher(year)
            messagebox.showinfo("Éxito", f"Análisis de Publisher para el año {year}.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un año válido en formato numérico.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el análisis de autores: {e}")


    def iniciar_analizar_base_de_datos(self):
        try:
            # Obtener el año ingresado
            year = int(self.base_datos_entry.get())
            # Instancia de Estadisticas y ejecución de analizarAutores
            analizarBaseDatos(year)
            messagebox.showinfo("Éxito", f"Análisis de base de datos para el año {year}.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un año válido en formato numérico.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el análisis de autores: {e}")

    def iniciar_analizar_ArticuloMasCitado(self):
        try:
            # Obtener el año ingresado
            year = int(self.articulo_entry.get())
            # Instancia de Estadisticas y ejecución de analizarAutores
            analizarArticuloMasCitado(year)
            messagebox.showinfo("Éxito", f"Análisis de Articulo mas citado para el año {year}.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un año válido en formato numérico.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el análisis de autores: {e}")

    def iniciar_database_autor(self):
        try:
            analizar_database_autor()
            messagebox.showinfo("Éxito", "Procesamiento completado.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el procesamiento: {e}")

    def iniciar_journal_articulo(self):
        try:
            analizar_journal_articulo()
            messagebox.showinfo("Éxito", "Procesamiento completado.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el procesamiento: {e}")

    def iniciar_analizar_autores_journal(self):
        try:
            # Obtener el año ingresado
            cantidadJournal = int(self.cantidad_journal_entry.get())
            # Instancia de Estadisticas y ejecución de analizarAutores
            analizar_autores_journal(cantidadJournal)
            messagebox.showinfo("Éxito", f"Análisis de Articulo mas citado para el año {cantidadJournal}.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un año válido en formato numérico.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el análisis de autores: {e}")


    def iniciar_journal_articulo_pais(self):
        try:
            analizar_journal_articulo_pais()
            messagebox.showinfo("Éxito", "Procesamiento completado.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el procesamiento: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazFrecuencia(root)
    root.mainloop()

