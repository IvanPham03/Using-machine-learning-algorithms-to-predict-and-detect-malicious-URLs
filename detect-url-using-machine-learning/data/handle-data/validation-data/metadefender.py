import requests

url = "https://api.criminalip.io/v1/domain/quick/malicious/view?domain=example.com"

payload={}

headers = {
  "x-api-key": "<YOUR_API_KEY>"
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)