class Consulta:
    def __init__(self, paciente, medico):
        self.__paciente = paciente
        self.__medico = medico

    @property
    def paciente(self):
        return self.__paciente
    @paciente.setter
    def paciente(self, paciente):
        self.__paciente = paciente

    @property
    def medico(self):
        return self.__medico
    @medico.setter
    def medico(self, medico):
        self.__medico = medico

    def __str__(self):
        return f"Consutla[paciente: {self.__paciente}, medico: {self.__medico}]"