import csv
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk

class Residente:
    def __init__(self, id, nombre, edad, genero, habitacion):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.habitacion = habitacion

class Chequeo:
    def __init__(self, id_chequeo, id_residente, fecha, sintoma, estado_actual):
        self.id_chequeo = id_chequeo
        self.id_residente = id_residente
        self.fecha = fecha
        self.sintoma = sintoma
        self.estado_actual = estado_actual

# Funciones para manejar CSV
def leer_residentes(file_path):
    residentes = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            residentes.append(Residente(row['ID'], row['Nombre'], row['Edad'], row['Genero'], row['Habitacion']))
    return residentes

def leer_chequeos(file_path):
    chequeos = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            chequeos.append(Chequeo(row['ID_Chequeo'], row['ID_Residente'], row['Fecha'], row['Sintomas'], row['Estado_Actual']))
    return chequeos

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Salud de Residentes")

        self.create_widgets()

    def create_widgets(self):
        self.tabControl = ttk.Notebook(self.root)

        # Pestañas
        self.tab_residentes = ttk.Frame(self.tabControl)
        self.tab_registro_residentes = ttk.Frame(self.tabControl)
        self.tab_registro_chequeos = ttk.Frame(self.tabControl)
        self.tab_diagnosticos = ttk.Frame(self.tabControl)

        # Nombres de pestañas actualizados
        self.tabControl.add(self.tab_residentes, text='Residentes')
        self.tabControl.add(self.tab_registro_residentes, text='Registro de Residentes')
        self.tabControl.add(self.tab_registro_chequeos, text='Registro de Chequeos')
        self.tabControl.add(self.tab_diagnosticos, text='Diagnósticos')

        self.tabControl.pack(expand=1, fill="both")

        self.create_residentes_tab()
        self.create_registro_residentes_tab()
        self.create_registro_chequeos_tab()
        self.create_diagnosticos_tab()

    # Funciones para la pestaña "Residentes"
    def create_residentes_tab(self):
        ttk.Label(self.tab_residentes, text="Gestión de Residentes").grid(column=0, row=0, padx=10, pady=10)

        self.residente_tree = ttk.Treeview(self.tab_residentes, columns=("ID", "Nombre", "Edad", "Género", "Habitación"), show='headings')
        self.residente_tree.heading("ID", text="ID")
        self.residente_tree.heading("Nombre", text="Nombre")
        self.residente_tree.heading("Edad", text="Edad")
        self.residente_tree.heading("Género", text="Género")
        self.residente_tree.heading("Habitación", text="Habitación")

        self.residente_tree.grid(column=0, row=1, padx=10, pady=10, columnspan=4)

        ttk.Button(self.tab_residentes, text="Agregar Residente", command=self.agregar_residente).grid(column=0, row=2, padx=10, pady=10)
        ttk.Button(self.tab_residentes, text="Editar Residente", command=self.editar_residente).grid(column=1, row=2, padx=10, pady=10)
        ttk.Button(self.tab_residentes, text="Eliminar Residente", command=self.eliminar_residente).grid(column=2, row=2, padx=10, pady=10)

    def agregar_residente(self):
        self.entrada_residente(None)

    def editar_residente(self):
        selected_item = self.residente_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un residente para editar.")
            return
        item = self.residente_tree.item(selected_item)
        self.entrada_residente(item, selected_item[0])

    def eliminar_residente(self):
        selected_item = self.residente_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un residente para eliminar.")
            return
        self.residente_tree.delete(selected_item)

    def entrada_residente(self, item, iid=None):
        data = item['values'] if item else ["", "", "", "", ""]
        entry_window = tk.Toplevel(self.root)
        entry_window.title("Entrada de Residente")

        tk.Label(entry_window, text="ID").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(entry_window, text="Nombre").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(entry_window, text="Edad").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(entry_window, text="Género").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(entry_window, text="Habitación").grid(row=4, column=0, padx=10, pady=5)

        id_entry = tk.Entry(entry_window)
        nombre_entry = tk.Entry(entry_window)
        edad_entry = tk.Entry(entry_window)
        genero_entry = tk.Entry(entry_window)
        habitacion_entry = tk.Entry(entry_window)

        id_entry.grid(row=0, column=1, padx=10, pady=5)
        nombre_entry.grid(row=1, column=1, padx=10, pady=5)
        edad_entry.grid(row=2, column=1, padx=10, pady=5)
        genero_entry.grid(row=3, column=1, padx=10, pady=5)
        habitacion_entry.grid(row=4, column=1, padx=10, pady=5)

        id_entry.insert(0, data[0])
        nombre_entry.insert(0, data[1])
        edad_entry.insert(0, data[2])
        genero_entry.insert(0, data[3])
        habitacion_entry.insert(0, data[4])

        def save_data():
            if not id_entry.get() or not nombre_entry.get() or not edad_entry.get():
                messagebox.showerror("Error", "Por favor complete todos los campos.")
                return
            new_data = [id_entry.get(), nombre_entry.get(), edad_entry.get(), genero_entry.get(),
                        habitacion_entry.get()]
            if item:
                self.residente_tree.item(iid, values=new_data)  # Usamos el 'iid' pasado como argumento
            else:
                self.residente_tree.insert('', 'end', values=new_data)
            entry_window.destroy()
            self.update_reportes_tab()

        tk.Button(entry_window, text="Guardar", command=save_data).grid(row=5, column=0, columnspan=2, pady=10)

    # Funciones para la pestaña "Registro de Residentes"
    def create_registro_residentes_tab(self):
        ttk.Label(self.tab_registro_residentes, text="Registro de Residentes").grid(column=0, row=0, padx=10, pady=10)

        self.registro_residente_tree = ttk.Treeview(self.tab_registro_residentes, columns=("ID", "Nombre"), show='headings')
        self.registro_residente_tree.heading("ID", text="ID")
        self.registro_residente_tree.heading("Nombre", text="Nombre")

        self.registro_residente_tree.grid(column=0, row=1, padx=10, pady=10, columnspan=4)

        self.tab_registro_residentes.bind("<Visibility>", self.update_registro_residentes_tab)

        ttk.Button(self.tab_registro_residentes, text="Agregar Chequeo", command=self.agregar_chequeo).grid(column=0, row=2, padx=10, pady=10)

    def update_registro_residentes_tab(self, event):
        for item in self.registro_residente_tree.get_children():
            self.registro_residente_tree.delete(item)
        for item in self.residente_tree.get_children():
            values = self.residente_tree.item(item, 'values')
            self.registro_residente_tree.insert('', 'end', values=(values[0], values[1]))

    def agregar_chequeo(self):
        selected_item = self.registro_residente_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un residente para agregar chequeo.")
            return
        item = self.registro_residente_tree.item(selected_item)
        self.entrada_chequeo(item['values'][0])

    def entrada_chequeo(self, id_residente):
        entry_window = tk.Toplevel(self.root)
        entry_window.title("Entrada de Chequeo")

        tk.Label(entry_window, text="ID de Chequeo").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(entry_window, text="Fecha").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(entry_window, text="Síntomas").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(entry_window, text="Estado Actual").grid(row=3, column=0, padx=10, pady=5)

        id_chequeo_entry = tk.Entry(entry_window)
        fecha_entry = tk.Entry(entry_window)
        sintomas_entry = tk.Entry(entry_window)
        estado_actual_entry = tk.Entry(entry_window)

        id_chequeo_entry.grid(row=0, column=1, padx=10, pady=5)
        fecha_entry.grid(row=1, column=1, padx=10, pady=5)
        sintomas_entry.grid(row=2, column=1, padx=10, pady=5)
        estado_actual_entry.grid(row=3, column=1, padx=10, pady=5)

        def save_data():
            if not id_chequeo_entry.get() or not fecha_entry.get():
                messagebox.showerror("Error", "Por favor complete todos los campos.")
                return
            new_data = [id_chequeo_entry.get(), id_residente, fecha_entry.get(), sintomas_entry.get(), estado_actual_entry.get()]
            self.chequeo_tree.insert('', 'end', values=new_data)
            self.update_diagnostico_tab()
            entry_window.destroy()

        tk.Button(entry_window, text="Guardar", command=save_data).grid(row=4, column=0, columnspan=2, pady=10)

    # Funciones para la pestaña "Registro de Chequeos"
    def create_registro_chequeos_tab(self):
        ttk.Label(self.tab_registro_chequeos, text="Registro de Chequeos").grid(column=0, row=0, padx=10, pady=10)

        self.chequeo_tree = ttk.Treeview(self.tab_registro_chequeos, columns=("ID Chequeo", "ID Residente", "Fecha", "Síntomas", "Estado Actual"), show='headings')
        self.chequeo_tree.heading("ID Chequeo", text="ID Chequeo")
        self.chequeo_tree.heading("ID Residente", text="ID Residente")
        self.chequeo_tree.heading("Fecha", text="Fecha")
        self.chequeo_tree.heading("Síntomas", text="Síntomas")
        self.chequeo_tree.heading("Estado Actual", text="Estado Actual")

        self.chequeo_tree.grid(column=0, row=1, padx=10, pady=10, columnspan=4)

    # Funciones para la pestaña "Diagnósticos"
    def create_diagnosticos_tab(self):
        ttk.Label(self.tab_diagnosticos, text="Diagnósticos").grid(column=0, row=0, padx=10, pady=10)

        self.diagnostico_tree = ttk.Treeview(self.tab_diagnosticos, columns=("ID Chequeo", "ID Residente", "Tratamiento", "Observación"), show='headings')
        self.diagnostico_tree.heading("ID Chequeo", text="ID Chequeo")
        self.diagnostico_tree.heading("ID Residente", text="ID Residente")
        self.diagnostico_tree.heading("Tratamiento", text="Tratamiento")
        self.diagnostico_tree.heading("Observación", text="Observación")

        self.diagnostico_tree.grid(column=0, row=1, padx=10, pady=10, columnspan=4)

        self.tab_diagnosticos.bind("<Visibility>", self.update_diagnostico_tab)

    def update_diagnostico_tab(self, event=None):
        for item in self.diagnostico_tree.get_children():
            self.diagnostico_tree.delete(item)

        tratamientos = {
            "Fiebre": "Paracetamol - Cada 6 horas",
            "Dolor de cabeza": "Ibuprofeno - Cada 8 horas",
            "Tos": "Dextrometorfano - Cada 8 horas",
            "Dolor muscular": "Naproxeno - Cada 8 horas",
            "Gripe": "DayQuil - Cada 6 horas",
            "Dolor de garganta": "Strepsils - Cada 3 horas",
            "Congestión nasal": "Pseudoefedrina - Cada 6 horas",
            "Dolor estomacal": "Bismuto subsalicilato - Cada 3 horas",
            "Vómito": "Dimenhidrinato - Cada 4 horas"
        }

        observaciones = {
            "Muy bien": "No requiere descanso",
            "Bien": "No requiere descanso",
            "Regular": "No requiere descanso",
            "Mal": "Descansar 1 día",
            "Muy mal": "Descansar 3 días"
        }

        for item in self.chequeo_tree.get_children():
            values = self.chequeo_tree.item(item, 'values')
            sintoma = values[3]
            estado = values[4]

            tratamiento = tratamientos.get(sintoma, "No requiere tratamiento")
            observacion = observaciones.get(estado, "No hay observaciones")

            new_data = [values[0], values[1], tratamiento, observacion]
            self.diagnostico_tree.insert('', 'end', values=new_data)

    

root = tk.Tk()
app = App(root)
root.mainloop()