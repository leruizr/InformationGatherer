import json
import ConfigurationHelper
from azure.storage.filedatalake import DataLakeServiceClient

def StoreJsonResult(result, directory, filename):

    configuration = ConfigurationHelper.get_configuration()

    # Replace these values with your Azure Storage account and Data Lake Storage Gen2 details
    account_name = configuration["storageAccountName"]
    account_key = configuration["storageAccountKey"]
    file_system_name = configuration["storageAccountFileSystemName"]
    base_directory = directory
    file_name = filename

    # Create a DataLakeServiceClient using the storage account and account key
    service_client = DataLakeServiceClient(account_url=f"https://{account_name}.dfs.core.windows.net", credential=account_key)

    # Get a reference to the file system
    file_system_client = service_client.get_file_system_client(file_system_name)

    # Get a reference to the file
    file_client = file_system_client.get_file_client(base_directory + '/' + file_name)

    # Convert the result list to JSON and write it to the file
    #result_json = json.dumps(result, indent=2)  # Stores ascii characters escaped
    result_json = json.dumps(result, indent=2, ensure_ascii=False)
    result_bytes = result_json.encode('utf-8')
    file_client.create_file()
    file_client.append_data(data=result_bytes, offset=0, length=len(result_bytes))
    file_client.flush_data(len(result_bytes))

    print("Results stored in Azure Data Lake Storage Gen2 in a single file.")