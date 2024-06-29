from functions import asignar_tareas
from models import estudiantes, habitaciones, ArbolIncidencias
from gui import cargar_incidencias_desde_csv

# Uso de las funciones
tareas = asignar_tareas(habitaciones)
print("Tareas de limpieza asignadas:", tareas)

# Inicialización del árbol de incidencias (esto se hará también en `gui.py`)
arbol_incidencias = ArbolIncidencias()
# Cargar incidencias desde el archivo CSV al inicio
cargar_incidencias_desde_csv()