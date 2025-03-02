# import requests
# from bs4 import BeautifulSoup
# import os
# import pandas as pd
# def check_url_bitdefender(url):
#     # Bitdefender Link Checker URL
#     bitdefender_url = 'https://www.bitdefender.com/toolbox/checker/'

#     # Payload sent to Bitdefender site
#     payload = {'url': url}

#     # Send POST request to Bitdefender Link Checker
#     response = requests.post(bitdefender_url, data=payload)

#     # Check response from Bitdefender
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         # Find the result in the HTML content of the response
#         result = soup.find('div', {'class': 'result'})
#         if result:
#             print(result.text.strip())
#             return result.text.strip()
#         else:
#             return 'No results found'
#     else:
#         return f'Error Check response from Bitdefender::: {response.status_code}'

# def main():
#     current_directory = os.getcwd()
#     data_path = os.path.join(current_directory, 'data/processed/new-dataset.csv')
#     data = pd.read_csv(data_path)
#     print(data.head(5))
#     # check and add new column to save result
#     data['Bitdefender'] = data['url'].apply(check_url_bitdefender)
    
#     print(data.head(10))
#     new_path = os.path.join(current_directory, 'data/processed/dataset-double-checked.csv')
#     data.to_csv(new_path, index=False)

# if __name__ == '__main__':
#     main()
