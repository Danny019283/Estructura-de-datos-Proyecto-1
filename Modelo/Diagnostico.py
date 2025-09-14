class Diagnostico:
    def __init__(self, descripcion, gravedad, fecha, paciente):
        self.__descripcion = descripcion
        # gravedad baja = 3, media = 2, alta = 1
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

    def fecha_con_formato(self):
        return f"{self.__fecha.day}/{self.__fecha.month}/{self.__fecha.year}"

    @property
    def paciente(self):
        return self.__paciente
    @paciente.setter
    def paciente(self, paciente):
        self.__paciente = paciente

    def __str__(self):
        return (f"Diagnostico[descripcion: {self.__descripcion}, gravedad: {self.__gravedad}, "
                f"fecha: {self.fecha_con_formato()}, paciente: {self.__paciente}]")