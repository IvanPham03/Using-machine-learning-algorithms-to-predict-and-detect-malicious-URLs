# double check the reliability of the dataset by calling google api (Google Safe Browsing for free) to validation
# or can use Webrisk API if you well-off 
from pysafebrowsing import SafeBrowsing

API_KEY="AIzaSyBIZSl5N1k2d3HSewCEtc-WgrxIXf2nHwM"
def check_url(url):
    try:
        # Initialize the SafeBrowsing object with the API key
        s = SafeBrowsing(API_KEY)

        # Lookup the URL and retrieve results
        result = s.lookup_urls([url]).get(url, None)

        if result is None:
            print(f"URL {url} returned no result from the API.")
            return False
        print(result)
        # Extract the 'malicious' flag
        is_malicious = result.get('malicious', False)
        print(f"URL: {url}, Malicious: {is_malicious}")
        return is_malicious
    except Exception as e:
        print(f"Error checking URL {url}: {e}")
        return False



def main():
  test = check_url("https://github.com/ShubhamJagtap2000/Networking-Essentials")
  print(test)
if __name__ == '__main__':
  main()