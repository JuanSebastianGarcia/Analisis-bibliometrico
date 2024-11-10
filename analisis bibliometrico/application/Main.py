"""
    En esta clase el objetivo es poder orquestar las funcionalidades del proyecto en orden,
    con el fin de ver un flujo de proceso limpio y uno detras de otro para garantizar su 
    funcionalidad

    orden de ejecucion

"""
import tkinter as tk
from tkinter import messagebox
from Frecuencia import Frecuencia
from estadisticas import Estadisticas


class InterfazFrecuencia:  
    estadistica = Estadisticas()
    def __init__(self, root):
        self.root = root
        self.root.title("Procesamiento de Frecuencia de Palabras")
        self.root.geometry("500x800")

        # Crear los frames para organizar los botones
        frame_izquierda = tk.Frame(root)
        frame_izquierda.pack(side="left", padx=20, pady=20)

        frame_centro = tk.Frame(root)
        frame_centro.pack(side="left", padx=20, pady=20)


        def abrir_nueva_pantalla_para_autores():
            nueva_ventana = tk.Toplevel(self.root)
            nueva_ventana.title("Analizar Autores")
            nueva_ventana.geometry("400x200")
            
            tk.Label(nueva_ventana, text="Introduce el año para analizar autores:").pack(pady=10)
            
            # Campo de entrada en la nueva ventana
            self.autor_entry = tk.Entry(nueva_ventana)
            self.autor_entry.pack(pady=5)
            
            # Botón que ejecuta self.analizar_autores
            tk.Button(nueva_ventana, text="Aceptar", command=self.analizar_autores).pack(pady=10)
        

        #Nueva ventana para las instituciones
        def abrir_nueva_pantalla_para_instituciones():
            nueva_ventana = tk.Toplevel(self.root)
            nueva_ventana.title("Analizar Instituciones")
            nueva_ventana.geometry("400x200")
            
            tk.Label(nueva_ventana, text="Introduce el año para analizar Instituciones:").pack(pady=10)
            
            # Campo de entrada en la nueva ventana
            self.instituciones_entry = tk.Entry(nueva_ventana)
            self.instituciones_entry.pack(pady=5)
            
            # Botón que ejecuta self.analizar_autores
            tk.Button(nueva_ventana, text="Aceptar", command=self.iniciar_analizar_instituciones).pack(pady=10)


        #Nueva ventana para las Journal
        def abrir_nueva_pantalla_para_journal():
            nueva_ventana = tk.Toplevel(self.root)
            nueva_ventana.title("Analizar Journal")
            nueva_ventana.geometry("400x200")
            
            tk.Label(nueva_ventana, text="Introduce el año para analizar Journal:").pack(pady=10)
            
            # Campo de entrada en la nueva ventana
            self.journal_entry = tk.Entry(nueva_ventana)
            self.journal_entry.pack(pady=5)
            
            # Botón que ejecuta self.analizar_autores
            tk.Button(nueva_ventana, text="Aceptar", command=self.iniciar_analizar_journal).pack(pady=10)

        #Nueva ventana para las Journal
        def abrir_nueva_pantalla_para_publisher():
            nueva_ventana = tk.Toplevel(self.root)
            nueva_ventana.title("Analizar Publisher")
            nueva_ventana.geometry("400x200")
            
            tk.Label(nueva_ventana, text="Introduce el año para analizar Publisher:").pack(pady=10)
            
            # Campo de entrada en la nueva ventana
            self.publisher_entry = tk.Entry(nueva_ventana)
            self.publisher_entry.pack(pady=5)
            
            # Botón que ejecuta self.analizar_autores
            tk.Button(nueva_ventana, text="Aceptar", command=self.iniciar_analizar_publiser).pack(pady=10)


        #Nueva ventana para las Journal
        def abrir_nueva_pantalla_para_baseDeDatos():
            nueva_ventana = tk.Toplevel(self.root)
            nueva_ventana.title("Analizar Base de datos")
            nueva_ventana.geometry("400x200")
            
            tk.Label(nueva_ventana, text="Introduce el año para analizar la base de datos:").pack(pady=10)
            
            # Campo de entrada en la nueva ventana
            self.base_datos_entry = tk.Entry(nueva_ventana)
            self.base_datos_entry.pack(pady=5)
            
            # Botón que ejecuta self.analizar_autores
            tk.Button(nueva_ventana, text="Aceptar", command=self.iniciar_analizar_base_de_datos).pack(pady=10)

        #Nueva ventana para las Journal
        def abrir_nueva_pantalla_para_articuloMasCitado():
            nueva_ventana = tk.Toplevel(self.root)
            nueva_ventana.title("Analizar Articulo mas citado")
            nueva_ventana.geometry("400x200")
            
            tk.Label(nueva_ventana, text="Introduce el año para analizar el articulo mas citado:").pack(pady=10)
            
            # Campo de entrada en la nueva ventana
            self.articulo_entry = tk.Entry(nueva_ventana)
            self.articulo_entry.pack(pady=5)
            
            # Botón que ejecuta self.analizar_autores
            tk.Button(nueva_ventana, text="Aceptar", command=self.iniciar_analizar_ArticuloMasCitado).pack(pady=10)


        #Nueva ventana para las Journal
        def abrir_nueva_pantalla_para_journalAutor():
            nueva_ventana = tk.Toplevel(self.root)
            nueva_ventana.title("Analizar Autores por cantidad de journal")
            nueva_ventana.geometry("400x200")
            
            tk.Label(nueva_ventana, text="Introduce la cantidad de journal para analizar el autor:").pack(pady=10)
            
            # Campo de entrada en la nueva ventana
            self.cantidad_journal_entry = tk.Entry(nueva_ventana)
            self.cantidad_journal_entry.pack(pady=5)
            
            # Botón que ejecuta self.analizar_autores
            tk.Button(nueva_ventana, text="Aceptar", command=self.iniciar_analizar_autores_journal).pack(pady=10)



        def abrir_nueva_pantalla_para_analizarGrafo():
            nueva_ventana = tk.Toplevel(self.root)
            nueva_ventana.title("Analizar Autores por cantidad de journal y articulos mas citados")
            nueva_ventana.geometry("400x200")
            
            tk.Label(nueva_ventana, text="Introduce la cantidad de journal para analizar el autor:").pack(pady=10)
            
            # Campo de entrada en la nueva ventana
            self.cantidad_journal_entry_pais = tk.Entry(nueva_ventana)
            self.cantidad_journal_entry_pais.pack(pady=5)

            tk.Label(nueva_ventana, text="Introduce la cantidad de atriculos:").pack(pady=10)
            
            # Campo de entrada en la nueva ventana
            self.cantidad_articulo_entry = tk.Entry(nueva_ventana)
            self.cantidad_articulo_entry.pack(pady=5)
            
            # Botón que ejecuta self.analizar_autores
            tk.Button(nueva_ventana, text="Aceptar", command=self.iniciar_journal_articulo_pais).pack(pady=10)


        self.procesar_button = tk.Button(
        frame_centro, 
        text="Generar Nube de Palabras", 
        command=self.iniciar_procesamiento,
        font=("Arial", 10, "bold"),  # Tipo y tamaño de fuente
        bg="#4DA6FF",  # Color de fondo (verde)
        fg="white",    # Color del texto (blanco)
        relief="raised",  # Tipo de borde
        bd=3,  # Grosor del borde
        padx=8,  # Espaciado horizontal
        pady=4    # Espaciado vertical
)
        self.procesar_button.pack(pady=10)
        # Etiqueta de descripción y botón para la nube de palabras
        self.label = tk.Label(frame_centro, text="Presiona el botón que desee para ver la estadistica interesada", font=("Arial", 10))
        self.label.pack(pady=10)


        # Botón para analizar autores por año
        self.analizar_button = tk.Button(frame_centro, text="Analizar Autores", 
                                         command=lambda: abrir_nueva_pantalla_para_autores())
        self.analizar_button.pack(pady=10)

        # Botón para analizar fechas
        self.procesar_button = tk.Button(frame_centro, text="Analizar Fechas", command=self.iniciar_analizarFecha)
        self.procesar_button.pack(pady=10)

        # Botón para contar tipo de producto
        self.procesar_button = tk.Button(frame_centro, text="Contar Tipo de Producto", command=self.iniciar_contar_tipo_producto)
        self.procesar_button.pack(pady=10)

        #Botón para analizar instituciones
        self.instituciones_button = tk.Button(frame_centro, text="Analizar Instituciones", command=lambda: abrir_nueva_pantalla_para_instituciones())
        self.instituciones_button.pack(pady=10)

        # Entrada y botón para analizar Journal por año
        self.journal_button = tk.Button(frame_centro, text="Analizar Journal", command=lambda: abrir_nueva_pantalla_para_journal())
        self.journal_button.pack(pady=10)

        # Entrada y botón para analizar Publisher por año
        self.publisher_button = tk.Button(frame_centro, text="Analizar Publisher", command=lambda: abrir_nueva_pantalla_para_publisher())
        self.publisher_button.pack(pady=10)

        # Elementos en frame centro

        # Entrada y botón para analizar base de datos por año
        self.base_datos_button = tk.Button(frame_centro, text="Analizar Base de Datos", command=lambda: abrir_nueva_pantalla_para_baseDeDatos())
        self.base_datos_button.pack(pady=10)

        # Entrada y botón para analizar el artículo más citado
        self.articulo_button = tk.Button(frame_centro, text="Analizar Artículo Más Citado", command=lambda: abrir_nueva_pantalla_para_articuloMasCitado())
        self.articulo_button.pack(pady=10)

        # Botón para analizar autores por base de datos
        self.database_autor_button = tk.Button(frame_centro, text="Analizar Database Autor", command=self.iniciar_database_autor)
        self.database_autor_button.pack(pady=10)

        # Botón para analizar los tres mejores journals
        self.journal_articulo_button = tk.Button(frame_centro, text="Analizar 3 Mejores Journal", command=self.iniciar_journal_articulo)
        self.journal_articulo_button.pack(pady=10)

        # Entrada y botón para analizar autores según la cantidad de journals
        self.analizar_autores_journal_button = tk.Button(frame_centro, text="Analizar Autores según Cantidad de Journals", command=lambda: abrir_nueva_pantalla_para_journalAutor())
        self.analizar_autores_journal_button.pack(pady=10)

        # Entrada y botón para analizar  journals segun el pais
        self.analizar_autores_journal_button = tk.Button(frame_centro, text="Analizar Autores según Cantidad de Journals", command=lambda: abrir_nueva_pantalla_para_analizarGrafo())
        self.analizar_autores_journal_button.pack(pady=10)

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
            self.estadistica.analizarAutores(year)
            messagebox.showinfo("Éxito", f"Análisis de autores completado para el año {year}.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un año válido en formato numérico.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el análisis de autores: {e}")

    def iniciar_analizarFecha(self):
        try:
            self.estadistica.analizarFecha()
            messagebox.showinfo("Éxito", "Procesamiento completado.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el procesamiento: {e}")


    def iniciar_contar_tipo_producto(self):
        try:
            self.estadistica.contar_tipos_producto()
            messagebox.showinfo("Éxito", "Procesamiento completado.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el procesamiento: {e}")


    def iniciar_analizar_instituciones(self):
        try:
            # Obtener el año ingresado
            year = int(self.instituciones_entry.get())
            # Instancia de Estadisticas y ejecución de analizarAutores
            self.estadistica.analizarInstituciones(year)
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
            self.estadistica.analizarJournal(year)
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
            self.estadistica.analizarPublisher(year)
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
            self.estadistica.analizarBaseDatos(year)
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
            self.estadistica.analizarArticuloMasCitado(year)
            messagebox.showinfo("Éxito", f"Análisis de Articulo mas citado para el año {year}.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un año válido en formato numérico.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el análisis de autores: {e}")

    def iniciar_database_autor(self):
        try:
            self.estadistica.analizar_database_autor()
            messagebox.showinfo("Éxito", "Procesamiento completado.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el procesamiento: {e}")

    def iniciar_journal_articulo(self):
        try:
            self.estadistica.analizar_journal_articulo()
            messagebox.showinfo("Éxito", "Procesamiento completado.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el procesamiento: {e}")

    def iniciar_analizar_autores_journal(self):
        try:
            # Obtener el año ingresado
            cantidadJournal = int(self.cantidad_journal_entry.get())
            # Instancia de Estadisticas y ejecución de analizarAutores
            self.estadistica.analizar_autores_journal(cantidadJournal)
            messagebox.showinfo("Éxito", f"Análisis de Articulo mas citado para el año {cantidadJournal}.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un año válido en formato numérico.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el análisis de autores: {e}")


    def iniciar_journal_articulo_pais(self):
        try:
            # Obtener el año ingresado
            journals = int(self.cantidad_journal_entry_pais.get())
            articulos_mas_citados= int(self.cantidad_articulo_entry.get())
            # Instancia de Estadisticas y ejecución de analizarAutores
            self.estadistica.analizar_journal_articulo_pais(journals,articulos_mas_citados)
            messagebox.showinfo("Éxito", f"Análisis de Articulo mas citado para el año .")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un año válido en formato numérico.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el análisis de autores: {e}")


if __name__ == "__main__":

    root = tk.Tk()
    app = InterfazFrecuencia(root)
    root.mainloop()

