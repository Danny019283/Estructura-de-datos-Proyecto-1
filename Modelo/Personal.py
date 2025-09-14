class Personal:
    def __init__(self, cedula, nombre, puesto):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__puesto = puesto

    @property
    def cedula(self):
        return self.__cedula
    @cedula.setter
    def cedula(self, cedula):
        self.__cedula = cedula

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def puesto(self):
        return self.__puesto
    @puesto.setter
    def puesto(self, puesto):
        self.__puesto = puesto

    def __str__(self):
        return f"Personal[cedula: {self.__cedula}, nombre: {self.__nombre}, puesto: {self.__puesto}]"