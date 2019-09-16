import numpy as np
import random

def djikstra(edges, start_node):
    # Get unique nodes
    to_visit = [start_node]
    visited = []
    distances = {start_node: 0}
    # Keep track of paths by memorizing candidate parent
    parents = {start_node: None}
    while len(to_visit):
        # Sort nodes by current distance to source and select the closest one
        min_node, min_dist = sorted([(node, distances[node]) for node in to_visit], key=lambda x: x[1])[0]
        to_visit.remove(min_node)
        # Get edges that link selected nodes and other nodes not already visited
        neigh_edges = [edge for edge in edges if edge[0] == min_node and edge[1] not in visited]
        neigh_nodes = [edge[1] for edge in neigh_edges]
        to_visit += neigh_nodes
        visited.append(min_node)
        for neigh_edge in neigh_edges:
            _, target, dist = neigh_edge
            if target not in distances or dist + min_dist < distances[target]:
                distances[target] = dist + min_dist
                parents[target] = min_node
    return distances, parents

def get_path(parents, node_idx):
    cur_idx = node_idx
    path = [cur_idx]
    while parents[cur_idx] is not None:
        path.append(parents[cur_idx])
        cur_idx = parents[cur_idx]
    return path
    
# Generate random edges
random.seed(0)
node_nb = 6
connect_prob = 0.3
edges = []
max_dist = 20
for node_start in range(node_nb):
    for node_end in range(node_nb):
        if node_end != node_start:
            if random.random() < connect_prob:
                edges.append((node_start, node_end, random.randint(1, max_dist)))

dists, parents = djikstra(edges, 0)
print(edges, dists)
print(get_path(parents, 2))




