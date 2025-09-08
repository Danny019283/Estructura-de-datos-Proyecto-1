class Cola_Emergencia:
    def __init__(self):
        self.__cola_pacientes = []

    #prioridades baja = 3, media = 2, alta = 1

    def encolar_y_ordenar(self, diagnostico):
        if diagnostico in self.__cola_pacientes:
            return False
        self.__cola_pacientes.append(diagnostico)
        self.__cola_pacientes.sort(key = lambda p: p.gravedad)
        return True

    def sacar_primero(self):
        return self.__cola_pacientes.pop(0) if self.__cola_pacientes else None

    def atender(self):
        pass

    def mostrar_espera(self):
        pass