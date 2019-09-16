import numpy as np

def djikstra(adj_matrix, start_idx=0):
    visited = []  # Keep track of already visited node idxs
    to_vis = [start_idx]  # Keep track of node idxs that are reachable and not visited yet

    dists = {start_idx: 0}  # Keep track of best distances to date
    # Initialize distances with infinity except at root
    for idx in range(len(adj_matrix)):
        if idx != start_idx:
            dists[idx] = float("inf")

    # Select node with lowest dist
    while len(to_vis):
        # This operation has time complexity V where V is the number of edges that are still to visit (worse case, ~total number of edges)
        # It can be made log(V) by using a min heap, which can be created in V time, and get_min and add_val are in log(V_to_visit)
        min_node, min_dist = sorted([(start_idx, dists[start_idx]) for start_idx in to_vis], key=lambda x: x[1])[0]
        to_vis = [node for node in to_vis if node != min_node] 
        visited.append(min_node)

        neighbor_dists = adj_matrix[min_node]
        for neigh_idx, neigh_dist in enumerate(neighbor_dists):
            # Nones in adjacency matrix mark absent paths
            if neigh_dist is not None and neigh_idx != min_node:
                if min_dist + neigh_dist < dists[neigh_idx]:
                    dists[neigh_idx] = min_dist + neigh_dist
                    if neigh_idx not in to_vis and neigh_idx not in visited:
                        to_vis.append(neigh_idx)
    return dists
            

def djikstra_with_path(adj_matrix, start_idx=0):
    visited = []  # Keep track of already visited node idxs
    to_vis = [start_idx]  # Keep track of node idxs that are reachable and not visited yet

    dists = {start_idx: 0}  # Keep track of best distances to date
    # Initialize distances with infinity except at root
    for idx in range(len(adj_matrix)):
        if idx != start_idx:
            dists[idx] = float("inf")
    # Aggregate parents in hash map which points from child to parent
    parents = {idx: None for idx in range(len(adj_matrix))}

    # Select node with lowest dist
    while len(to_vis):
        min_node, min_dist = sorted([(start_idx, dists[start_idx]) for start_idx in to_vis], key=lambda x: x[1])[0]
        to_vis = [node for node in to_vis if node != min_node]
        # from collections improt 
        visited.append(min_node)

        neighbor_dists = adj_matrix[min_node]
        for neigh_idx, neigh_dist in enumerate(neighbor_dists):
            if neigh_dist is not None and neigh_idx != min_node:
                if min_dist + neigh_dist < dists[neigh_idx]:
                    dists[neigh_idx] = min_dist + neigh_dist
                    # Remember current best parent
                    parents[neigh_idx] = min_node
                    if neigh_idx not in to_vis and neigh_idx not in visited:
                        to_vis.append(neigh_idx)
    return dists, parents

def get_path(parents, idx):
    cur_idx = idx
    path = [idx]
    while parents[cur_idx] is not None:
        path.append(parents[cur_idx])
        cur_idx = parents[cur_idx]
    return path
            
adj_matrix = [[2, 1, None, 2, 1],
               [2, 10, 1, 1, None],
               [None, 2, 2, None, None],
               [2, None, None, 2, 1],
               [4, 1, None, None, None]]

print(np.array(adj_matrix), djikstra(adj_matrix))
dists, parents = djikstra_with_path(adj_matrix)
print(np.array(adj_matrix), dists, parents, get_path(parents, 2))
