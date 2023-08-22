from urllib.request import urlopen

import webbrowser

import json

# store the URL in url variable as parameter for urlopen
url = "https://api.ipify.org/?format=json"

# store the response of URL
response = urlopen(url)

# storing the JSON response from url in data
data_json = json.loads(response.read())

# print the json response
print(data_json)

site = "https://ipinfo.io/data_json/geo"

webbrowser.open(site)