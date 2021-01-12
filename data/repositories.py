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

# List to hold all the final repositories (total 250)
repositories = []
for page in range(1, 4):
    params = {
        "per_page": "100",
        "page": page
    }

    response = requests.get(endpoint, headers=headers, params=params)
    data = json.loads(response.text)

    for item in data['items']:
        # Keep only id, full_name, stargazers_count from the object attributes
        filtered_data = dict()
        filtered_data['id'] = item['id']
        filtered_data['full_name'] = item['full_name']
        filtered_data['stargazers_count'] = item['stargazers_count']

        repositories.append(filtered_data)

# Save the list of the repositories in json file
with open("repos.json", "w") as fp:
    json.dump(repositories, fp, indent=4)
