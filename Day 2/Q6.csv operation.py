import pandas as pd
import requests as rq
import time as t

url = "http://api.open-notify.org/iss-now.json"

header={
    
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

data_list = []

max_retries = 3
retry_delay = 5  

try:
    for i in range(101):
        attempt = 0
        while attempt < max_retries:
            try:
                response = rq.get(url, timeout=5) 
                response.raise_for_status()
                req_data = response.json()

                timestamp = req_data['timestamp']
                latitude = req_data['iss_position']['latitude']
                longitude = req_data['iss_position']['longitude']

                data_list.append([timestamp, latitude, longitude])

                print(f"Data added for iteration {i}")
                break  

            except rq.exceptions.RequestException as e:
                attempt += 1
                print(f"Attempt {attempt} failed: {e}")
                if attempt < max_retries:
                    print(f"Retrying in {retry_delay} seconds...")
                    t.sleep(retry_delay)
                else:
                    print("Max retries exceeded. Skipping this iteration.")
                    break

        t.sleep(1)

except Exception as e:
    print(f"Unexpected error: {e}")

data = pd.DataFrame(data_list, columns=['timestamp', 'latitude', 'longitude'])

data.to_csv('iss_location_data.csv', index=False)

print("Data added to csv")
