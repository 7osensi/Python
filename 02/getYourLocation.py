from urllib.request import urlopen
import webbrowser
import json

# # store the URL in url variable as parameter for urlopen
# ip_url = "https://api.ipify.org/?format=json"

# # store the response of URL
# response1 = urlopen(ip_url)

# # Storing the JSON response from url and store it in ip
# ip = json.loads(response1.read())

# print(ip['ip'])

location_url = "https://ipapi.co/json/"

# store the response of URL
response2 = urlopen(location_url)

# Storing the JSON response from url and store it in ip
location = json.loads(response2.read())

# print the json response (ip)
print(location['ip'])
print(location['country_name'])
print(location['city'])