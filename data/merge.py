import json
import pathlib

from collections import Counter


all_users = Counter()
repo_users_mapping = dict()

path = pathlib.Path("stargazers/")

if not any(path.iterdir()):
    print("The directory for the stargazers per repository is empty. "
          "Please request them from the contributors of the project")
    exit()

for repo in path.iterdir():
    with open(repo, "r") as f:
        stargazers = json.load(f)

    repository_name = repo.name.replace("--", "/")
    # take just username
    users = [user['login'] for user in stargazers]
    repo_users_mapping[repository_name] = users
    all_users.update(users)

print(all_users.most_common(5))

# Write the unified json collection to file
with open("repos_users.json", "w") as f:
    json.dump(repo_users_mapping, f, indent=4)
