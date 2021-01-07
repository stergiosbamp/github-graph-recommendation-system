import json
import networkx as nx

from random import choice
from collections import Counter
from random import choice, sample


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


def print_graph_stats(G):
    # graph metrics
    print(f"Average clustering coefficient: {nx.average_clustering(G)}")
    print(f"Transitivity: {nx.transitivity(G)}")
    print(f"Average shortest path length: {nx.average_shortest_path_length(G)}")
    print(f"Diameter: {nx.diameter(G)}")
    print(f"Radius: {nx.radius(G)}")
    print(f"Number of connected components: {len(list(nx.connected_components(G)))}")

    # take forever to compute, probably not applicable on our graph which is highly connected
    print(f"Node connectivity: {nx.node_connectivity(G)}")
    print(f"Minimum node cut: {nx.minimum_node_cut(G)}")
    print(f"Edge connectivity: {nx.edge_connectivity(G)}")
    print(f"Minimum node cut: {nx.minimum_edge_cut(G)}")

    # node metrics (also need time to compute)
    print(f"Degree centrality: {nx.degree_centrality(G)}")
    print(f"Closeness centrality: {nx.closeness_centrality(G, wf_improved=True)}")
    print(f"Betweenness centrality: {nx.betweenness_centrality(G, normalized=True, endpoints=False)}")
    print(f"PageRank: {nx.pagerank(G)}")
    h, a = nx.hits(G)
    print(f"Hubs: {h}")
    print(f"Authorities: {a}")


def random_neighbor(G, node):
    neighbors = list(G.neighbors(node))
    randomly_selected_neighbor = choice(neighbors)
    return randomly_selected_neighbor


def random_walks(G_reduced, target_user, total_steps, double_steps_per_random_walk, verbose=False):
    seed_repos = list(G_reduced.neighbors(target_user))
    total_steps_per_repo = round(total_steps / len(seed_repos))
    random_walks_per_repo = round(total_steps_per_repo / (2 * double_steps_per_random_walk))
    if random_walks_per_repo == 0:
        raise(ValueError("Increase total_steps or decrease double_steps_per_random_walk."))

    if verbose:
        print(f"\n\n\nStarting random walks for target user: {target_user}")
        print(f"The seed repos of the user are: {len(seed_repos)}")
        print(f"The number of random walks per repo will be: {random_walks_per_repo}")

    repo_visit_counts = Counter()
    for seed_repo in seed_repos:
        if verbose:
            print(f"\nStarting random walks for seed repo: {seed_repo}")

        for i in range(random_walks_per_repo):
            if verbose:
                print(f"Repo random walk: {i}")
            repo_node = seed_repo

            for t in range(double_steps_per_random_walk):
                user_node = random_neighbor(G_reduced, repo_node)
                repo_node = random_neighbor(G_reduced, user_node)
                repo_visit_counts.update([repo_node])
                if verbose:
                    print(f"{t}: {repo_node}")
            
            if verbose:
                print(f"The repo visit counts are {repo_visit_counts}")
            
    return repo_visit_counts


def remove_random_edges(G, target_user, portion=10):
    neighbors = list(G.neighbors(target_user))
    neighbors_to_remove = sample(neighbors, k=portion)

    for neighbor in neighbors_to_remove:
        G.remove_edge(target_user, neighbor)

    return neighbors_to_remove


def add_edges(G, target_user, edges):
    edges_to_add = []
    for edge in edges:
        edges_to_add.append((target_user, edge))

    G.add_edges_from(edges_to_add)


if __name__ == "__main__":
    G = build_bipartite_graph("../data/repos_users.json")

    target_user = "walsvid"
    repo_visit_counts = random_walks(G, target_user, total_steps=2000, double_steps_per_random_walk=3)
    topk = 5
    print(f"\n\nThe top-5 recommended repos for user {target_user} are: {repo_visit_counts.most_common(topk)}")
