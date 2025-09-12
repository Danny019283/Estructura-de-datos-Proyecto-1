from Logica_de_negocio.Paciente import Paciente
from Logica_de_negocio.Personal import Personal
from Logica_de_negocio.Diagnostico import Diagnostico
from Logica_de_negocio.Consulta import Consulta

from Acceso_a_datos.Lista_Paciente import Lista_Paciente
from Acceso_a_datos.Cola_Emergencia import Cola_Emergencia
from Acceso_a_datos.Historial_Consultas import Historial_Consultas
from Acceso_a_datos.Jerarquia_Medica import Jerarquia_Medica

# =============================
# Inicialización de estructuras
# =============================
lista_pacientes = Lista_Paciente()
cola_emergencia = Cola_Emergencia()
historial = Historial_Consultas()
jerarquia = Jerarquia_Medica()

# Cargar jerarquía médica de ejemplo
jerarquia.insertar(Personal(1, "Director", "Director"))
jerarquia.insertar(Personal(2, "Jefe Área A", "Jefe"))
jerarquia.insertar(Personal(3, "Doctor 1", "Doctor"))
jerarquia.insertar(Personal(4, "Doctor 2", "Doctor"))
jerarquia.insertar(Personal(5, "Jefe Área B", "Jefe"))
jerarquia.insertar(Personal(6, "Doctor 3", "Doctor"))

#valida la entrada del usuario
def pedirDato(mensaje: str, tipoDeDato, mensajeError: str):
    while True:
        try:
            return tipoDeDato(input(mensaje))
        except ValueError:
            print(f"{mensajeError}. Intente de nuevo ")
            input("Presione ENTER ")
        except Exception as e:
            print(f"ERROR INESPERADO: {type(e).__name__}\nIntente una vez mas.")
            input("Presione ENTER")


def prioridad_label(n):
    return {1: "ALTA", 2: "MEDIA", 3: "BAJA"}.get(n, str(n))


def mostrar_menu():
    print("""
==========================================
   SISTEMA DE GESTIÓN HOSPITALARIA
==========================================
1. Registrar nuevo paciente
2. Mostrar lista de pacientes
3. Gestionar emergencias
   3.1. Agregar paciente a emergencias
   3.2. Atender paciente (según prioridad)
   3.3. Mostrar pacientes en espera
4. Consultas médicas
   4.1. Registrar nueva consulta
   4.2. Mostrar historial de consultas
   4.3. Deshacer última consulta (Undo)
5. Personal médico
   5.1. Mostrar jerarquía del hospital (Árbol)
   5.2. Agregar nuevo médico
9. Salir
==========================================
""")


def registrar_paciente():
    nombre = input("Ingrese nombre del paciente: ")
    cedula = int(input("Ingrese cédula: "))
    edad = int(input("Ingrese edad: "))
    fecha_ingreso = input("Ingrese fecha de ingreso (dd/mm/aaaa): ")
    paciente = Paciente(cedula, nombre, edad, fecha_ingreso)

    if lista_pacientes.insertar_pacientes(paciente):
        print("Paciente registrado correctamente.")
    else:
        print("El paciente ya estaba registrado.")


def mostrar_pacientes():
    pacientes = lista_pacientes.generar_estadis()
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        for p in pacientes:
            print(p)


def agregar_a_emergencias():
    cedula = int(input("Ingrese cédula del paciente: "))
    paciente = lista_pacientes.buscar_paciente(cedula)
    if paciente is None:
        print("Paciente no encontrado.")
        return

    diagnostico_desc = input("Ingrese diagnóstico: ")
    prioridad = int(input("Seleccione nivel de prioridad (1 = Alta, 2 = Media, 3 = Baja): "))
    diagnostico = Diagnostico(diagnostico_desc, prioridad, "hoy", paciente)

    if cola_emergencia.encolar_y_ordenar(diagnostico):
        print(f"Paciente {paciente.nombre} agregado a la cola de emergencias con prioridad {prioridad_label(prioridad)}.")
    else:
        print("El paciente ya está en la cola.")


def atender_paciente():
    elemento = cola_emergencia.atender()
    if elemento is None:
        print("No hay pacientes en emergencia.")
        return
    prioridad_num, diagnostico = elemento
    paciente = diagnostico.paciente
    print(f"Atendiendo a: {paciente.nombre} (Prioridad: {prioridad_label(prioridad_num)}) - {diagnostico.descripcion}")


    medico = Personal(999, "Médico de guardia", "Doctor")
    consulta = Consulta(paciente, medico)
    historial.empujar(consulta, diagnostico)
    print("Consulta registrada automáticamente en historial.")


def mostrar_espera():
    print(cola_emergencia)