import json
import networkx as nx

from random import choice


def build_bipartite_graph(filename):
    print(f"\nBuilding graph...")

    with open(filename, "r") as f:
        repo_users_mapping = json.load(f)

    repo_nodes = list(repo_users_mapping.keys())
    user_nodes = set()
    edges = []
    for repo, users in repo_users_mapping.items():
        for user in users:
            user_nodes.add(user)
            edges.append((repo, user))

    print(f"\nRepo nodes extracted from file: {len(repo_nodes)}")
    print(f"User nodes extracted from file: {len(user_nodes)}")
    print(f"Edges extracted from file: {len(edges)}")

    G = nx.Graph()
    G.add_nodes_from(repo_nodes, bipartite=0)
    G.add_nodes_from(user_nodes, bipartite=1)
    G.add_edges_from(edges)

    print(f"Constructed graph is bipartite: {nx.bipartite.is_bipartite(G)}")

    return G


def random_neighbor(G, node):
    neighbors = list(G.neighbors(node))
    randomly_selected_neighbor = choice(neighbors)
    return randomly_selected_neighbor


def random_walk(G, starting_user, iterations):
    neighbor = random_neighbor(G, starting_user)
    print("Starting random from user", neighbor)

    for i in range(iterations):
        neighbor = random_neighbor(G, neighbor)
        if i % 2 == 0:
            print("Walker is now at user", neighbor)
        else:
            print("Walker is now at repo", neighbor)

    return neighbor


if __name__ == "__main__":
    G = build_bipartite_graph("../data/repos_users.json")

    target_user = "walsvid"
    recommended_repo = random_walk(G, target_user, 10)
    print("For user '{}' is recommended repository: '{}'".format(target_user, recommended_repo))
