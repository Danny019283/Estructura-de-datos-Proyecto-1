from sqlalchemy.sql.operators import truediv

from Modelo.Paciente import Paciente
from Modelo.Personal import Personal
from Modelo.Diagnostico import Diagnostico
from Modelo.Consulta import Consulta

from Acceso_a_datos.Lista_Paciente import Lista_Paciente
from Acceso_a_datos.Cola_Emergencia import Cola_Emergencia
from Acceso_a_datos.Historial_Consultas import Historial_Consultas
from Acceso_a_datos.Jerarquia_Medica import Jerarquia_Medica

from datetime import datetime

#DEFINICON DE CLASE SISTEMA
class Sistema():
# =============================
# Inicialización de estructuras
# =============================
    def __init__(self):
        self.__lista_pacientes = Lista_Paciente()
        self.__cola_emergencia = Cola_Emergencia()
        self.__historial = Historial_Consultas()
        self.__jerarquia = Jerarquia_Medica()
        self.__PRIORIDAD = {
        1: "ALTA",
        2: "MEDIA",
        3: "BAJA"
        }

        # Cargar jerarquía médica de ejemplo
        self.__jerarquia.insertar(Personal(1, "Director", "Director"))
        self.__jerarquia.insertar(Personal(2, "Jefe Área A", "Jefe de Area"))
        self.__jerarquia.insertar(Personal(3, "Doctor 1", "Doctor"))
        self.__jerarquia.insertar(Personal(4, "Doctor 2", "Doctor"))
        self.__jerarquia.insertar(Personal(5, "Jefe Área B", "Jefe de Area"))
        self.__jerarquia.insertar(Personal(6, "Resi", "Residente"))


# valida la entrada del usuario
    def pedir_dato(self, mensaje: str, tipoDeDato, mensajeError: str):
        while True:
            try:
                return tipoDeDato(input(mensaje))
            except ValueError:
                print(f"{mensajeError}. Intente de nuevo ")
                input("Presione ENTER ")
            except Exception as e:
                print(f"ERROR INESPERADO: {type(e).__name__}\nIntente una vez mas.")
                input("Presione ENTER")

    def validar_rango(self, min, max, mensaje):
        while True:
            dato = self.pedir_dato(mensaje, int, "El dato ingresado debe ser un numero entero")
            if dato >= min and dato <= max:
                return dato
            else:
                print(f"el dato debe estar entre {min} y {max}")


    def mostrar_menu(self):
        print("""
    ==========================================
       SISTEMA DE GESTIÓN HOSPITALARIA
    ==========================================
    1. Registrar nuevo paciente
    2. Mostrar lista de pacientes
    3. Gestionar emergencias
    4. Consultas médicas
    5. Personal médico
    6. Pacientes – Ordenamiento y reportes
    7. Salir
    ==========================================
    """)

    def mostrar_menu_gestion_em(self):
        print("""
    ==========================================
            GESTION DE EMERGENCIAS
    ==========================================
    1. Agregar paciente a emergencias
    2. Atender paciente (según prioridad)
    3. Mostrar pacientes en espera
    4. Menu principal
    """)

    def mostrar_menu_consultas(self):
        print("""
    ==========================================
                CONSULTAS MEDICAS
    ==========================================   
    1. Registrar nueva consulta
    2. Mostrar historial de consultas
    3. Deshacer última consulta (Undo)
    4. Menu principal
    """)

    def mostrar_menu_personal(self):
        print("""
    ==========================================
                PERSONAL MEDICO
    ==========================================   
    1. Mostrar jerarquía del hospital (Árbol)
    2. Agregar nuevo médico
    3. Menu Principal
    """)

    def mostrar_menu_reportes(self):
        print("""
    ==========================================
                    REPORTES
    ==========================================
    1. Ordenar pacientes por edad (insertion sort)
    2. Ordenar pacientes por fecha de ingreso (merge sort)
    3. Generar estadísticas (recursividad)
    4. Menu principal
    """)



    def registrar_paciente(self):
        nombre = input("Ingrese nombre del paciente: ")
        cedula = self.pedir_dato("Ingrese la cedula del paciente: ", int, "el dato ingresado debe ser un numero entero")
        edad = self.validar_rango(0, 120, "Ingrese la edad del paciente: ")
        fecha_ingreso = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
        paciente = Paciente(cedula, nombre, edad, fecha_ingreso)

        if self.__lista_pacientes.insertar_pacientes(paciente):
            print("Paciente registrado correctamente.")
        else:
            print("El paciente ya estaba registrado.")


    def mostrar_pacientes(self):
        print(self.__lista_pacientes)


    def registrar_emergencia(self):
        id = self.pedir_dato("Ingrese la cedula del paciente: ", int, "El dato ingresado debe ser un numero entero")
        paciente = self.__lista_pacientes.buscar_paciente(id)
        if paciente is None:
            print("El paciente no existe")
        else:
            descrip_diag = input("Ingrese diagnóstico: ")
            prioridad = self.validar_rango(1, 3, "Seleccione nivel de prioridad (1 = Alta, 2 = Media, 3 = Baja): ")
            fecha = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
            diagnostico = Diagnostico(descrip_diag, prioridad, fecha, paciente)

            if self.__cola_emergencia.encolar_y_ordenar(diagnostico):
                print("paciente exitosamente agregado a la cola de emergencias.")
            else:
                print("El paciente ya está en la cola.")


    def atender_paciente(self):
        #paciente = (prioridad, diagnostico)
        paciente = self.__cola_emergencia.atender()
        if paciente is None:
            print("No hay pacientes en emergencia.")
            return
        print(f"Atendiendo a: {paciente[1].paciente.nombre} (Prioridad: {self.__PRIORIDAD.get(paciente[0])}")

        medico = Personal(999, "Médico de guardia", "Doctor")
        consulta = Consulta(paciente, medico)
        self.__historial.empujar(consulta, paciente[1])
        print("Consulta registrada automáticamente en historial.")


    def mostrar_espera(self):
        print(self.__cola_emergencia)

    def registrar_consulta(self):
        cedula = self.pedir_dato("Ingrese la cedula del paciente: ", int, "El dato ingresado debe ser un numero entero")
        paciente = self.__lista_pacientes.buscar_paciente(cedula)
        if paciente is None:
            print("Paciente no encontrado.")
        else:
            medico = Personal(888, "Doctor General", "Doctor")
            consulta = Consulta(paciente, medico)
            descripcion = input("Diagnóstico: ")
            prioridad = self.validar_rango(1, 3, "Seleccione nivel de prioridad (1 = Alta, 2 = Media, 3 = Baja): ")
            fecha = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
            diagnostico = Diagnostico(descripcion, prioridad, fecha, paciente)
            self.__historial.empujar(consulta, diagnostico)
            print("Consulta registrada.")


    def mostrar_historial(self):
        print(self.__historial)


    def deshacer_ultima(self):
        deshecho = self.__historial.deshacer_ult_cons()
        if deshecho:
            print("Consulta eliminada del historial.")
        else:
            print("No hay consultas para deshacer.")


    def mostrar_jerarquia(self):
        print(self.__jerarquia)


    def agregar_medico(self):
        cedula = self.pedir_dato("Ingrese la cedula del medico: ", int, "El dato ingresado debe ser un numero entero")
        nombre = input("Nombre: ")
        print("""1. Residente
        2. Doctor
        3. Jefe de Area
        4. Director
        """)
        puesto = self.validar_rango(1, 4, "Ingrese una opcion: ")
        medico = Personal(cedula, nombre, puesto)
        self.__jerarquia.insertar(medico)
        print("Médico agregado.")

    def asignar_puesto(self, eleccion):
        dicc_puesto = {1: "Residente", 2: "Doctor", 3: "Jefe de Area", 4: "Director"}
        return dicc_puesto[eleccion]


    def estadisticas_recursivas(self):
        edad_promedio = self.__lista_pacientes.edad_promedio()
        if edad_promedio == 0:
            print("No hay pacientes registrados")
        else:
            print(f"La edad promedio de los Pacientes es: {edad_promedio}")
        consl_ultimo_mes = self.__historial.consultas_ultimo_mes()
        if consl_ultimo_mes == 0:
            print("No hay consultas registradas el ultimo mes")
        else:
            print(f"Consultas el ultimo mes: {consl_ultimo_mes}")


    # === Bucle principal ===
    def menu_principal(self):
        while True:
            self.mostrar_menu()
            opcion = input("Ingrese una opción: ").strip()

            if opcion == "1":
                self.registrar_paciente()
            elif opcion == "2":
                self.mostrar_pacientes()
            elif opcion == "3":
                self.menu_gestion_emergencias()
            elif opcion == "4":
                self.menu_consult_medicas()
            elif opcion == "5":
                self.menu_personal_medico()
            elif opcion == "6":
                self.menu_orden_y_reportes()
            elif opcion == "7":
                print("Saliendo...")
                break
            else:
                print("Opción no válida.")\

    def menu_gestion_emergencias(self):
        while True:
            self.mostrar_menu_gestion_em()
            opc = input("Ingrese opción: ").strip()
            if opc == "1":
                self.registrar_emergencia()
            elif opc == "2":
                self.atender_paciente()
            elif opc == "3":
                print(self.__cola_emergencia)
            elif opc == "4":
                print("Saliendo...")
                break

    def menu_consult_medicas(self):
        while True:
            self.mostrar_menu_consultas()
            opc = input("Ingrese una opción: ").strip()
            if opc == "1":
                self.registrar_consulta()
            elif opc == "2":
                self.mostrar_historial()
            elif opc == "3":
                self.deshacer_ultima()
            elif opc == "4":
                print("Saliendo...")
                break
            else:
                print("Opcion no valida.")

    def menu_personal_medico(self):
        while True:
            self.mostrar_menu_personal()
            opc = input("Ingrese una opción: ").strip()
            if opc == "1":
                self.mostrar_jerarquia()
            elif opc == "2":
                self.agregar_medico()
            elif opc == "3":
                print("Saliendo...")
                break
            else:
                print("Opcion no valida.")

    def menu_orden_y_reportes(self):
        while True:
            self.mostrar_menu_reportes()
            opc = input("Ingrese una opción: ").strip()
            if opc == "1":
                self.__lista_pacientes.ordenar_edad_insercion()
                print(self.__lista_pacientes)
            elif opc == "2":
                self.__lista_pacientes.ordenar_fecha_mergesort()
                print(self.__lista_pacientes)
            elif opc == "3":
                self.estadisticas_recursivas()
            elif opc == "4":
                print("Saliendo...")
                break
            else:
                print("Opcion no valida.")

if __name__ == "__main__":
    Sistema = Sistema()
    Sistema.menu_principal()