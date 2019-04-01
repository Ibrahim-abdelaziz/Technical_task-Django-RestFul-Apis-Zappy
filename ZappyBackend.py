import urllib.parse
import requests

main_api = "http://127.0.0.1:8000/zappy_app/"

message = 'how to go anywhere'

url = main_api + urllib.parse.urlencode({'message':message})

json_data = requests.get(main_api).json()

print(json_data)

