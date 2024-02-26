# InformationGatherer

Este proyecto utiliza NewsApi para obtener noticias relevantes para SURA y luego almacena esa información en servicios de Azure.

## PASOS PARA EJECUTAR EL CÓDIGO:

### 1. Configuración:

Antes de ejecutar el código, asegúrate de completar el archivo de configuración `config.json` con la información correcta, incluyendo claves API y detalles de almacenamiento de Azure.

- `"newsApiurl"`: La URL del servicio de la API de noticias que se utilizará para realizar solicitudes.
- `"apiKey"`: La clave API necesaria para autenticar y realizar solicitudes a la API de noticias.
- `"storageAccountName"`: El nombre de la cuenta de almacenamiento de Azure donde se almacenarán los resultados. 
- `"storageAccountKey"`: La clave de acceso de la cuenta de almacenamiento de Azure. 
- `"storageAccountFileSystemName"`: El nombre de la carpeta en la cuenta de almacenamiento de Azure donde se almacenarán los resultados. 

Para obtener la API KEY, primero debes registrarte en la API. Puedes hacerlo en [este enlace](https://newsapi.ai/).

Para obtener más información sobre cómo consumir la API con Python, puedes revisar el [repositorio](https://github.com/EventRegistry/event-registry-python/wiki).

### 2. Instalar dependencias: 

Asegúrate de tener las bibliotecas necesarias instaladas. Puedes hacerlo ejecutando `pip install -r requirements.txt`. Este archivo contiene la lista de dependencias necesarias junto con sus respectivas versiones.

### 3. Ejecutar:

Ejecuta el script principal `NewsApiGatherer.py` en tu entorno de ejecución de Python.

### 4. Resultados:

Los resultados se obtendrán de la API de noticias, se procesarán y se almacenarán en un archivo JSON en Azure Data Lake Storage Gen2.
