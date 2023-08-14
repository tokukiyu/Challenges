
import requests

# Replace with your own API key and Search Engine ID
API_KEY = 'AIzaSyASp4ppfcqDP7qU1f3w0lplea2wN6okqls'
SEARCH_ENGINE_ID = '87de6d4157d0e4220'

# Search query
search_query = input("Enter search query: ")

# API endpoint
url = f'https://www.googleapis.com/customsearch/v1'

# Parameters for the API request
params = {
    'key': API_KEY,
    'cx': SEARCH_ENGINE_ID,
    'q': search_query,
    'num': 10 , # Number of results
      'searchType': 'image'
}

# Make the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    items = data.get('items', [])

    if items:
        for item in items:
            title = item.get('title')
            link = item.get('link')
            print(f'Title: {title}')
            print(f'Link: {link}')
            print('-' * 40)
    else:
        print('No results found.')
else:
    print('Request failed. Check your API key and Search Engine ID.')

