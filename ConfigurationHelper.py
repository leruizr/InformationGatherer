# Importar los módulos necesarios para trabajar con archivos JSON y rutas
import json
import os


# Definir una función para obtener la configuración desde un archivo JSON
def get_configuration():
    """Lee y devuelve la configuración del archivo ``config.json``.

    Se usa una ruta basada en la ubicación del módulo para evitar errores
    cuando el programa se ejecuta desde distintos directorios.
    """

    # Obtener la ruta absoluta del archivo de configuración
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')

    # Abrir el archivo en modo lectura con la codificación adecuada
    with open(config_path, encoding='utf-8') as config_file:
        # Cargar los datos del archivo JSON en una estructura de datos de Python
        data = json.load(config_file)

    # Devolver los datos cargados como resultado de la función
    return data
