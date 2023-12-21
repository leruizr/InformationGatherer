# Importar los módulos necesarios
import requests  # Para realizar solicitudes HTTP
import AzureHelper  # Módulo personalizado para interactuar con Azure
import ConfigurationHelper  # Módulo personalizado para obtener la configuración
from datetime import datetime, timedelta  # Para trabajar con fechas y horas

# Obtener el año y el mes actuales
current_year = datetime.now().year
current_month = datetime.now().month

# Crear una cadena de texto con el año y mes actuales en formato "YYYY-MM"
current_year_month = f"{current_year:04d}-{current_month:02d}"

# Obtener la fecha y hora actuales
current_datetime = datetime.now()

# Obtener el nombre de la fecha siete días atrás en formato "YYYY-MM-DD"
seven_days_ago_name = (current_datetime - timedelta(days=7)).strftime("%Y-%m-%d")

# Crear un nombre de archivo en formato "YYYY-MM-DD_HH-MM-SS.json"
file_name = current_datetime.strftime("%Y-%m-%d_%H-%M-%S.json")

# Obtener la configuración del programa
configuration = ConfigurationHelper.get_configuration()

# Definir una función para obtener información de noticias
def getNewsInformation():
    # Obtener la URL del servicio y la clave API de la configuración
    serviceUrl = configuration["newsApiurl"]
    apiKey = configuration["apiKey"]

    # Construir el cuerpo JSON para la solicitud
    json_body = {
        "action": "getArticles",
        "keyword": ["Colombia", "Latinoamerica"],
        "articlesPage": 1,
        "articlesCount": 100,
        "articlesSortBy": "date",
        "articlesSortByAsc": False,
        "articlesArticleBodyLen": -1,
        "resultType": "articles",
        "dataType": ["news", "pr"],
        "apiKey": apiKey,
        "forceMaxDataTimeWindow": 7,
        "lang": "spa",
        "dateStart": seven_days_ago_name,
        "categoryUri": ["news/Health", "news/Business"]
    }

    # Realizar la solicitud a la API
    try:
        response = requests.post(serviceUrl, json=json_body)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            data = response.json()
            return data
            # Procesar los datos de respuesta según sea necesario
            # print(json.dumps(data, indent=2))
        else:
            print(f"Solicitud a la API fallida con código de estado: {response.status_code}")
    except Exception as e:
        print(f"Error al realizar la solicitud a la API: {e}")

# Definir una función para extraer información relevante de las noticias
def extractNewsInformation(data):
    result = []
    for article in data['articles']['results']:
        extracted_data = {
            'date': article['date'],
            'dateTimePub': article['dateTimePub'],
            'dataType': article['dataType'],
            'url': article['url'],
            'title': article['title'],
            'body': article['body'],
            'source_uri': article['source']['uri']
        }
        result.append(extracted_data)
    return result

# Función principal del programa
def main():
    # Obtener información de la API de noticias
    newsApiData = getNewsInformation()

    # Extraer campos relevantes
    formattedNewsApiData = extractNewsInformation(newsApiData)
    
    # Almacenar el resultado en Azure
    AzureHelper.StoreJsonResult(formattedNewsApiData, current_year_month, file_name)

# Ejecutar la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()
