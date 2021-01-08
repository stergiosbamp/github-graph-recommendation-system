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
    # G = build_bipartite_graph("../data/repos_users-6000.json")
    # G = build_bipartite_graph("../data/repos_users-9000.json")

    # random_walk_parameters(G)
    top_k_experiment(G)

"""
RANDOM WALKS AND DOUBLE STEPS
-----------------------------

For 3000 users graph size.

Performance for random_walks_per_repo = 5 and double_steps_per_random_walk = 1
Precision @ 30: 0.0963
Recall: @ 30: 0.2890

Performance for random_walks_per_repo = 5 and double_steps_per_random_walk = 2
Precision @ 30: 0.1084
Recall: @ 30: 0.3252

Performance for random_walks_per_repo = 5 and double_steps_per_random_walk = 3
Precision @ 30: 0.1162
Recall: @ 30: 0.3485

Performance for random_walks_per_repo = 5 and double_steps_per_random_walk = 4
Precision @ 30: 0.1197
Recall: @ 30: 0.3590

Performance for random_walks_per_repo = 10 and double_steps_per_random_walk = 1
Precision @ 30: 0.1101
Recall: @ 30: 0.3302

Performance for random_walks_per_repo = 10 and double_steps_per_random_walk = 2
Precision @ 30: 0.1204
Recall: @ 30: 0.3612

Performance for random_walks_per_repo = 10 and double_steps_per_random_walk = 3
Precision @ 30: 0.1286
Recall: @ 30: 0.3857

Performance for random_walks_per_repo = 10 and double_steps_per_random_walk = 4
Precision @ 30: 0.1362
Recall: @ 30: 0.4087

Performance for random_walks_per_repo = 20 and double_steps_per_random_walk = 1
Precision @ 30: 0.1261
Recall: @ 30: 0.3782

Performance for random_walks_per_repo = 20 and double_steps_per_random_walk = 2
Precision @ 30: 0.1340
Recall: @ 30: 0.4020

Performance for random_walks_per_repo = 20 and double_steps_per_random_walk = 3
Precision @ 30: 0.1379
Recall: @ 30: 0.4137

Performance for random_walks_per_repo = 20 and double_steps_per_random_walk = 4
Precision @ 30: 0.1378
Recall: @ 30: 0.4135

Performance for random_walks_per_repo = 40 and double_steps_per_random_walk = 1
Precision @ 30: 0.1364
Recall: @ 30: 0.4093

Performance for random_walks_per_repo = 40 and double_steps_per_random_walk = 2
Precision @ 30: 0.1403
Recall: @ 30: 0.4208

Performance for random_walks_per_repo = 40 and double_steps_per_random_walk = 3
Precision @ 30: 0.1435
Recall: @ 30: 0.4305

Performance for random_walks_per_repo = 40 and double_steps_per_random_walk = 4
Precision @ 30: 0.1432
Recall: @ 30: 0.4297
"""

"""
TOP-K (3000)
------------

Performance for top-k:  10
Precision @ 10: 0.1890
Recall: @ 10: 0.1890

Performance for top-k:  20
Precision @ 20: 0.1547
Recall: @ 20: 0.3093

Performance for top-k:  30
Precision @ 30: 0.1323
Recall: @ 30: 0.3970

Performance for top-k:  40
Precision @ 40: 0.1191
Recall: @ 40: 0.4765

TOP-K (6000)
------------

Performance for top-k:  10
Precision @ 10: 0.1620
Recall: @ 10: 0.1620

Performance for top-k:  20
Precision @ 20: 0.1413
Recall: @ 20: 0.2827

Performance for top-k:  30
Precision @ 30: 0.1227
Recall: @ 30: 0.3682

Performance for top-k:  40
Precision @ 40: 0.1128
Recall: @ 40: 0.4510

TOP-K (9000)
------------

Performance for top-k:  10
Precision @ 10: 0.1550
Recall: @ 10: 0.1550

Performance for top-k:  20
Precision @ 20: 0.1345
Recall: @ 20: 0.2690

Performance for top-k:  30
Precision @ 30: 0.1173
Recall: @ 30: 0.3518

Performance for top-k:  40
Precision @ 40: 0.1048
Recall: @ 40: 0.4192

"""