import random
import time

from random_walk import *


def random_walk_parameters(G):
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

    G = build_bipartite_graph("../data/repos_users.json")

    # random_walk_parameters(G)
    top_k_experiment(G)

"""
RANDOM WALKS AND DOUBLE STEPS
-----------------------------

For 3000 users graph size.

Performance for random_walks_per_repo = 5 and double_steps_per_random_walk = 1
Precision @ 30: 0.0758
Recall: @ 30: 0.2275

Performance for random_walks_per_repo = 5 and double_steps_per_random_walk = 2
Precision @ 30: 0.0828
Recall: @ 30: 0.2485

Performance for random_walks_per_repo = 5 and double_steps_per_random_walk = 3
Precision @ 30: 0.0853
Recall: @ 30: 0.2560

Performance for random_walks_per_repo = 5 and double_steps_per_random_walk = 4
Precision @ 30: 0.0897
Recall: @ 30: 0.2690

Performance for random_walks_per_repo = 10 and double_steps_per_random_walk = 1
Precision @ 30: 0.0847
Recall: @ 30: 0.2540

Performance for random_walks_per_repo = 10 and double_steps_per_random_walk = 2
Precision @ 30: 0.0941
Recall: @ 30: 0.2822

Performance for random_walks_per_repo = 10 and double_steps_per_random_walk = 3
Precision @ 30: 0.0949
Recall: @ 30: 0.2848

Performance for random_walks_per_repo = 10 and double_steps_per_random_walk = 4
Precision @ 30: 0.0980
Recall: @ 30: 0.2940

Performance for random_walks_per_repo = 20 and double_steps_per_random_walk = 1
Precision @ 30: 0.0955
Recall: @ 30: 0.2865

Performance for random_walks_per_repo = 20 and double_steps_per_random_walk = 2
Precision @ 30: 0.0992
Recall: @ 30: 0.2975

Performance for random_walks_per_repo = 20 and double_steps_per_random_walk = 3
Precision @ 30: 0.1004
Recall: @ 30: 0.3012

Performance for random_walks_per_repo = 20 and double_steps_per_random_walk = 4
Precision @ 30: 0.1012
Recall: @ 30: 0.3035

Performance for random_walks_per_repo = 40 and double_steps_per_random_walk = 1
Precision @ 30: 0.1034
Recall: @ 30: 0.3102

Performance for random_walks_per_repo = 40 and double_steps_per_random_walk = 2
Precision @ 30: 0.1034
Recall: @ 30: 0.3102

Performance for random_walks_per_repo = 40 and double_steps_per_random_walk = 3
Precision @ 30: 0.1058
Recall: @ 30: 0.3175

Performance for random_walks_per_repo = 40 and double_steps_per_random_walk = 4
Precision @ 30: 0.1078
Recall: @ 30: 0.3235
"""

"""
TOP-K
------------

Performance for top-k:  10
Precision @ 10: 0.1183
Recall: @ 10: 0.1183

Performance for top-k:  20
Precision @ 20: 0.1037
Recall: @ 20: 0.2073

Performance for top-k:  30
Precision @ 30: 0.0977
Recall: @ 30: 0.2930

Performance for top-k:  40
Precision @ 40: 0.0932
Recall: @ 40: 0.3730
"""