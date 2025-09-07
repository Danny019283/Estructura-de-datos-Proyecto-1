class Lista_Paciente:
    def __init__(self):
        self.__pacientes = []

    def insertar_pacientes(self, paciente):
        if paciente not in self.__pacientes:
            self.__pacientes.append(paciente)
            return True
        return False

    def actualizar_paciente(self, paciente):
        for pac in self.__pacientes:
            if pac == paciente:
                pac = paciente
                return True
        return False

    def borrar_paciente(self, cedula):
        paciente = self.buscar_paciente(cedula)
        if paciente is not None:
            self.__pacientes.remove(paciente)
            return True
        return False

    def buscar_paciente(self, cedula):
        for paciente in self.__pacientes:
            if paciente.cedula == cedula:
                return paciente
        return None

    def ordenar_edad_insercion(self):
        for i in range(1, len(self.__pacientes)):
            aux = self.__pacientes[i]
            j = i - 1
            while j >= 0 and self.__pacientes[j].edad > aux.edad:
                self.__pacientes[j + 1] = self.__pacientes[j]
                j -= 1
                self.__pacientes[j + 1] = aux