import os
import requests
import json

from dotenv import load_dotenv


# Get our GitHub's token
load_dotenv()

TOKEN = os.getenv("TOKEN")
GITHUB_API = "https://api.github.com/"

# Construct the query string based on GitHub's guidelines
#   topic: machine learning
#   language: Python
#   starts: at least 1000 stars

endpoint = GITHUB_API + "search/repositories?q=topic:machine-learning+language:python+stars:>1000"

headers = {
    "Authorization": "Bearer {}".format(TOKEN)
}

items = []
for page in range(1, 4):
    params = {
        "per_page": "100",
        "page": page
    }

    response = requests.get(endpoint, headers=headers, params=params)
    data = json.loads(response.text)

    for item in data['items']:
        filtered_data = dict()
        filtered_data['id'] = item['id']
        filtered_data['full_name'] = item['full_name']
        filtered_data['stargazers_count'] = item['stargazers_count']

        items.append(filtered_data)


with open("repos.json", "w") as fp:
    json.dump(items, fp, indent=4)
