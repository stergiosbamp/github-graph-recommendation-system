import json
import pathlib

from collections import Counter


all_users = Counter()

path = pathlib.Path("stargazers/")

for repo in path.iterdir():
    with open(repo, "r") as f:
        stargazers = json.load(f)

    # take just username
    users = [user['login'] for user in stargazers]
    all_users.update(users)

print(all_users.most_common(5))
