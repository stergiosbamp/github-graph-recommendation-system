import matplotlib.pyplot as plt
import networkx as nx


def plot_performance_vs_random_walk_parameters():
    # all number are for portion = 10, and users = 3000

    # number of double steps used used for each individual random walk
    double_steps_per_random_walk = [1, 2, 3, 4]

    # pefrormance with 5 random walks per repo
    prec_with_5_random_walks_per_repo = [0.0758, 0.0828, 0.0853, 0.0897]
    rec_with_5_random_walks_per_repo = [0.2275, 0.2485, 0.2560, 0.2690]

    # pefrormance with 10 random walks per repo
    prec_with_10_random_walks_per_repo = [0.0847, 0.0941, 0.0949, 0.0980]
    rec_with_10_random_walks_per_repo = [0.2540, 0.2822, 0.2848, 0.2940]

    # pefrormance with 20 random walks per repo
    prec_with_20_random_walks_per_repo = [0.0955, 0.0992, 0.1004, 0.1012]
    rec_with_20_random_walks_per_repo = [0.2865, 0.2975, 0.3012, 0.3035]

    # pefrormance with 40 random walks per repo
    prec_with_40_random_walks_per_repo = [0.1034, 0.1034, 0.1058, 0.1078]
    rec_with_40_random_walks_per_repo = [0.3102, 0.3102, 0.3175, 0.3235]

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
    plt.legend(["3000 stargazers", "6000 stargazers", "9000 stargazers"])

    # Recall plot for all three graphs
    plt.figure()
    plt.plot(top_k_s, rec_3000)
    plt.plot(top_k_s, rec_6000)
    plt.plot(top_k_s, rec_9000)

    plt.xlabel("Top-K queries")
    plt.ylabel("Recall @ K")
    plt.xticks(top_k_s)
    plt.legend(["3000 stargazers", "6000 stargazers", "9000 stargazers"])

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
    plt.legend(["Graph size: 3000 users"])

    plt.show()


if __name__ == "__main__":
    # plot_performance_vs_random_walk_parameters()
    plot_performance_vs_top_k()
