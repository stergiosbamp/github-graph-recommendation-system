import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    plot_performance_vs_random_walk_parameters()
