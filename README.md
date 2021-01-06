# A graph-based Github recommendation system
This is repository for the "Social Network Analysis" course's project.

## Task
Implement a graph-based recommendation system for GitHub. Particularly we
recommend repositories for a target user that he may wants to like or contribute, by
utilizing his previous starred repositories.

Contributors:

* Stergios Bampakis
* Themis Spanoudis
* Takis Kavargyris


## Dataset
The data gathered are from the GitHub's API.
We collect various users (stargazers) from a seed repository and for each user the stars that he has given.


### Project setup

Create virtual environment

```
$ python3 -m venv venv
$ source venv/bin/activate
```

Upgrade pip

```
$ python -m pip install --upgrade pip
```

Install dependencies

```
$ pip install -r requirements.txt
```
