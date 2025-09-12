class Historial_Consultas:
    def __init__(self):
        self.__pila_consultas = []

    def empujar(self, consulta, diagnostico=None):
        self.__pila_consultas.append((consulta, diagnostico))
        return True

    def deshacer_ult_cons(self):
        if self.esta_vacia():
            return None
        return self.__pila_consultas.pop()

    def mostrar_historial(self):
        return list(reversed(self.__pila_consultas))

    def esta_vacia(self):
        return len(self.__pila_consultas) == 0

    def __len__(self):
        return len(self.__pila_consultas)

    def __str__(self):
        if self.esta_vacia():
            return "Historial vacío"
        lines = []
        for consulta, diagnostico in reversed(self.__pila_consultas):
            try:
                paciente_nombre = consulta.paciente.nombre
            except Exception:
                paciente_nombre = str(consulta)
            if diagnostico is not None:
                prio_map = {1: "ALTA", 2: "MEDIA", 3: "BAJA"}
                prio_label = prio_map.get(diagnostico.gravedad, str(diagnostico.gravedad))
                lines.append(f"- {paciente_nombre} ({diagnostico.descripcion}) [Prioridad {prio_label}]")
            else:
                lines.append(f"- {paciente_nombre} (consulta sin diagnóstico registrado)")
        return "\n".join(lines)