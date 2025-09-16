from datetime import datetime
from Acceso_a_datos.Manejo_De_Archivos import Manejo_De_Archivos as fs


class Historial_Consultas:
    def __init__(self):
        self.__pila_consultas = fs.cargar_datos("Historial Consultas")

    def empujar(self, consulta, diagnostico=None):
        self.__pila_consultas.append((consulta, diagnostico))
        fs.guardar_datos("Historial Consultas", self.__pila_consultas)
        return True

    def deshacer_ult_cons(self):
        if self.esta_vacia():
            return None
        eliminado = self.__pila_consultas.pop()
        fs.guardar_datos("Historial Consultas", self.__pila_consultas)
        return eliminado

    def mostrar_historial(self):
        return list(reversed(self.__pila_consultas))

    def esta_vacia(self):
        return len(self.__pila_consultas) == 0

    def consultas_ultimo_mes(self, i = 0, cont = 0,  ultimo_mes = None):
        if self.esta_vacia():
            return 0
        if ultimo_mes is None:
            ultimo_mes = datetime(datetime.now().year, datetime.now().month, datetime.now().day) #toma el ultimo mes
        if i >= len(self.__pila_consultas):
            return cont
        if self.__pila_consultas[i][1].fecha.year == ultimo_mes.year: #verifica que el anio sea el actual
            if self.__pila_consultas[i][1].fecha.month == ultimo_mes.month: #vefica que el mes sea el actual y suma +1 contador si se cumple
                cont += 1
        return self.consultas_ultimo_mes(i + 1, cont, ultimo_mes)

    def __str__(self):
        if self.esta_vacia():
            return "Historial vacío"
        mostrar = f""
        for consulta, diagnostico in self.__pila_consultas:
            mostrar += f"{consulta}:\n {diagnostico}\n\n"
        return mostrar
