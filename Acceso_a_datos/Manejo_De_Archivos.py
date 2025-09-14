import pickle
import os

class Manejo_De_Archivos:
    def __init__(self):
        pass

    @staticmethod
    def _ruta_archivo(nombre):
        # Carpeta datos en la raíz del proyecto
        base_dir = os.path.dirname(os.path.dirname(__file__))  # sube un nivel desde Control/
        datos_dir = os.path.join(base_dir, "datos")
        os.makedirs(datos_dir, exist_ok=True)  # crear carpeta si no existe
        return os.path.join(datos_dir, f"{nombre}.pkl")

    @staticmethod
    def guardar_datos(nombre ,lista):
        ruta = Manejo_De_Archivos._ruta_archivo(nombre)
        with open(ruta, "wb") as f:
            pickle.dump(lista, f)

    @staticmethod
    def cargar_datos(nombre):
        ruta = Manejo_De_Archivos._ruta_archivo(nombre)
        try:
            with open(ruta, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            with open(ruta, "wb") as f:
                pickle.dump([], f)
                return []