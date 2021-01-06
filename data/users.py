import os
import requests
import json

from dotenv import load_dotenv

# Get our GitHub's token
load_dotenv()

TOKEN = os.getenv("TOKEN")
GITHUB_API = "https://api.github.com/"

base_endpoint_start = GITHUB_API + "repos/"
base_endpoint_end = "/stargazers"

headers = {
    "Authorization": "Bearer {}".format(TOKEN)
}

with open("repos.json", "r") as fp:
    seed_repos = json.loads(fp)

for repo in seed_repos:

    users = []

    fullname = repo["full_name"]

    url = base_endpoint_start + fullname + base_endpoint_end

    flag = True

    for page in range(1, 401):
        params = {
            "per_page": "100",
            "page": page
        }
    
        response = requests.get(url, headers=headers, params=params)
        stargazers = json.loads(response.text)

        for user in stargazers:
            filtered_user = dict()
            filtered_user["login"] = user["login"]
            filtered_user["id"] = user["id"]
            users.append(filtered_user)
    
    filename = fullname.replace('/', '--') + ".json"
    with open(filename, "w") as fp:
        json.dump(items, fp, indent=4)