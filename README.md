# InformationGatherer

Consumo NewsApi para obtener noticias de interes para SURA y almacenamiento de la informacion en servicios de azure.

PASOS PARA EJECUTAR EL CODIGO:

1. Configuración:

Antes de ejecutar el código, completa el archivo de configuración (config.json) con la información correcta, incluyendo claves API y detalles de almacenamiento de Azure.

"newsApiurl": La URL del servicio de la API de noticias que se utilizará para realizar solicitudes.
"apiKey": La clave API necesaria para autenticar y realizar solicitudes a la API de noticias.
"storageAccountName": El nombre de la cuenta de almacenamiento de Azure donde se almacenarán los resultados. 
"storageAccountKey": La clave de acceso de la cuenta de almacenamiento de Azure. 
"storageAccountFileSystemName": El nombre de la carpeta en la cuenta de almacenamiento de Azure donde se almacenarán los resultados. 

Para esto primero que todo se debe registrar en la API para obtener la API KEY la url es la siguiente:
https://newsapi.ai/

https://github.com/EventRegistry/event-registry-python/wiki = repositorio con informacion para consumo de la API con python.

De igual forma en la misma pueden verificar la documentación de la API en caso de que requieran realizar algun cambio en la petición o respuesta.

la informacion que va en el archivo cofig.json es la siguiente :


2. Instalar dependencias: 

Asegúrate de tener las bibliotecas necesarias instaladas, puedes hacerlo ejecutando pip install requests azure-storage-file-datalake.
Para tener claras las dependencias que se instalaron puede verificar el archivo requeriments.txt en donde esta la lista con la respectiva version.


3. Ejecutar:

Ejecuta el script principal (NewsApiGatherer.py) en tu entorno de ejecución de Python.


4. Resultados:

Los resultados se obtendrán de la API de noticias, se procesarán y se almacenarán en un archivo JSON en Azure Data Lake Storage Gen2.