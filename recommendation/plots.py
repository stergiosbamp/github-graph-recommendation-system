import matplotlib.pyplot as plt
import networkx as nx

from random_walk import build_bipartite_graph


def plot_performance_vs_random_walk_parameters():
    # all number are for portion = 10, and users = 3000

    # number of double steps used used for each individual random walk
    double_steps_per_random_walk = [1, 2, 3, 4]

    # pefrormance with 5 random walks per repo
    prec_with_5_random_walks_per_repo = [0.0963, 0.1084, 0.1162, 0.1197]
    rec_with_5_random_walks_per_repo = [0.2890, 0.3252, 0.3485, 0.3590]

    # pefrormance with 10 random walks per repo
    prec_with_10_random_walks_per_repo = [0.1101, 0.1204, 0.1286, 0.1362]
    rec_with_10_random_walks_per_repo = [0.3302, 0.3612, 0.3857, 0.4087]

    # pefrormance with 20 random walks per repo
    prec_with_20_random_walks_per_repo = [0.1261, 0.1340, 0.1379, 0.1378]
    rec_with_20_random_walks_per_repo = [0.3782, 0.4020, 0.4137, 0.4135]

    # pefrormance with 40 random walks per repo
    prec_with_40_random_walks_per_repo = [0.1364, 0.1403, 0.1435, 0.1432]
    rec_with_40_random_walks_per_repo = [0.4093, 0.4208, 0.4305, 0.4297]

    # plot precision
    fig = plt.figure()
    plt.plot(double_steps_per_random_walk, prec_with_5_random_walks_per_repo)
    plt.plot(double_steps_per_random_walk, prec_with_10_random_walks_per_repo)
    plt.plot(double_steps_per_random_walk, prec_with_20_random_walks_per_repo)
    plt.plot(double_steps_per_random_walk, prec_with_40_random_walks_per_repo)
    plt.xlabel("Double steps per random walk")
    plt.ylabel("Precision @ 30")
    plt.legend(["5 random walks per repo", "10 random walks per repo", "20 random walks per repo", "40 random walks per repo"])
    plt.xticks([1, 2, 3, 4])

    # plot recall
    fig = plt.figure()
    plt.plot(double_steps_per_random_walk, rec_with_5_random_walks_per_repo)
    plt.plot(double_steps_per_random_walk, rec_with_10_random_walks_per_repo)
    plt.plot(double_steps_per_random_walk, rec_with_20_random_walks_per_repo)
    plt.plot(double_steps_per_random_walk, rec_with_40_random_walks_per_repo)
    plt.xlabel("Double steps per random walk")
    plt.ylabel("Recall @ 30")
    plt.legend(["5 random walks per repo", "10 random walks per repo", "20 random walks per repo", "40 random walks per repo"])
    plt.xticks([1, 2, 3, 4])

    plt.show()


def plot_performance_vs_top_k():
    top_k_s = [10, 20, 30, 40]

    prec_3000 = [0.1890, 0.1547, 0.1323, 0.1191]
    rec_3000 = [0.1890, 0.3093, 0.3970, 0.4765]

    prec_6000 = [0.1620, 0.1413, 0.1227, 0.1128]
    rec_6000 = [0.1620, 0.2827, 0.3682, 0.4510]

    prec_9000 = [0.1550, 0.1345, 0.1173, 0.1048]
    rec_9000 = [0.1550, 0.2690, 0.3518, 0.4192]

    # Precision plot for all three graphs
    plt.figure()
    plt.plot(top_k_s, prec_3000)
    plt.plot(top_k_s, prec_6000)
    plt.plot(top_k_s, prec_9000)

    plt.xlabel("Top-K queries")
    plt.ylabel("Precision @ K")
    plt.xticks(top_k_s)
    plt.legend(["Graph size: 3000 stargazers", "Graph size: 6000 stargazers", "Graph size: 9000 stargazers"])

    # Recall plot for all three graphs
    plt.figure()
    plt.plot(top_k_s, rec_3000)
    plt.plot(top_k_s, rec_6000)
    plt.plot(top_k_s, rec_9000)

    plt.xlabel("Top-K queries")
    plt.ylabel("Recall @ K")
    plt.xticks(top_k_s)
    plt.legend(["Graph size: 3000 stargazers", "Graph size: 6000 stargazers", "Graph size: 9000 stargazers"])

    plt.show()


def plot_degree_distribution(G):
    repos, users = nx.bipartite.sets(G)

    repo_degrees = [G.degree(repo_node) for repo_node in repos]
    user_degrees = [G.degree(user_node) for user_node in users]

    # plot degree distribution for repos
    plt.figure()
    plt.hist(repo_degrees)
    plt.xlabel("Repository node degree")
    plt.ylabel("Number of repository nodes")
    plt.yscale("log")
    plt.legend(["Graph size: 250 repos"])

    # plot degree distribution for users
    plt.figure()
    plt.hist(user_degrees)
    plt.xlabel("User node degree")
    plt.ylabel("Numner of user nodes")
    plt.yscale("log")
    plt.legend(["Graph size: 3000 stargazers"])

    plt.show()


if __name__ == "__main__":
    G = build_bipartite_graph("../data/repos_users-3000.json")

    # plot_performance_vs_random_walk_parameters()
    # plot_degree_distribution(G)
    plot_performance_vs_top_k()
