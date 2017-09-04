def cluster(num_clusters, desired_num_clusters, sorted_edges, nodes_set):
    while num_clusters > desired_num_clusters:
        node_a, node_b, edge_dist = sorted_edges.pop(0)
        while same_root(node_a, node_b, nodes_set): 
            node_a, node_b, edge_dist = sorted_edges.pop(0)
        union(node_a, node_b, nodes_set)
        num_clusters -= 1
    node_a, node_b, edge_dist = sorted_edges.pop(0)
    while same_root(node_a, node_b, nodes_set): 
        node_a, node_b, edge_dist = sorted_edges.pop(0)
    return node_a, node_b, edge_dist
    

def main():
    edges = []
    #with open('test.txt') as file_in:
    with open('clustering1.txt') as file_in:
        next(file_in)
        for line in file_in:
            edges.append(map(int, line.strip().split(' ')))
    sorted_edges = sorted(edges, key = lambda edge: edge[-1])
    #num_clusters = int(open('test.txt').readline().strip())
    num_clusters = int(open('clustering1.txt').readline().strip())
    desired_num_clusters = 4
    nodes_set = make_nodes_set(num_clusters)
    print(cluster(num_clusters, desired_num_clusters, sorted_edges, nodes_set))

if __name__ == '__main__':
    print main()