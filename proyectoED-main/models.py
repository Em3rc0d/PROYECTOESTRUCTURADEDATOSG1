class Estudiante:
    def __init__(self, id_estudiante, nombre):
        self.id_estudiante = id_estudiante
        self.nombre = nombre

class Habitacion:
    def __init__(self, id_habitacion, estudiante1, estudiante2):
        self.id_habitacion = id_habitacion
        self.estudiante1 = estudiante1
        self.estudiante2 = estudiante2
        self.incidencias = []

class Incidencia:
    def __init__(self, id_incidencia, id_habitacion, descripcion, gravedad):
        self.id_incidencia = id_incidencia
        self.id_habitacion = id_habitacion
        self.descripcion = descripcion
        self.gravedad = gravedad
        self.left = None
        self.right = None

class ArbolIncidencias:
    def __init__(self):
        self.root = None

    def insertar(self, incidencia):
        if self.root is None:
            self.root = incidencia
        else:
            self._insertar_recursivo(self.root, incidencia)

    def _insertar_recursivo(self, nodo_actual, nueva_incidencia):
        if nueva_incidencia.id_incidencia < nodo_actual.id_incidencia:
            if nodo_actual.left is None:
                nodo_actual.left = nueva_incidencia
            else:
                self._insertar_recursivo(nodo_actual.left, nueva_incidencia)
        else:
            if nodo_actual.right is None:
                nodo_actual.right = nueva_incidencia
            else:
                self._insertar_recursivo(nodo_actual.right, nueva_incidencia)

    def buscar(self, id_incidencia):
        return self._buscar_recursivo(self.root, id_incidencia)

    def _buscar_recursivo(self, nodo_actual, id_incidencia):
        if nodo_actual is None or nodo_actual.id_incidencia == id_incidencia:
            return nodo_actual
        elif id_incidencia < nodo_actual.id_incidencia:
            return self._buscar_recursivo(nodo_actual.left, id_incidencia)
        else:
            return self._buscar_recursivo(nodo_actual.right, id_incidencia)

    def reporte_incidencias(self):
        incidencias = []
        self._recolectar_incidencias(self.root, incidencias)
        return incidencias

    def _recolectar_incidencias(self, nodo_actual, incidencias):
        if nodo_actual is not None:
            self._recolectar_incidencias(nodo_actual.left, incidencias)
            incidencias.append(nodo_actual)
            self._recolectar_incidencias(nodo_actual.right, incidencias)
