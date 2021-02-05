import json
import networkx as nx

from random import choice
from collections import Counter
from random import choice, sample


def build_bipartite_graph(filename):
    """
    Function that reads the final data collection and builds an networkx
    bipartipe graph between repositories and stargazers.

    Args:
        - filename (str): The file to read
    Returns:
        The networkx graph
    """
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


def save_graph_for_gephi(G, path):
    """
    Function that saves a graph as .gexf file in compatible format
    with Gephi visualization tool

    Args:
        - G (networkx graph): The graph
        - path (str): The path where to save the .gexf file
    """

    nx.write_gexf(G, path)
    print("Saved graph in Gephi compatible format")


def print_graph_stats(G):
    """
    Function that prints various graph metrics.

    Args:
        - G (networkx graph): The graph for which to print metrics
    """
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
    """
    Function thar randomly selects a neighbor of a node.

    Args:
        - G (networkx graph): The graph where the node belong
        - node (str): The node for which to choose a random neighbor

    Returns:
        node (str): The randomly selected node

    """
    neighbors = list(G.neighbors(node))
    randomly_selected_neighbor = choice(neighbors)
    return randomly_selected_neighbor


def random_walks(G_reduced, target_user, random_walks_per_repo, double_steps_per_random_walk, verbose=False):
    """
    Function that given a target user gets the seed repositories of the user, conducts random walks for each repository
    and returns the aggregated repository visit counts

    Args:
        - G_reduced (networkx graph): The graph on which random walks will run
        - target_user (str): The user for whom to conduct the random walks
        - random_walks_per_repo (int): The number of random walks to conduct for each repository of the target user
        - double_steps_per_random_walk (int): The number of double hops to conduct for each random walk
        - verbose (bool): Whether to print informative messages

    Returns:
        (dict): The dict that holds the repository aggregated visit counts from the random walk

    """
    seed_repos = list(G_reduced.neighbors(target_user))
    #print(f"\n\n\nStarting random walks for target user: {target_user}")

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
    """
    Function that randomly removes edges for given target users

    Args:
        - G (networkx graph): The graph where the target user belongs
        - target_user (str): The user for whom to remove edges
        - portion (int): The number of edges to be removed

    Returns:
        (list, list): The list of the removed neighbors and the list of the remaining neighbors

    """
    neighbors = set(G.neighbors(target_user))
    removed_neighbors = sample(neighbors, k=portion)
    remaining_neighbors = neighbors.difference(set(removed_neighbors))
    remaining_neighbors = list(remaining_neighbors)

    for neighbor in removed_neighbors:
        G.remove_edge(target_user, neighbor)

    return removed_neighbors, remaining_neighbors


def add_edges(G, target_user, edges):
    """
    Function to add back to the graph the removed edges of the target user

    Args:
        - G (networkx graph): The graph where the target user belongs
        - target_user (str): The user for whom to add back edges
        - edges (List[str]): The nodes of the edges that should be added
    """
    edges_to_add = []
    for edge in edges:
        edges_to_add.append((target_user, edge))

    G.add_edges_from(edges_to_add)


def evaluate(G, target_user, portion, topk, random_walks_per_repo, double_steps_per_random_walk):
    """
    Function that given a target user and corresponding recommendation parameters, returns the number
    of repos that are founded in the initially removed repo edges.

    Args:
        - G (networkx graph): The graph where the target user belongs
        - target_user (str): The user for whom to evaluate the recommendation
        - portion (int): The number of edges to be removed
        - topk: The number of repositories to recommend
        - random_walks_per_repo (int): The number of random walks to conduct for each repository of the target user
        - double_steps_per_random_walk (int): The number of double hops to conduct for each random walk

    Returns:
        The number of recommended repos that are also found in the initially removed repo edges
    """
    removed_neighbors, remaining_neighbors = remove_random_edges(G, target_user, portion=portion)
    repo_visit_counts = random_walks(G, target_user, random_walks_per_repo=random_walks_per_repo, double_steps_per_random_walk=double_steps_per_random_walk)
    add_edges(G, target_user, removed_neighbors)
    topk_repos = []
    recommend_count = 0
    for repo, count in repo_visit_counts.most_common():
        if repo not in set(remaining_neighbors):
            topk_repos.append(repo)
            recommend_count += 1
        if recommend_count == topk:
            break
    correct = set(topk_repos).intersection(set(removed_neighbors))
    return len(correct)


def recommend(G, target_user, topk, random_walks_per_repo=10, double_steps_per_random_walk=4):
    """
    Function that actually performs the recommendation task
    For a target user using the random walk algorithm recommends the requested number
    of repos that the user hasn't starred already

    Args:
        - G (networkx graph): The graph where the target user belongs
        - target_user (str): The user for whom to evaluate the recommendation
        - topk: The number of repositories to recommend
        - random_walks_per_repo (int): The number of random walks to conduct for each repository of the target user
        - double_steps_per_random_walk (int): The number of double hops to conduct for each random walk

    """
    repo_visit_counts = random_walks(G, target_user, random_walks_per_repo=random_walks_per_repo, double_steps_per_random_walk=double_steps_per_random_walk)
    topk_repos = []
    recommend_count = 0
    starred_repos = list(G.neighbors(target_user))
    for repo, count in repo_visit_counts.most_common():
        if repo not in starred_repos:
            topk_repos.append(repo)
            recommend_count += 1
        if recommend_count == topk:
            break

    print("For GitHub user: {}, "
          "\n\tthe top-{} recommended repositories are {}".format(target_user, topk, topk_repos))


if __name__ == "__main__":
    G = build_bipartite_graph("../data/repos_users-3000.json")

    save_graph_for_gephi(G, "../data/github-bipartite.gexf")

    target_users = ["fly51fly", "gaomingweig", "izdi", "data-catalysis"]

    for stargazer in target_users:
        recommend(G, stargazer, topk=10)
