import requests
import AzureHelper
import ConfigurationHelper
from datetime import datetime, timedelta

current_year = datetime.now().year
current_month = datetime.now().month
current_year_month = f"{current_year:04d}-{current_month:02d}"
current_datetime = datetime.now()
seven_days_ago_name = (current_datetime - timedelta(days=7)).strftime("%Y-%m-%d")
file_name = current_datetime.strftime("%Y-%m-%d_%H-%M-%S.json")
configuration = ConfigurationHelper.get_configuration()

def getNewsInformation():

    serviceUrl = configuration["newsApiurl"]
    apiKey = configuration["apiKey"]

    # Construct the JSON body
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
        "lang" : "spa",
        "dateStart" : seven_days_ago_name,
        "categoryUri" : ["news/Health", "news/Business"]
    }

    # Make the API request
    try:
        response = requests.post(serviceUrl, json=json_body)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            return data
            # Process the response data as needed
            # print(json.dumps(data, indent=2))
        else:
            print(f"API request failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Error making API request: {e}")


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

def main():

    # get information from API
    newsApiData = getNewsInformation()

    # Extracting relevant fields
    formattedNewsApiData = extractNewsInformation(newsApiData)
    
    # Store result on Azure
    AzureHelper.StoreJsonResult(formattedNewsApiData, current_year_month, file_name)

if __name__ == "__main__":
    main()