class Diagnostico:
    def __init__(self, descripcion, gravedad, fecha, paciente):
        self.__descripcion = descripcion
        self.__gravedad = gravedad
        self.__fecha = fecha
        self.__paciente = paciente

    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @property
    def gravedad(self):
        return self.__gravedad
    @gravedad.setter
    def gravedad(self, gravedad):
        self.__gravedad = gravedad

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def paciente(self):
        return self.__paciente
    @paciente.setter
    def paciente(self, paciente):
        self.__paciente = paciente

    def __str__(self):
        return (f"Diagnostico[descripcion: {self.__descripcion}, gravedad: {self.__gravedad}, "
                f"fecha: {self.__fecha}, paciente: {self.__paciente}]")