import requests
from pprint import pprint

URL = "http://127.0.0.1:2224/"

#Sending get requests to the flask api
resp = requests.get(URL)

#Pretty printing the json response
pprint(resp.json())