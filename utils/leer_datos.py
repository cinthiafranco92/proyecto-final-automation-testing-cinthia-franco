import json
import os


RUTA_JSON = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "usuarios.json"
)


def cargar_usuarios():
    with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
        return json.load(archivo)