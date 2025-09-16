class Jerarquia_Medica:
    def __init__(self):
        self.__arbol_puesto = None

    def obtener_jerarquia(self, puesto):
        dicc_jerarquia = {"Residente": 1, "Doctor": 2, "Jefe de Area": 3, "Director": 4}
        return dicc_jerarquia[puesto]

    def construir_arbol(self, dicc):
        #crea un arbol ABB
        def _insertar(arbol, nuevo):
            if arbol is None:
                return nuevo, None, None
            medico, izq, der = arbol
            print(nuevo.puesto)
            if self.obtener_jerarquia(nuevo.puesto) < self.obtener_jerarquia(arbol[0].puesto):
                return medico, _insertar(izq, nuevo), der
            else:
                return medico, izq, _insertar(der, nuevo)
        #agrega los medicos la arbol
        for med in dicc.values():
            self.__arbol_puesto = _insertar(self.__arbol_puesto, med)

    def mostrar_jerarquia(self):
        def _mostrar(arbol):
            if arbol is None:
                return ""
            jerarquia = ""
            #verifica la jerarquia para dar el formato
            if self.obtener_jerarquia(arbol[0].puesto) == 3:
                jerarquia += f" |_"
            if self.obtener_jerarquia(arbol[0].puesto) == 2:
                jerarquia += f"     |_"
            if self.obtener_jerarquia(arbol[0].puesto) == 1:
                jerarquia += f"         |_"

            jerarquia += f"{arbol[0].puesto}\n"

            #recorre el arbol
            if arbol[1]:
                jerarquia += f"{_mostrar(arbol[1])}"
            if arbol[2]:
                jerarquia += f"{_mostrar(arbol[2])}"
            return jerarquia

        return _mostrar(self.__arbol_puesto)

    def __str__(self):
        return self.mostrar_jerarquia() or "Jerarquía medica vacia"




