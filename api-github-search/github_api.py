import requests

# Define the API endpoint
url = "https://api.github.com/search/repositories"

# Define query parameters
params = {
    "q": "python",
    "sort": "stars",
    "order": "desc",
    "per_page": 5
}

# Make the request
response = requests.get(url, params=params)

# Convert response to JSON
data = response.json()

# Print repository name and stars
for repo in data["items"]:
    print(f"{repo['name']} - ⭐ {repo['stargazers_count']}")