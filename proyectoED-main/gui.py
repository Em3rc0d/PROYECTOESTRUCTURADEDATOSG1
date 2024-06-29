import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime

from functions import generar_reporte, registrar_incidencia
from models import Estudiante, Habitacion, Incidencia, ArbolIncidencias

# Inicialización del árbol de incidencias
arbol_incidencias = ArbolIncidencias()
habitaciones = [i for i in range(1, 51)]
# Función para registrar una nueva incidencia
def registrar_incidencia_gui():
    try:
        id_habitacion = int(combobox_habitacion.get().split(' ')[1])
        descripcion = entry_descripcion.get()
        gravedad = combobox_gravedad.get()
        incidencia = registrar_incidencia(arbol_incidencias, id_habitacion, descripcion, gravedad)
        messagebox.showinfo("Incidencia Registrada", f"Incidencia {incidencia.id_incidencia} registrada con éxito.")
        # Actualizar el reporte después de registrar
        mostrar_reporte()
    except ValueError:
        messagebox.showerror("Error", "Por favor, selecciona una habitación válida.")

# Función para modificar una incidencia existente
def modificar_incidencia():
    try:
        id_incidencia = int(entry_id_incidencia.get())
        nueva_descripcion = entry_nueva_descripcion.get()
        nueva_gravedad = combobox_nueva_gravedad.get()
        
        incidencia = arbol_incidencias.buscar(id_incidencia)
        if incidencia:
            incidencia.descripcion = nueva_descripcion
            incidencia.gravedad = nueva_gravedad
            messagebox.showinfo("Incidencia Modificada", f"Incidencia {id_incidencia} modificada correctamente.")
            # Actualizar el reporte después de modificar
            mostrar_reporte()
        else:
            messagebox.showerror("Error", f"Incidencia con ID {id_incidencia} no encontrada.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un ID de incidencia válido.")

# Función para mostrar el reporte de incidencias
def mostrar_reporte():
    reporte = generar_reporte(arbol_incidencias)
    reporte_text.delete('1.0', tk.END)
    for incidencia in reporte:
        reporte_text.insert(tk.END, f"ID Incidencia: {incidencia['ID Incidencia']}\n")
        reporte_text.insert(tk.END, f"ID Habitación: {incidencia['ID Habitación']}\n")
        reporte_text.insert(tk.END, f"Descripción: {incidencia['Descripción']}\n")
        reporte_text.insert(tk.END, f"Gravedad: {incidencia['Gravedad']}\n")
        reporte_text.insert(tk.END, f"Fecha: {incidencia['Fecha']}\n\n")

# Función para guardar el reporte de incidencias en un archivo CSV
def guardar_reporte_csv():
    reporte = generar_reporte(arbol_incidencias)
    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Obtener la fecha una sola vez
    filename = 'reporte_incidencias.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['ID Incidencia', 'ID Habitación', 'Descripción', 'Gravedad', 'Fecha']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for incidencia in reporte:
            writer.writerow({
                'ID Incidencia': incidencia['ID Incidencia'],
                'ID Habitación': incidencia['ID Habitación'],
                'Descripción': incidencia['Descripción'],
                'Gravedad': incidencia['Gravedad'],
                'Fecha': fecha_actual  # Usar la misma fecha para todas las incidencias
            })
    messagebox.showinfo("Reporte Guardado", f"Reporte de incidencias guardado como '{filename}'.")



# Función para cargar incidencias desde un archivo CSV
def cargar_incidencias_desde_csv():
    try:
        filename = 'reporte_incidencias.csv'
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id_incidencia = int(row['ID Incidencia'])
                id_habitacion = int(row['ID Habitación'])
                descripcion = row['Descripción']
                gravedad = row['Gravedad']
                
                # Verificar si la incidencia ya existe en el árbol
                incidencia_existente = arbol_incidencias.buscar(id_incidencia)
                if incidencia_existente:
                    continue  # Si ya existe, pasar a la siguiente incidencia
                
                # Si no existe, crear e insertar la nueva incidencia
                nueva_incidencia = Incidencia(id_incidencia, id_habitacion, descripcion, gravedad)
                arbol_incidencias.insertar(nueva_incidencia)
        
        # Actualizar el reporte después de cargar desde CSV
        mostrar_reporte()
        
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo 'reporte_incidencias.csv' no encontrado.")



# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Limpieza y Reporte de Incidencias")

# Sección de Registro de Incidencias
frame_registro = ttk.LabelFrame(root, text="Registrar Incidencia")
frame_registro.grid(row=0, column=0, padx=10, pady=10)

ttk.Label(frame_registro, text="Habitación:").grid(row=0, column=0, padx=5, pady=5)
combobox_habitacion = ttk.Combobox(frame_registro)
combobox_habitacion['values'] = [f'Habitación {hab}' for hab in habitaciones]
combobox_habitacion.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_registro, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
entry_descripcion = ttk.Entry(frame_registro)
entry_descripcion.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_registro, text="Gravedad:").grid(row=2, column=0, padx=5, pady=5)
combobox_gravedad = ttk.Combobox(frame_registro, values=["Leve", "Moderado", "Grave"])
combobox_gravedad.grid(row=2, column=1, padx=5, pady=5)

btn_registrar = ttk.Button(frame_registro, text="Registrar Incidencia", command=registrar_incidencia_gui)
btn_registrar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Sección de Modificación de Incidencias
frame_modificacion = ttk.LabelFrame(root, text="Modificar Incidencia")
frame_modificacion.grid(row=1, column=0, padx=10, pady=10)

ttk.Label(frame_modificacion, text="ID Incidencia:").grid(row=0, column=0, padx=5, pady=5)
entry_id_incidencia = ttk.Entry(frame_modificacion)
entry_id_incidencia.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_modificacion, text="Nueva Descripción:").grid(row=1, column=0, padx=5, pady=5)
entry_nueva_descripcion = ttk.Entry(frame_modificacion)
entry_nueva_descripcion.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_modificacion, text="Nueva Gravedad:").grid(row=2, column=0, padx=5, pady=5)
combobox_nueva_gravedad = ttk.Combobox(frame_modificacion, values=["Leve", "Moderado", "Grave"])
combobox_nueva_gravedad.grid(row=2, column=1, padx=5, pady=5)

btn_modificar = ttk.Button(frame_modificacion, text="Modificar Incidencia", command=modificar_incidencia)
btn_modificar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Sección de Reporte de Incidencias
frame_reporte = ttk.LabelFrame(root, text="Reporte de Incidencias")
frame_reporte.grid(row=0, column=1, rowspan=2, padx=10, pady=10)

btn_mostrar_reporte = ttk.Button(frame_reporte, text="Mostrar Reporte", command=mostrar_reporte)
btn_mostrar_reporte.grid(row=0, column=0, padx=5, pady=5)

btn_guardar_reporte_csv = ttk.Button(frame_reporte, text="Guardar Reporte CSV", command=guardar_reporte_csv)
btn_guardar_reporte_csv.grid(row=0, column=1, padx=5, pady=5)

btn_cargar_desde_csv = ttk.Button(frame_reporte, text="Cargar desde CSV", command=cargar_incidencias_desde_csv)
btn_cargar_desde_csv.grid(row=0, column=2, padx=5, pady=5)

reporte_text = tk.Text(frame_reporte, width=50, height=20)
reporte_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Mostrar reporte inicial al abrir la aplicación
cargar_incidencias_desde_csv()
mostrar_reporte()

# Ejecutar la aplicación
root.mainloop()
