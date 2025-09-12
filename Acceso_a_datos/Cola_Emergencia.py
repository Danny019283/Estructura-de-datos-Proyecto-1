import heapq

class Cola_Emergencia:
    def __init__(self):
        self.__cola_pacientes = []

    #gravedad baja = 3, media = 2, alta = 1
    def encolar_y_ordenar(self, diagnostico):
        #comprueba que no haya repetidos
        if self.buscar_paciente(diagnostico.paciente.cedula) is None:
            return False
        #agrega el elemento a la cola de prioridad
        heapq.heappush(self.__cola_pacientes, (diagnostico.gravedad, diagnostico.paciente))
        return True

    def buscar_paciente(self, cedula):
        #recorre la cola y devuelve el paciente buscado si es encontrado
        for elemento in self.__cola_pacientes:
            prioridad, paciente = elemento
            if paciente.cedula == cedula:
                return elemento
        return None

    def ver_paciente_mayor_prioridad(self):
        if self.esta_vacia():
            return None
        prioridad, paciente = self.__cola_pacientes[0]
        return paciente

    def atender(self):
        #elimina y lo devuelve
        #
        # el paciente con mayor prioridad



        if self.esta_vacia():
            return None
        return heapq.heappop(self.__cola_pacientes)

    def esta_vacia(self):
        return len(self.__cola_pacientes) == 0

    def __str__(self):
        return f"Cola Emergencia: {self.__cola_pacientes}"