import os
import csv
import random
from datetime import datetime
from collections import deque

RUTA_ARCHIVO_ESTUDIANTES = 'registroscsv/estudiantes.csv'
RUTA_ARCHIVO_REGISTRO_ACCESO = 'registroscsv/registro_acceso.csv'
RUTA_ARCHIVO_ESTADO_ESTUDIANTES = 'registroscsv/estado_estudiantes.csv'

def inicializar_archivos():
    if not os.path.exists(RUTA_ARCHIVO_ESTUDIANTES):
        with open(RUTA_ARCHIVO_ESTUDIANTES, 'w', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(['Nombre', 'Apellidos', 'Código', 'DNI', 'Facultad'])
    
    if not os.path.exists(RUTA_ARCHIVO_REGISTRO_ACCESO):
        with open(RUTA_ARCHIVO_REGISTRO_ACCESO, 'w', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(['Nombre', 'Apellidos', 'Código', 'Tipo de Acceso', 'Fecha y Hora'])
    
    if not os.path.exists(RUTA_ARCHIVO_ESTADO_ESTUDIANTES):
        with open(RUTA_ARCHIVO_ESTADO_ESTUDIANTES, 'w', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(['Código', 'Estado'])

def cargar_estudiantes():
    estudiantes = []
    with open(RUTA_ARCHIVO_ESTUDIANTES, 'r') as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Omitir encabezado
        for fila in lector:
            estudiantes.append(fila)
    return estudiantes

def agregar_estudiante(nombre, apellidos, codigo, dni, facultad):
    nuevo_estudiante = [nombre, apellidos, codigo, dni, facultad]
    with open(RUTA_ARCHIVO_ESTUDIANTES, 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(nuevo_estudiante)
    
    with open(RUTA_ARCHIVO_ESTADO_ESTUDIANTES, 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([codigo, 'Fuera'])

def eliminar_estudiante(estudiante):
    filas = []
    with open(RUTA_ARCHIVO_ESTUDIANTES, 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila != estudiante:
                filas.append(fila)
    
    with open(RUTA_ARCHIVO_ESTUDIANTES, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(filas)
    
    codigo = estudiante[2]
    filas = []
    with open(RUTA_ARCHIVO_ESTADO_ESTUDIANTES, 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] != codigo:
                filas.append(fila)
    
    with open(RUTA_ARCHIVO_ESTADO_ESTUDIANTES, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(filas)

def cargar_estado_estudiantes():
    estado = {}
    with open(RUTA_ARCHIVO_ESTADO_ESTUDIANTES, 'r') as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Omitir encabezado
        for fila in lector:
            estado[fila[0]] = fila[1]
    return estado

def actualizar_estado_estudiante(codigo, nuevo_estado):
    filas = []
    with open(RUTA_ARCHIVO_ESTADO_ESTUDIANTES, 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] == codigo:
                fila[1] = nuevo_estado
            filas.append(fila)
    
    with open(RUTA_ARCHIVO_ESTADO_ESTUDIANTES, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(filas)

def registrar_acceso(tipo_acceso):
    estudiantes = cargar_estudiantes()
    estado = cargar_estado_estudiantes()
    
    if tipo_acceso == "Entra Universidad":
        estudiantes_elegibles = [s for s in estudiantes if estado[s[2]] == 'Fuera']
    elif tipo_acceso == "Entra Residencia":
        estudiantes_elegibles = [s for s in estudiantes if estado[s[2]] == 'En Universidad']
    elif tipo_acceso == "Sale Universidad":
        estudiantes_elegibles = [s for s in estudiantes if estado[s[2]] == 'En Universidad']
    elif tipo_acceso == "Sale Residencia":
        estudiantes_elegibles = [s for s in estudiantes if estado[s[2]] == 'En Residencia']
    
    if estudiantes_elegibles:
        estudiante = random.choice(estudiantes_elegibles)
        marca_tiempo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        registro_acceso = [estudiante[0], estudiante[1], estudiante[2], tipo_acceso, marca_tiempo]
        
        if tipo_acceso == "Entra Universidad":
            actualizar_estado_estudiante(estudiante[2], 'En Universidad')
        elif tipo_acceso == "Entra Residencia":
            # Mantiene el estado 'En Universidad' y añade 'En Residencia'
            actualizar_estado_estudiante(estudiante[2], 'En Residencia')
        elif tipo_acceso == "Sale Universidad":
            actualizar_estado_estudiante(estudiante[2], 'Fuera')
        elif tipo_acceso == "Sale Residencia":
            actualizar_estado_estudiante(estudiante[2], 'En Universidad')
        
        with open(RUTA_ARCHIVO_REGISTRO_ACCESO, 'a', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(registro_acceso)
        return registro_acceso
    else:
        return None

def cargar_registro_acceso():
    registros = []
    if os.path.exists(RUTA_ARCHIVO_REGISTRO_ACCESO):
        with open(RUTA_ARCHIVO_REGISTRO_ACCESO, 'r') as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Omitir encabezado
            for fila in lector:
                registros.append(fila)
    return registros
