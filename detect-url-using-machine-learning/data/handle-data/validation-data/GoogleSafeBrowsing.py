# double check the reliability of the dataset by calling google api (Google Safe Browsing for free) to validation
# or can use Webrisk API if you well-off 
from pysafebrowsing import SafeBrowsing
from dotenv import load_dotenv
import os
import pandas as pd
load_dotenv() # Load environment variables from .env file


API_KEY = os.environ.get('API_KEY')  # should put api key in environment variable
LIST_API_KEY = os.environ.get('LIST_API_KEY')
def check_url(url, api_key):
  s = SafeBrowsing(api_key)
  try: 
    # sample result format: dict_values([{'malicious': True, 'platforms': ['ANY_PLATFORM'], 'threats': ['MALWARE'], 'cache': '300s'}]) 
    r = list(s.lookup_urls([url]).values()) # true/false 
    print("url: ", url, "check: ",r[0]['malicious'])
    return r[0]['malicious'] 
  except Exception as e:
    print(f"Error checking URL {url}: {e}") 
    return False


def main():
  current_directory = os.getcwd()
  data_path = os.path.join(current_directory, 'data/processed/extracted_dataset.csv')
  data = pd.read_csv(data_path)
  print(data.head(5))
  # if you have money use Web risk API, you can call without dividing the number of api calls
  # check and add new column to save result
  # data['GoogleSafebrowsing'] = data['url'].apply(check_url) # only this 1 row for all if you have money :))))
  # or------------------------------------------------------------------------------------------
  # Because safe browsing only supports 10k quotas per day, use 10 api keys to loop through, the total will be 100k query lookup api
  # Split DataFrame into 10k row blocks
  chunk_size = 10000 
  chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

  results = []
  current_api_key_index = 0 

  for chunk in chunks:
    # Use current API key for this data block
    current_api_key = LIST_API_KEY[current_api_key_index] 
    print("current_api_key_index::: ", current_api_key_index, "api_key: ", current_api_key)
    chunk['GoogleSafebrowsing'] = chunk['url'].apply(lambda x: check_url(x, current_api_key)) 
    results.append(chunk) 
    current_api_key_index = (current_api_key_index + 1) % len(LIST_API_KEY)

  # Combine data blocks
  data = pd.concat(results)
  print(data.head(10))
  # or------------------------------------------------------------------------------------------
  new_path = os.path.join(current_directory, 'data/processed/google_checked.csv')
  data.to_csv(new_path, index=False)
if __name__ == '__main__':
  main()