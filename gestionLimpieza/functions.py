import csv
from datetime import datetime
from models import Estudiante, Habitacion, Incidencia, ArbolIncidencias

# Simulación de datos
estudiantes = [Estudiante(i, f'Estudiante {i}') for i in range(1, 101)]
habitaciones = [Habitacion(i, estudiantes[2*i], estudiantes[2*i+1]) for i in range(50)]

# Asignación de tareas de limpieza
def asignar_tareas(habitaciones):
    tareas = {}
    for habitacion in habitaciones:
        tareas[habitacion.id_habitacion] = [habitacion.estudiante1.nombre, habitacion.estudiante2.nombre]
    return tareas

# Registro de incidencias
def registrar_incidencia(arbol, id_habitacion, descripcion, gravedad):
    id_incidencia = len(arbol.reporte_incidencias()) + 1
    nueva_incidencia = Incidencia(id_incidencia, id_habitacion, descripcion, gravedad)
    arbol.insertar(nueva_incidencia)
    return nueva_incidencia

# Generación de reportes de incidencias
def generar_reporte(arbol):
    incidencias = arbol.reporte_incidencias()
    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    reporte = []
    for incidencia in incidencias:
        reporte.append({
            'ID Incidencia': incidencia.id_incidencia,
            'ID Habitación': incidencia.id_habitacion,
            'Descripción': incidencia.descripcion,
            'Gravedad': incidencia.gravedad,
            'Fecha': fecha_actual  # Usar la fecha obtenida al inicio
        })
    return reporte


# Guardar reporte de incidencias en un archivo CSV
def guardar_reporte_csv(reporte, filename='reporte_incidencias.csv'):
    if not reporte:
        return
    keys = reporte[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(reporte)
