import os
import requests

api_key = os.getenv("API_KEY")

if not api_key:
    print("Error: API_KEY not found in environment variables.")
    exit(1)

url = "https://jsonplaceholder.typicode.com/posts/1"  # test API

headers = {
    "Authorization": f"Bearer {api_key}"
}

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Response JSON:", response.json())
    elif response.status_code == 429:
        print("Rate limit reached. Try again later.")
    else:
        print(f"Request failed. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("Network error occurred:", e)