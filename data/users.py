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
    seed_repos = json.load(fp)

for repo in seed_repos:

    users = []
    fullname = repo["full_name"]
    url = base_endpoint_start + fullname + base_endpoint_end

    print("Getting stargazers for repo: {}".format(fullname))

    for page in range(1, 401):
        params = {
            "per_page": "100",
            "page": page
        }
    
        print("\tRequesting page: {}".format(page))

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 403:
            print("\tRate limiting error!")
            exit()

        stargazers = json.loads(response.text)
        if len(stargazers) == 0:
            print("You reached the end for repo: {} at page: {}".format(repo, page))
            break

        for user in stargazers:
            filtered_user = dict()
            filtered_user["login"] = user["login"]
            filtered_user["id"] = user["id"]
            users.append(filtered_user)
    
    filename = "stargazers/" + fullname.replace('/', '--') + ".json"
    with open(filename, "w") as fp:
        json.dump(users, fp, indent=4)
