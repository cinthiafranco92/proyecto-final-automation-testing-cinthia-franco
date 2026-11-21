
import logging
from pathlib import Path


CARPETA_LOGS = Path(__file__).parent.parent / "logs"
CARPETA_LOGS.mkdir(parents=True, exist_ok=True)

RUTA_LOG = CARPETA_LOGS / "automation.log"


def obtener_logger(nombre):
    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formato = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        archivo = logging.FileHandler(
            RUTA_LOG,
            encoding="utf-8"
        )
        archivo.setFormatter(formato)

        logger.addHandler(archivo)

    return logger