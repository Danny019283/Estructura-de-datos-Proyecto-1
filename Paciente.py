class Paciente:
    def __init__(self,cedula, nombre, edad):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__edad = edad

    @property
    def cedula(self):
        return self.__cedula
    @cedula.setter
    def cedula(self,cedula):
        self.__cedula = cedula

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,edad):
        self.__edad = edad

    def __str__(self):
        return (f"Paciente[ cedula: {self.__cedula}, nombre: {self.__nombre},"
                f"edad: {self.__edad}]")