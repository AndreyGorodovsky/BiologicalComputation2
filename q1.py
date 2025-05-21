import itertools
import networkx as nx

def is_connected(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    queue = [0]
    visited[0] = True
    while queue:
        node = queue.pop(0)
        for neighbor, has_edge in enumerate(adj_matrix[node]):
            if has_edge and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return all(visited)

def generateSubgraphs(n):
    edge_indices = [(i, j) for i in range(n) for j in range(n) if i != j]
    num_edges = len(edge_indices)
    connected_graphs = []
    for bits in range(1, 2 ** num_edges):
        adj_matrix = [[0] * n for _ in range(n)]
        for idx, (i, j) in enumerate(edge_indices):
            if (bits >> idx) & 1:
                adj_matrix[i][j] = 1
        if is_connected(adj_matrix):
            connected_graphs.append(adj_matrix)
    # Remove isomorphic duplicates
    unique_graphs = []
    nx_graphs = []
    for adj in connected_graphs:
        G = nx.DiGraph()
        G.add_nodes_from(range(len(adj)))
        for i in range(len(adj)):
            for j in range(len(adj)):
                if adj[i][j]:
                    G.add_edge(i, j)
        if not any(nx.is_isomorphic(G, H) for H in nx_graphs):
            unique_graphs.append(adj)
            nx_graphs.append(G)
    return unique_graphs

def writeOutput(n, graphs):
    with open("q1.txt", "w") as f:
        f.write(f"n={n}\n")
        f.write(f"count={len(graphs)}\n")
        for idx, graph in enumerate(graphs, 1):
            f.write(f"#{idx}\n")
            for i, row in enumerate(graph):
                for j, val in enumerate(row):
                    if val:
                        f.write(f"{i+1} {j+1}\n")

def main():
    n = int(input("Enter n: "))
    graphs = generateSubgraphs(n)
    writeOutput(n, graphs)

if __name__ == "__main__":
    main()       