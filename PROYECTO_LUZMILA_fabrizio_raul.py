import tkinter as tk
from tkinter import ttk
import os

# Estructuras de datos
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def obtener_todos(self):
        datos = []
        actual = self.cabeza
        while actual:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, dato):
        self.elementos.append(dato)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def obtener_todos(self):
        return self.elementos[::-1]

class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, dato):
        self.elementos.append(dato)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def obtener_todos(self):
        return self.elementos

# Instancias de estructuras de datos
anuncios = ListaEnlazada()
quejas = Pila()
sugerencias = Cola()

# Funciones auxiliares para manejo de archivos
def guardar_en_archivo(nombre_archivo, texto):
    with open(nombre_archivo, 'a') as file:
        file.write(texto + '\n')

def leer_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    with open(nombre_archivo, 'r') as file:
        return file.readlines()

# Ventana Principal
def ventana_principal():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("PROYECTO")
    f = tk.Frame()
    f.pack(fill="both", expand="True")
    f.config(width="500", height="300")
    f.config(bd=20)
    f.config(relief="ridge")
    label = tk.Label(f, text="ELIJA QUIEN VA A INGRESAR", font=("Algerian", 15))
    label.place(relx=0.5, y=50, anchor="center")

    def abrir_ventana_residente():
        root.destroy()
        ventana_residente()

    def abrir_ventana_administrativo():
        root.destroy()
        ventana_administrativo()

    button_residente = tk.Button(root, text="RESIDENTE", command=abrir_ventana_residente, cursor="hand2")
    button_residente.place(relx=0.5, y=120, anchor="center")

    button_administrativo = tk.Button(root, text="PERSONAL ADMINISTRATIVO", command=abrir_ventana_administrativo, cursor="hand2")
    button_administrativo.place(relx=0.5, y=200, anchor="center")

    root.mainloop()

# Ventana de Residente
def ventana_residente():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Residente")
    t = tk.Frame()
    t.pack(fill="both", expand="True")
    t.config(width="500", height="300")
    t.config(bd=20)
    t.config(relief="ridge")
    label1 = tk.Label(t, text="BIENVENIDO", font=("Algerian", 15))
    label1.place(relx=0.5, y=15, anchor="center")
    label2 = tk.Label(t, text="Elija la opcion que desea realizar", font=("Algerian", 13))
    label2.place(relx=0.5, y=50, anchor="center")

    def ver_anuncios():
        root.destroy()
        ventana_ver_anuncios()

    def presentar_queja():
        root.destroy()
        ventana_presentar_queja()

    def sugerir_algo():
        root.destroy()
        ventana_sugerir_algo()

    def volver():
        root.destroy()
        ventana_principal()

    tk.Button(root, text="Ver Anuncios", command=ver_anuncios, cursor="hand2").place(relx=0.5, y=100, anchor="center")
    tk.Button(root, text="Presentar Queja Anónima", command=presentar_queja, cursor="hand2").place(relx=0.5, y=140, anchor="center")
    tk.Button(root, text="Sugerir Algo", command=sugerir_algo, cursor="hand2").place(relx=0.5, y=180, anchor="center")
    tk.Button(root, text="Volver", command=volver, cursor="hand2").place(relx=0.5, y=220, anchor="center")
    tk.Button(root, text="Salir", command=root.quit, cursor="hand2").place(relx=0.5, y=260, anchor="center")

    root.mainloop()

# Ventana del Personal Administrativo
def ventana_administrativo():
    root = tk.Tk()
    root.title("Personal Administrativo")
    t = tk.Frame()
    t.pack(fill="both", expand="True")
    t.config(width="500", height="300")
    t.config(bd=20)
    t.config(relief="ridge")
    label1 = tk.Label(t, text="BIENVENIDO", font=("Algerian", 15))
    label1.place(relx=0.5, y=15, anchor="center")
    label2 = tk.Label(t, text="Elija la opcion que desea realizar", font=("Algerian", 13))
    label2.place(relx=0.5, y=50, anchor="center")

    def verificar_quejas():
        root.destroy()
        ventana_verificar_quejas()

    def realizar_anuncio():
        root.destroy()
        ventana_realizar_anuncio()

    def verificar_recomendaciones():
        root.destroy()
        ventana_verificar_recomendaciones()

    def volver():
        root.destroy()
        ventana_principal()

    tk.Button(root, text="Verificar Quejas", command=verificar_quejas, cursor="hand2").place(relx=0.5, y=100, anchor="center")
    tk.Button(root, text="Realizar un Anuncio", command=realizar_anuncio, cursor="hand2").place(relx=0.5, y=140, anchor="center")
    tk.Button(root, text="Verificar Recomendaciones", command=verificar_recomendaciones, cursor="hand2").place(relx=0.5, y=180, anchor="center")
    tk.Button(root, text="Volver", command=volver, cursor="hand2").place(relx=0.5, y=220, anchor="center")
    tk.Button(root, text="Salir", command=root.quit, cursor="hand2").place(relx=0.5, y=260, anchor="center")

    root.mainloop()

# Ventana para Realizar Anuncio
def ventana_realizar_anuncio():
    root = tk.Tk()
    root.title("REALIZAR ANUNCIO")
    t = tk.Frame()
    t.pack(fill="both", expand="True")
    t.config(width="500", height="300")
    t.config(bd=20)
    t.config(relief="ridge")

    tk.Label(root, text="Ingrese el anuncio:", font=("Footlight MT Light", 12)).place(relx=0.5, y=40, anchor="center")
    texto_anuncio = tk.Text(root, width=50, height=10)
    texto_anuncio.place(relx=0.5, y=150, anchor="center")

    def guardar_anuncio():
        anuncio = texto_anuncio.get("1.0", tk.END).strip()
        if anuncio:
            anuncios.agregar(anuncio)
            guardar_en_archivo('anuncios.txt', anuncio)
            root.destroy()
            ventana_administrativo()

    tk.Button(root, text="Guardar", command=guardar_anuncio).place(relx=0.85, y=260, anchor="center")
    tk.Button(root, text="Volver", command=lambda: [root.destroy(), ventana_administrativo()]).place(relx=0.15, y=260, anchor="center")

    root.mainloop()

# Ventana para Ver Anuncios
def ventana_ver_anuncios():
    root = tk.Tk()
    root.title("Ver Anuncios")
    root.title("ANUNCIOS")
    t = tk.Frame()
    t.pack(fill="both", expand="True")
    t.config(width="500", height="300")
    t.config(bd=20)
    t.config(relief="ridge")

    anuncios = leer_archivo('anuncios.txt')
    text_widget = tk.Text(root, width=40, height=10, font=("Algerian", 12))
    text_widget.place(relx=0.5, y=125, anchor="center")

    if not anuncios:
        text_widget.insert(tk.END, "No hay anuncios por el momento")
    else:
        for anuncio in anuncios:
            text_widget.insert(tk.END, anuncio.strip() + '\n')

    tk.Button(root, text="Volver", command=lambda: [root.destroy(), ventana_residente()]).place(relx=0.5, y=260, anchor="center")

    root.mainloop()

# Ventana para Presentar Queja
def ventana_presentar_queja():
    root = tk.Tk()
    root.title("PRESENTAR QUEJA")
    t = tk.Frame()
    t.pack(fill="both", expand="True")
    t.config(width="500", height="300")
    t.config(bd=20)
    t.config(relief="ridge")

    tk.Label(root, text="Ingrese su queja:", font=("Footlight MT Light", 13)).place(relx=0.5, y=40, anchor="center")
    texto_queja = tk.Text(root, width=50, height=10)
    texto_queja.place(relx=0.5, y=150, anchor="center")

    def guardar_queja():
        queja = texto_queja.get("1.0", tk.END).strip()
        if queja:
            quejas.apilar(queja)
            guardar_en_archivo('quejas.txt', queja)
            root.destroy()
            ventana_residente()

    tk.Button(root, text="Guardar", command=guardar_queja).place(relx=0.85, y=260, anchor="center")
    tk.Button(root, text="Volver", command=lambda: [root.destroy(), ventana_residente()]).place(relx=0.15, y=260, anchor="center")

    root.mainloop()

# Ventana para Sugerir Algo
def ventana_sugerir_algo():
    root = tk.Tk()
    root.title("SUGERENCIA")
    t = tk.Frame()
    t.pack(fill="both", expand="True")
    t.config(width="500", height="300")
    t.config(bd=20)
    t.config(relief="ridge")

    tk.Label(root, text="Ingrese su sugerencia:", font=("Footlight MT Light", 13)).place(relx=0.5, y=40, anchor="center")
    texto_sugerencia = tk.Text(root, width=50, height=10)
    texto_sugerencia.place(relx=0.5, y=150, anchor="center")

    def guardar_sugerencia():
        sugerencia = texto_sugerencia.get("1.0", tk.END).strip()
        if sugerencia:
            sugerencias.encolar(sugerencia)
            guardar_en_archivo('sugerencias.txt', sugerencia)
            root.destroy()
            ventana_residente()

    tk.Button(root, text="Guardar", command=guardar_sugerencia).place(relx=0.85, y=260, anchor="center")
    tk.Button(root, text="Volver", command=lambda: [root.destroy(), ventana_residente()]).place(relx=0.15, y=260, anchor="center")

    root.mainloop()

# Ventana para Verificar Quejas
def ventana_verificar_quejas():
    root = tk.Tk()
    root.title("Verificar Quejas")
    root.title("ANUNCIOS")
    t = tk.Frame()
    t.pack(fill="both", expand="True")
    t.config(width="500", height="300")
    t.config(bd=20)
    t.config(relief="ridge")

    quejas = leer_archivo('quejas.txt')
    listbox = tk.Listbox(root, width=70, height=12)
    listbox.place(relx=0.5, y=125, anchor="center")

    if not quejas:
        listbox.insert(tk.END, "No hay quejas por ahora")
    else:
        for queja in quejas:
            listbox.insert(tk.END, queja.strip())

    tk.Button(root, text="Volver", command=lambda: [root.destroy(), ventana_administrativo()]).place(relx=0.5, y=260, anchor="center")

    root.mainloop()

# Ventana para Verificar Recomendaciones
def ventana_verificar_recomendaciones():
    root = tk.Tk()
    root.title("RECOMENDACIONES")
    t = tk.Frame()
    t.pack(fill="both", expand="True")
    t.config(width="500", height="300")
    t.config(bd=20)
    t.config(relief="ridge")

    sugerencias = leer_archivo('sugerencias.txt')
    listbox = tk.Listbox(root, width=70, height=12)
    listbox.place(relx=0.5, y=125, anchor="center")

    if not sugerencias:
        listbox.insert(tk.END, "No hay sugerencias por ahora")
    else:
        for sugerencia in sugerencias:
            listbox.insert(tk.END, sugerencia.strip())

    tk.Button(root, text="Volver", command=lambda: [root.destroy(), ventana_administrativo()]).place(relx=0.5, y=260, anchor="center")

    root.mainloop()

ventana_principal()
