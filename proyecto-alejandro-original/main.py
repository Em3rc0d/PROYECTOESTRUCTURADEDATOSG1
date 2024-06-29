import tkinter as tk
from tkinter import ttk, messagebox
import gestor_estudiantes

class AppResidenciaUniversitaria(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Gestión de Residencia Universitaria")
        self.geometry("1000x600")
        
        self.crear_widgets()
        
    def crear_widgets(self):
        self.marcos = {}
        
        contenedor = ttk.Frame(self)
        contenedor.pack(expand=True, fill='both')
        
        # Crear todos los marcos
        for F in (Panel, ControlAcceso, ControlTiempoResidencia, VerEstudiantes):
            nombre_pagina = F.__name__
            marco = F(parent=contenedor, controller=self)
            self.marcos[nombre_pagina] = marco
            marco.place(relwidth=1, relheight=1)
        
        self.mostrar_marco("Panel")
        
    def mostrar_marco(self, nombre_pagina):
        marco = self.marcos[nombre_pagina]
        marco.tkraise()

class Panel(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        etiqueta = ttk.Label(self, text="Sistema de Gestión de Residencia", font=("Helvetica", 24, "bold"))
        etiqueta.place(relx=0.5, rely=0.2, anchor='center')
        
        # Botones de navegación
        botones = [
            ("Control de Acceso", "ControlAcceso"),
            ("Ver Estudiantes", "VerEstudiantes")
        ]
        
        for i, (texto, marco) in enumerate(botones):
            boton = ttk.Button(self, text=texto, command=lambda m=marco: controller.mostrar_marco(m))
            boton.place(relx=0.5, rely=0.4 + i * 0.1, anchor='center')

class ControlAcceso(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        etiqueta = ttk.Label(self, text="Control de Acceso", font=("Helvetica", 20))
        etiqueta.place(relx=0.5, rely=0.1, anchor='center')

        # Botones para Universidad
        boton_entrar_uni = ttk.Button(self, text="Entra Universidad", command=self.entrar_universidad)
        boton_entrar_uni.place(relx=0.2, rely=0.2, anchor='center')
        
        boton_salir_uni = ttk.Button(self, text="Sale Universidad", command=self.salir_universidad)
        boton_salir_uni.place(relx=0.2, rely=0.3, anchor='center')

        # Botones para Residencia
        boton_entrar_res = ttk.Button(self, text="Entra Residencia", command=self.entrar_residencia)
        boton_entrar_res.place(relx=0.8, rely=0.2, anchor='center')
        
        boton_salir_res = ttk.Button(self, text="Sale Residencia", command=self.salir_residencia)
        boton_salir_res.place(relx=0.8, rely=0.3, anchor='center')
        
        # Etiquetas para listas
        etiqueta_uni = ttk.Label(self, text="Universidad", font=("Helvetica", 16))
        etiqueta_uni.place(relx=0.2, rely=0.4, anchor='center')
        
        etiqueta_res = ttk.Label(self, text="Residencia", font=("Helvetica", 16))
        etiqueta_res.place(relx=0.8, rely=0.4, anchor='center')
        
        # Lista para mostrar estudiantes de universidad
        self.lista_uni = tk.Listbox(self, font=("Helvetica", 12))
        self.lista_uni.place(relx=0.2, rely=0.55, anchor='center', relwidth=0.35, relheight=0.2)
        
        # Lista para mostrar estudiantes de residencia
        self.lista_res = tk.Listbox(self, font=("Helvetica", 12))
        self.lista_res.place(relx=0.8, rely=0.55, anchor='center', relwidth=0.35, relheight=0.2)
        
        # Lista para mostrar registro de acceso de universidad
        self.lista_registro_uni = tk.Listbox(self, font=("Helvetica", 12))
        self.lista_registro_uni.place(relx=0.2, rely=0.85, anchor='center', relwidth=0.35, relheight=0.2)
        
        # Lista para mostrar registro de acceso de residencia
        self.lista_registro_res = tk.Listbox(self, font=("Helvetica", 12))
        self.lista_registro_res.place(relx=0.8, rely=0.85, anchor='center', relwidth=0.35, relheight=0.2)
        
        self.cargar_registro_acceso()
        
        boton_volver = ttk.Button(self, text="Volver", command=lambda: controller.mostrar_marco("Panel"))
        boton_volver.place(relx=0.5, rely=0.9, anchor='center')

    def cargar_registro_acceso(self):
        self.lista_uni.delete(0, tk.END)
        self.lista_res.delete(0, tk.END)
        self.lista_registro_uni.delete(0, tk.END)
        self.lista_registro_res.delete(0, tk.END)
        
        estudiantes = gestor_estudiantes.cargar_estudiantes()
        estados = gestor_estudiantes.cargar_estado_estudiantes()
        registro_acceso = gestor_estudiantes.cargar_registro_acceso()
        
        for estudiante in estudiantes:
            info_estudiante = ' | '.join(estudiante)
            if estados[estudiante[2]] == 'En Universidad' or estados[estudiante[2]] == 'En Residencia':
                self.lista_uni.insert(tk.END, info_estudiante)
            if estados[estudiante[2]] == 'En Residencia':
                self.lista_res.insert(tk.END, info_estudiante)
        
        for entrada_registro in registro_acceso:
            info_registro = f"{entrada_registro[0]} {entrada_registro[1]} | {entrada_registro[2]} | {entrada_registro[4]} | {entrada_registro[3]}"
            if entrada_registro[3] in ["Entra Universidad", "Sale Universidad"]:
                self.lista_registro_uni.insert(tk.END, info_registro)
            elif entrada_registro[3] in ["Entra Residencia", "Sale Residencia"]:
                self.lista_registro_res.insert(tk.END, info_registro)
    
    def entrar_universidad(self):
        self.manejar_acceso("Entra Universidad")

    def salir_universidad(self):
        self.manejar_acceso("Sale Universidad")
    
    def entrar_residencia(self):
        self.manejar_acceso("Entra Residencia")
    
    def salir_residencia(self):
        self.manejar_acceso("Sale Residencia")

    def manejar_acceso(self, tipo_acceso):
        registro_acceso = gestor_estudiantes.registrar_acceso(tipo_acceso)
        if registro_acceso:
            self.cargar_registro_acceso()

class ControlTiempoResidencia(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        etiqueta = ttk.Label(self, text="Control de Tiempo de Residencia", font=("Helvetica", 20))
        etiqueta.place(relx=0.5, rely=0.3, anchor='center')
        
        # Botón para actualizar
        boton_actualizar = ttk.Button(self, text="Actualizar")
        boton_actualizar.place(relx=0.5, rely=0.5, anchor='center')

        boton_volver = ttk.Button(self, text="Volver", command=lambda: controller.mostrar_marco("Panel"))
        boton_volver.place(relx=0.5, rely=0.7, anchor='center')

class VerEstudiantes(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        etiqueta = ttk.Label(self, text="Lista de Estudiantes", font=("Helvetica", 20))
        etiqueta.place(relx=0.5, rely=0.2, anchor='center')
        
        self.lista_estudiantes = tk.Listbox(self, font=("Helvetica", 12))
        self.lista_estudiantes.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.8, relheight=0.4)
        
        self.cargar_estudiantes()
        
        boton_agregar = ttk.Button(self, text="Agregar Estudiante", command=self.abrir_ventana_agregar_estudiante)
        boton_agregar.place(relx=0.35, rely=0.8, anchor='center')
        
        boton_eliminar = ttk.Button(self, text="Eliminar Estudiante", command=self.abrir_ventana_eliminar_estudiante)
        boton_eliminar.place(relx=0.65, rely=0.8, anchor='center')
        
        boton_volver = ttk.Button(self, text="Volver", command=lambda: controller.mostrar_marco("Panel"))
        boton_volver.place(relx=0.5, rely=0.9, anchor='center')
        
    def cargar_estudiantes(self):
        self.lista_estudiantes.delete(0, tk.END)
        estudiantes = gestor_estudiantes.cargar_estudiantes()
        for estudiante in estudiantes:
            self.lista_estudiantes.insert(tk.END, ' | '.join(estudiante))
    
    def abrir_ventana_agregar_estudiante(self):
        nueva_ventana = tk.Toplevel(self)
        nueva_ventana.title("Agregar Estudiante")
        nueva_ventana.geometry("400x400")
        
        # Nombre
        etiqueta_nombre = ttk.Label(nueva_ventana, text="Nombre:")
        etiqueta_nombre.place(relx=0.1, rely=0.1)
        self.entrada_nombre = ttk.Entry(nueva_ventana)
        self.entrada_nombre.place(relx=0.4, rely=0.1)
        
        # Apellidos
        etiqueta_apellidos = ttk.Label(nueva_ventana, text="Apellidos:")
        etiqueta_apellidos.place(relx=0.1, rely=0.2)
        self.entrada_apellidos = ttk.Entry(nueva_ventana)
        self.entrada_apellidos.place(relx=0.4, rely=0.2)
        
        # Código
        etiqueta_codigo = ttk.Label(nueva_ventana, text="Código:")
        etiqueta_codigo.place(relx=0.1, rely=0.3)
        self.entrada_codigo = ttk.Entry(nueva_ventana)
        self.entrada_codigo.place(relx=0.4, rely=0.3)
        
        # DNI
        etiqueta_dni = ttk.Label(nueva_ventana, text="DNI:")
        etiqueta_dni.place(relx=0.1, rely=0.4)
        self.entrada_dni = ttk.Entry(nueva_ventana)
        self.entrada_dni.place(relx=0.4, rely=0.4)
        
        # Facultad
        etiqueta_facultad = ttk.Label(nueva_ventana, text="Facultad:")
        etiqueta_facultad.place(relx=0.1, rely=0.5)
        self.entrada_facultad = ttk.Entry(nueva_ventana)
        self.entrada_facultad.place(relx=0.4, rely=0.5)
        
        # Botón para agregar
        boton_agregar = ttk.Button(nueva_ventana, text="Agregar", command=self.agregar_estudiante)
        boton_agregar.place(relx=0.4, rely=0.7)
        
    def agregar_estudiante(self):
        gestor_estudiantes.agregar_estudiante(
            self.entrada_nombre.get(),
            self.entrada_apellidos.get(),
            self.entrada_codigo.get(),
            self.entrada_dni.get(),
            self.entrada_facultad.get()
        )
        
        self.cargar_estudiantes()
        self.entrada_nombre.master.destroy()
        
    def abrir_ventana_eliminar_estudiante(self):
        estudiante_seleccionado = self.lista_estudiantes.get(tk.ACTIVE)
        if not estudiante_seleccionado:
            return
        
        nueva_ventana = tk.Toplevel(self)
        nueva_ventana.title("Eliminar Estudiante")
        nueva_ventana.geometry("400x200")

        etiqueta = ttk.Label(nueva_ventana, text="¿Estás seguro de eliminar este estudiante?")
        etiqueta.place(relx=0.1, rely=0.2)
        
        boton_confirmar = ttk.Button(nueva_ventana, text="Eliminar", command=lambda: self.eliminar_estudiante(estudiante_seleccionado, nueva_ventana))
        boton_confirmar.place(relx=0.4, rely=0.6)
        
    def eliminar_estudiante(self, estudiante, ventana):
        datos_estudiante = estudiante.split(' | ')
        gestor_estudiantes.eliminar_estudiante(datos_estudiante)
        self.cargar_estudiantes()
        ventana.destroy()

if __name__ == "__main__":
    gestor_estudiantes.inicializar_archivos()
    app = AppResidenciaUniversitaria()
    app.mainloop()
