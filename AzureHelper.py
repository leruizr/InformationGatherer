# Importar los módulos necesarios
import json  # Para trabajar con archivos JSON
import ConfigurationHelper  # Módulo personalizado para obtener la configuración
from azure.storage.filedatalake import DataLakeServiceClient  # Cliente para interactuar con Azure Data Lake Storage Gen2

# Definir una función para almacenar un resultado en formato JSON en Azure Data Lake Storage Gen2
def StoreJsonResult(result, directory, filename):
    # Obtener la configuración del programa
    configuration = ConfigurationHelper.get_configuration()

    # Obtener las credenciales y detalles de almacenamiento de Azure desde la configuración
    account_name = configuration["storageAccountName"]
    account_key = configuration["storageAccountKey"]
    file_system_name = configuration["storageAccountFileSystemName"]
    base_directory = directory
    file_name = filename

    # Crear un cliente de servicio para interactuar con Azure Data Lake Storage Gen2
    service_client = DataLakeServiceClient(account_url=f"https://{account_name}.dfs.core.windows.net", credential=account_key)

    # Obtener una referencia al sistema de archivos
    file_system_client = service_client.get_file_system_client(file_system_name)

    # Obtener una referencia al archivo
    file_client = file_system_client.get_file_client(base_directory + '/' + file_name)

    # Convertir la lista de resultados a formato JSON y escribirlo en el archivo
    # result_json = json.dumps(result, indent=2)  # Almacena caracteres ASCII escapados
    result_json = json.dumps(result, indent=2, ensure_ascii=False)  # No escapa caracteres ASCII
    result_bytes = result_json.encode('utf-8')
    
    # Crear el archivo en Azure Data Lake Storage Gen2
    file_client.create_file()
    
    # Anexar los datos al archivo
    file_client.append_data(data=result_bytes, offset=0, length=len(result_bytes))
    
    # Finalizar la escritura de datos en el archivo
    file_client.flush_data(len(result_bytes))

    print("Resultados almacenados en Azure Data Lake Storage Gen2 en un solo archivo.")
