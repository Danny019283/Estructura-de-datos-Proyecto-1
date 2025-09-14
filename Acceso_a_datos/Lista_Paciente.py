
from Acceso_a_datos.Manejo_De_Archivos import Manejo_De_Archivos as fs


class Lista_Paciente:
    def __init__(self):
        self.__pacientes = fs.cargar_datos("Pacientes")

    def insertar_pacientes(self, paciente):
        if paciente not in self.__pacientes:
            self.__pacientes.append(paciente)
            fs.guardar_datos("Pacientes", self.__pacientes)
            return True
        return False

    def actualizar_paciente(self, paciente):
        for pac in self.__pacientes:
            if pac == paciente:
                self.__pacientes.remove(pac)
                self.insertar_pacientes(paciente)
                fs.guardar_datos("Pacientes", self.__pacientes)
                return True
        return False

    def borrar_paciente(self, cedula):
        paciente = self.buscar_paciente(cedula)
        if paciente is not None:
            self.__pacientes.remove(paciente)
            fs.guardar_datos("Pacientes", self.__pacientes)
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

    def ordenar_fecha_mergesort(self, arr = None):
        if arr is None:
            arr = self.__pacientes
            #caso 1
        if len(arr) == 1:
            return arr
        mitad = len(arr) // 2
        arr_izq = arr[:mitad]
        arr_der = arr[mitad:]

        arr_izq_orden = self.ordenar_fecha_mergesort(arr_izq)
        arr_der_orden = self.ordenar_fecha_mergesort(arr_der)

        return self.fecha_merge(arr_izq_orden, arr_der_orden)

    def fecha_merge(self, arr_izq, arr_der):
        arr_resultado = []
        while len(arr_izq) > 0 and len(arr_der) > 0:
            if arr_izq[0].fecha_ingreso > arr_der[0].fecha_ingreso:
                arr_resultado.append(arr_izq[0])
                arr_der.pop(0)
            else:
                arr_resultado.append(arr_der[0])
                arr_der.pop(0)
        return arr_resultado

    #falta definirla del todo
    def generar_estadis(self, i=0):
        if i == len(self.__pacientes):
            return []
        return [self.__pacientes[i]] + self.generar_estadis(i + 1)

    def estaVacia(self):
        if len(self.__pacientes) == 0:
            return True
        return False

    def edad_promedio(self, i = 0, suma_edad = 0):
        if self.estaVacia():
            return 0
        if i >= len(self.__pacientes):
            return  suma_edad/len(self.__pacientes)
        suma_edad += self.__pacientes[i].edad
        return self.edad_promedio(i + 1, suma_edad)


    def __str__(self):
        if self.estaVacia():
            return f"No hay pacientes registrados"
        mostrar = f""
        for paciente in self.__pacientes:
            mostrar += f"{paciente}\n"
        return mostrar

