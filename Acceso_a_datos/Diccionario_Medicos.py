from Modelo import Personal
from Acceso_a_datos.Manejo_De_Archivos import Manejo_De_Archivos as fs

class Diccionario_Medicos:
    def __init__(self):
        self.__dicc_medicos = {}
        if self.esta_vacia():
            fs.cargar_datos("Medicos")

    @property
    def dicc_medicos(self):
        #devuelve una copia del diccionario para mostrar la jerarquia
        return self.__dicc_medicos.copy()

    def insertar(self, personal: Personal):
        #inserta los medico al diccionario con su cedula como key
        if personal in self.__dicc_medicos: #repetido
            return False
        self.__dicc_medicos[personal.cedula] = personal
        fs.guardar_datos("Medicos", self.__dicc_medicos)
        return True

    def actualizar(self, personal: Personal):
        if self.buscar(personal.cedula) is not None:
            return False
        self.__dicc_medicos[personal.cedula] = personal
        fs.guardar_datos("Medicos", self.__dicc_medicos)
        return True

    def buscar(self, cedula):
        try:
            return self.__dicc_medicos[cedula]
        except KeyError:
            return None

    def borrar(self, cedula):
        if self.buscar(cedula) is None:
            return False
        self.__dicc_medicos.pop(cedula)
        fs.guardar_datos("Medicos", self.__dicc_medicos)
        return True

    def esta_vacia(self):
        if len(self.__dicc_medicos) == 0:
            return True
        return False

    def __str__(self):
        return self.dicc_medicos.__str__()
