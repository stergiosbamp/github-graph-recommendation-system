import json
import pathlib

from collections import Counter


all_users = Counter()
repo_users_mapping = dict()
filtered_users_repos = dict()

path = pathlib.Path("stargazers/")

if not any(path.iterdir()):
    print("The directory for the stargazers per repository is empty. "
          "Please request them from the contributors of the project")
    exit()

for repo in path.iterdir():
    with open(repo, "r") as f:
        stargazers = json.load(f)

    repository_name = repo.stem.replace("--", "/")
    # take just username
    users = [user['login'] for user in stargazers]
    repo_users_mapping[repository_name] = users
    all_users.update(users)

# Take the top-3000 users with the highest number of stars
most_common_users = all_users.most_common(3000)

# Get the top users based on their stars
top_users = []
for stat in most_common_users:
    username, stars = stat
    top_users.append(username)

# Filter out the users based on the top users
for repo, users in repo_users_mapping.items():
    # From all users from the running repo, take the intersection with the top_users.
    filtered_users = set(users).intersection(set(top_users))
    filtered_users_repos[repo] = list(filtered_users)


# Write the unified json collection to file
with open("repos_users.json", "w") as f:
    json.dump(filtered_users_repos, f, indent=4)
