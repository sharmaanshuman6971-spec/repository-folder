import requests
import pandas as pd

def fetch_and_clean_data():
    # Step 1: Fetch data from API
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()

    # Step 2: Convert to DataFrame
    df = pd.DataFrame(data)

    # Step 3: Basic cleaning
    df = df.rename(columns={"userId": "user_id"})
    df = df.drop(columns=["id"])

    # Step 4: Add post_length column
    df["post_length"] = df["body"].apply(len)

    return df