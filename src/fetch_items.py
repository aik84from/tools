import time
import requests


def fetch_items(url, data):
    results = []
    for item in data:
        try:
            start_time = time.time()
            response = requests.post(url, json=item, timeout=600)
            end_time = time.time()
            results.append({
                "response_time": round(end_time - start_time, 4),
                "response": response.json()
            })
        except requests.exceptions.RequestException as e:
            print(e)
    return results
    

