# Importar el módulo json para trabajar con archivos JSON
import json

# Definir una función para obtener la configuración desde un archivo JSON
def get_configuration():
    # Abrir el archivo 'config.json' en modo lectura
    with open('config.json') as config_file:
        # Cargar los datos del archivo JSON en una estructura de datos de Python
        data = json.load(config_file)
        # Devolver los datos cargados como resultado de la función
        return data
