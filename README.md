# **Proyecto Magna**

Link: [Proyecto Magna](https://github.com/Em3rc0d/PROYECTOESTRUCTURADEDATOSG1.git)

**Proyecto Magna** es una aplicación de interfaz gráfica desarrollada en Python utilizando Tkinter. La aplicación permite abrir y ejecutar diferentes proyectos desde una única interfaz centralizada. Cada proyecto está asociado con un botón, y al hacer clic en él, se ejecuta el script principal del proyecto correspondiente.

## **Contenidos**
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Uso](#uso)
5. [Estructura del Proyecto](#estructura-del-proyecto)
6. [Capturas de Pantalla](#capturas-de-pantalla)
7. [Personalización](#personalización)
8. [Contribuciones](#contribuciones)
9. [Licencia](#licencia)
10. [Contacto](#contacto)
11. [Etiquetas](#etiquetas)
12. [Enlaces](#enlaces)

## **Descripción del Proyecto**
El proyecto permite a los usuarios abrir y ejecutar diferentes scripts desde una interfaz gráfica centralizada. Cada script está asociado con un botón dentro de la interfaz. Al hacer clic en un botón, el script correspondiente se ejecuta automáticamente.

## **Requisitos**
1. Python 3.6 o superior
2. Tkinter (incluido con Python)
3. Sistema operativo: Windows, macOS o Linux

## **Instalación**

### **Clonar el repositorio**

```sh
git clone https://github.com/Em3rc0d/PROYECTOESTRUCTURADEDATOSG1.git
cd PROYECTOESTRUCTURADEDATOSG1
```

### **Instalar dependencias (si es necesario)**

```sh
pip install -r requirements.txt
```

### **Actualizar la ruta del ejecutable de Python**

Asegúrate de que la variable `python_executable` en el archivo `MAGNA.py` apunta a la ubicación correcta del ejecutable de Python en tu sistema.

## **Uso**

### **Ejecutar la aplicación**

```sh
python MAGNA.py
```

### **Interfaz de usuario**

La aplicación abrirá una ventana con botones etiquetados para cada proyecto. Haz clic en un botón para abrir y ejecutar el script principal del proyecto correspondiente.

## **Estructura del Proyecto**

```sh
PROYECTOESTRUCTURADEDATOSG1/
├── gestionComunicacioninterna/
├── gestionLimpieza/
│   ├── __pycache__/
│   ├── functions.py
│   ├── gui.py
│   ├── main.py
│   ├── models.py
├── gestionSalud/
│   ├── jorigito_proyecto_luzmila.py
├── gestionSeguridad/
│   ├── __pycache__/
│   ├── gestor_estudiantes.py
├── recursos/
│   ├── UNMSM.png
├── registroscsv/
│   ├── estado_estudiantes.csv
│   ├── estudiantes.csv
│   ├── registro_acceso.csv
│   ├── reporte_incidencias.csv
├── PROYECTO_LUZMILA_fabrizio_raul.py
├── MAGNA.py
└── README.md
```

## **Personalización**

### **Cambiar el estilo de la interfaz**

Puedes personalizar el color de fondo, las fuentes y otros estilos en el archivo `MAGNA.py` modificando las configuraciones de Tkinter.

### **Agregar nuevos proyectos**

1. Añade los scripts de tus nuevos proyectos en el directorio principal del proyecto.
2. Modifica la función `create_widgets` en `MAGNA.py` para incluir un nuevo botón que apunte al nuevo script.

## **Contribuciones**

Las contribuciones son bienvenidas. Para reportar problemas o sugerir mejoras, abre un "issue" o un "pull request" en el repositorio.

## **Licencia**

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## **Etiquetas**

- **Python**
- **Tkinter**
- **GUI**
- **Proyecto**
- **Ejemplo**
- **Interfaz gráfica**
- **Automatización**
- **Productividad**
