import heapq
from Acceso_a_datos.Manejo_De_Archivos import Manejo_De_Archivos as fs


class Cola_Emergencia:
    def __init__(self):
        self.__cola_pacientes = fs.cargar_datos("cola de emergencias")

    #gravedad baja = 3, media = 2, alta = 1
    def encolar_y_ordenar(self, diagnostico):
        #comprueba que no haya repetidos
        if self.buscar_paciente(diagnostico.paciente.cedula) is not None:
            return False

        #agrega el elemento a la cola de prioridad
        heapq.heappush(self.__cola_pacientes, (diagnostico.gravedad, diagnostico))
        fs.guardar_datos("cola de emergencias", self.__cola_pacientes)
        return True

    def buscar_paciente(self, cedula):
        #recorre la cola y devuelve el paciente buscado si es encontrado
        for prioridad, diagnostico in self.__cola_pacientes:
            if diagnostico.paciente.cedula == cedula:
                return prioridad, diagnostico
        return None

    def ver_paciente_mayor_prioridad(self):
        if self.esta_vacia():
            return None
        prioridad, diagnostico = self.__cola_pacientes[0]
        return diagnostico.paciente

    def atender(self):
        #elimina y lo devuelve el paciente con mayor prioridad
        if self.esta_vacia():
            return None
        eliminado = heapq.heappop(self.__cola_pacientes)
        fs.guardar_datos("cola de emergencias", self.__cola_pacientes)
        return eliminado

    def esta_vacia(self):
        return len(self.__cola_pacientes) == 0

    def __str__(self):
        if self.esta_vacia():
            return "No hay emergencias registradas"
        mostrar = f""
        for elemento in self.__cola_pacientes:
            prioridad, diagnostico = elemento
            mostrar += f"prioridad: {prioridad}, paciente: {diagnostico.paciente}\n"
        return mostrar