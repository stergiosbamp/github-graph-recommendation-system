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

# Read the seed repositories
with open("repos.json", "r") as fp:
    seed_repos = json.load(fp)

for repo in seed_repos:
    # For each repository get the stargazers
    users = []
    fullname = repo["full_name"]
    # Construct the final endpoint for the repository
    url = base_endpoint_start + fullname + base_endpoint_end

    print("Getting stargazers for repo: {}".format(fullname))

    for page in range(1, 401):
        params = {
            "per_page": "100",
            "page": page
        }
    
        print("\tRequesting page: {}".format(page))

        response = requests.get(url, headers=headers, params=params)
        # Check for rate limiting error (5000 requests per hour)
        if response.status_code == 403:
            print("\tRate limiting error!")
            exit()

        stargazers = json.loads(response.text)
        # Check if we collected all users for the repository
        if len(stargazers) == 0:
            print("You reached the end for repo: {} at page: {}".format(repo, page))
            break

        for user in stargazers:
            # Keep only login (username) and id of the user
            filtered_user = dict()
            filtered_user["login"] = user["login"]
            filtered_user["id"] = user["id"]
            users.append(filtered_user)

    # Replace the / (slash) with -- (double dash) to make it a valid filepath
    filename = "stargazers/" + fullname.replace('/', '--') + ".json"
    # Save the stargazers for each repository in each own json file
    with open(filename, "w") as fp:
        json.dump(users, fp, indent=4)
