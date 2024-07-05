import json
import requests as rq

url="http://api.open-notify.org/iss-now.json"

headers={

 "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"

}

data = rq.get(url).json()
print(f'Latitude: {data["iss_position"]["latitude"]}')
print(f'Longitude: {data["iss_position"]["longitude"]}')
print(f'Timestamp: {data["timestamp"]}')