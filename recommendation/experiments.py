from random_walk import *

import random
import time

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

    


if __name__ == "__main__":
    random.seed(0)

    G = build_bipartite_graph("../data/repos_users.json")

    random_walk_parameters(G)

"""
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