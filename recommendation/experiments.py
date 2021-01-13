import random
import time

from random_walk import *


def random_walk_parameters(G):
    """
    Function to evaluate the effect of some selected random_walks_per_repo and double_steps_per_random_walk parameters
    based on the precision and recall of the recommendations for a randomly selected portion of users (600)

    Args:
        - G (networkx graph): The graph for which to evaluate the performance

    """
    repos, users = nx.bipartite.sets(G)
    users = list(users)
    target_users = random.sample(users, 600)

    portion = 10
    topk = 30

    random_walks_per_repo = [5, 10, 20, 40]
    double_steps_per_random_walk = [1, 2, 3, 4]
    
    for param1 in random_walks_per_repo:
        for param2 in double_steps_per_random_walk:
            n_correct = 0
            for user in target_users:
                n_correct += evaluate(G, user, portion=portion, topk=topk, random_walks_per_repo=param1, double_steps_per_random_walk=param2)
            
            print(f"\nPerformance for random_walks_per_repo = {param1} and double_steps_per_random_walk = {param2}")
            print(f"Precision @ {topk}: {n_correct / (topk * len(target_users)):.4f}")
            print(f"Recall: @ {topk}: {n_correct/ (portion * len(target_users)):.4f}")

    
def top_k_experiment(G):
    """
    Function to evaluate the effect of some number of top-k recommended items based on the precision and recall of the recommendations
    for a randomly selected portion of users (600)

    Args:
        - G (networkx graph): The graph for which to evaluate the performance

    """
    repos, users = nx.bipartite.sets(G)
    users = list(users)
    target_users = random.sample(users, 600)

    portion = 10
    random_walk_per_repo = 10
    double_steps_per_random_walk = 4

    top_k_s = [10, 20, 30, 40]

    for topk in top_k_s:
        n_correct = 0
        for user in target_users:
            n_correct += evaluate(G,
                                  user,
                                  portion=portion,
                                  topk=topk,
                                  random_walks_per_repo=random_walk_per_repo,
                                  double_steps_per_random_walk=double_steps_per_random_walk)
        print("\nPerformance for top-k: ", topk)
        print(f"Precision @ {topk}: {n_correct / (topk * len(target_users)):.4f}")
        print(f"Recall: @ {topk}: {n_correct / (portion * len(target_users)):.4f}")


if __name__ == "__main__":
    random.seed(0)

    G = build_bipartite_graph("../data/repos_users-3000.json")
    # G = build_bipartite_graph("../data/repos_users-6000.json")
    # G = build_bipartite_graph("../data/repos_users-9000.json")

    # random_walk_parameters(G)
    top_k_experiment(G)
