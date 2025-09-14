from Modelo import Personal

class NodoArbol:
    def __init__(self, personal: Personal):
        self.personal = personal
        self.izq = None
        self.der = None

    def __str__(self):
        return str(self.personal)


class Jerarquia_Medica:
    def __init__(self):
        self.__arbol_personal = None

    def insertar(self, personal: Personal):
        def _insertar(nodo, nuevo):
            if nodo is None:
                return NodoArbol(nuevo)
            if nuevo.cedula < nodo.personal.cedula:
                nodo.izq = _insertar(nodo.izq, nuevo)
            elif nuevo.cedula > nodo.personal.cedula:
                nodo.der = _insertar(nodo.der, nuevo)
            return nodo

        self.__arbol_personal = _insertar(self.__arbol_personal, personal)

    def buscar(self, cedula: int):
        def _buscar(nodo, cedula):
            if nodo is None:
                return None
            if cedula == nodo.personal.cedula:
                return nodo.personal
            elif cedula < nodo.personal.cedula:
                return _buscar(nodo.izq, cedula)
            else:
                return _buscar(nodo.der, cedula)

        return _buscar(self.__arbol_personal, cedula)

    def borrar(self, cedula: int):
        def _min_value_node(nodo):
            actual = nodo
            while actual.izq is not None:
                actual = actual.izq
            return actual

        def _borrar(nodo, cedula):
            if nodo is None:
                return nodo
            if cedula < nodo.personal.cedula:
                nodo.izq = _borrar(nodo.izq, cedula)
            elif cedula > nodo.personal.cedula:
                nodo.der = _borrar(nodo.der, cedula)
            else:
                if nodo.izq is None and nodo.der is None:
                    return None
                elif nodo.izq is None:
                    return nodo.der
                elif nodo.der is None:
                    return nodo.izq
                temp = _min_value_node(nodo.der)
                nodo.personal = temp.personal
                nodo.der = _borrar(nodo.der, temp.personal.cedula)
            return nodo
        self.__arbol_personal = _borrar(self.__arbol_personal, cedula)

    def mostrar_jerarquia(self):
        def _mostrar(nodo, nivel=0):
            if nodo is None:
                return ""
            resultado = "   " * nivel + str(nodo.personal) + "\n"
            resultado += _mostrar(nodo.izq, nivel + 1)
            resultado += _mostrar(nodo.der, nivel + 1)
            return resultado

        return _mostrar(self.__arbol_personal)

    def __str__(self):
        return self.mostrar_jerarquia() or "Jerarquía medica vacia"
