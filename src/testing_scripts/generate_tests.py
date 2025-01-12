import random
import os
import networkx as nx
import numpy

def generate_test(file_name, num_nodes, edges):
    """
    Saves a graph with the given parameters to a file.
    """
    with open(file_name, 'w') as file:
        file.write(f"{num_nodes} {len(edges)}\n")
        for u, v in edges:
            file.write(f"{u} {v}\n")

def generate_random_graph(nr_nodes, edge_probability):
    """
    Generates an Erdős-Rényi graph.

    Parameters:
        num_nodes (int): Number of nodes in the graph.
        edge_probability (float): Probability of creating an edge between any two nodes.

    Returns:
        list[tuple[int, int]]: List of edges in the graph.
    """
    graph = nx.erdos_renyi_graph(nr_nodes, edge_probability)
    return list(graph.edges())

def generate_complete_graph(num_nodes):
    """
    Generates a complete graph.

    Parameters:
        num_nodes (int): Number of nodes in the graph.

    Returns:
        list[tuple[int, int]]: List of edges in the graph.
    """
    graph = nx.complete_graph(num_nodes)
    return list(graph.edges())

def generate_cycle_graph(num_nodes):
    """
    Generates a random graph with cycles.

    Returns:
        list[tuple[int, int]]: List of edges in the graph.
    """
    graph = nx.cycle_graph(num_nodes)
    return list(graph.edges())

def generate_bipartite_graph(num_nodes_set1, num_nodes_set2):
    """
    Generates a random bipartite graph.

    Returns:
        list[tuple[int, int]]: List of edges in the graph.
    """
    graph = nx.complete_bipartite_graph(num_nodes_set1, num_nodes_set2)
    return list(graph.edges())

def generate_path_graph(num_nodes):
    """
    Generates a chain graph.

    Returns:
        list[tuple[int, int]]: List of edges in the graph.
    """
    graph = nx.path_graph(num_nodes)
    return list(graph.edges())

def generate_grid_graph(num_rows, num_columns):
    """
    Generates a grid graph.

    Returns:
        list[tuple[int, int]]: List of edges in the graph.
    """
    edges = []
    for i in range(num_rows):
        for j in range(num_columns):
            # Horizontal edges (connect right neighbors)
            if j < num_columns - 1:
                edges.append((i * num_columns + j, i * num_columns + (j + 1)))
            # Vertical edges (connect bottom neighbors)
            if i < num_rows - 1:
                edges.append((i * num_columns + j, (i + 1) * num_columns + j))

    return edges

def generate_all_tests():
    """
    Generates test cases and saves them in the 'tests' folder.
    """
    os.makedirs("../tests/random_graphs", exist_ok=True)
    os.makedirs("../tests/complete_graphs", exist_ok=True)
    os.makedirs("../tests/cycle_graphs", exist_ok=True)
    # os.makedirs("../tests/bipartite_graphs", exist_ok=True)
    os.makedirs("../tests/path_graph", exist_ok=True)
    os.makedirs("../tests/grid_graph", exist_ok=True)

    test_cases = []
    # Random graphs
    count = 1
    for i in range(1, 10):
        probabilities = numpy.linspace(0.5, 1, 5) 
        for j, probability in enumerate(probabilities, start=1):
            test_cases.append((f"random_graphs/test{count}", i, generate_random_graph(i, probability)))
            count += 1
                          
    # Complete graphs
    for i in range(1, 10):
        test_cases.append((f"complete_graphs/test{i}", i, generate_complete_graph(i)))

    # Cycle graphs
    for i in range(10, 20):
        test_cases.append((f"cycle_graphs/test{i - 9}", i, generate_cycle_graph(i)))

    # Bipartite graphs
    # for i in range(1, 20):
    #     num_nodes_set1 = random.randint(0, i)
    #     num_nodes_set2 = i - num_nodes_set1
    #     test_cases.append((f"bipartite_graphs/test{i}", i, generate_bipartite_graph(num_nodes_set1, num_nodes_set2)))

    # Path graphs
    for i in range(1, 50):
        test_cases.append((f"path_graph/test{i}", i, generate_path_graph(i)))

    # Grid graphs
    for i in range(1, 30):
        test_cases.append((f"grid_graph/test{i}", i * i, generate_grid_graph(i, i)))


    for name, nodes, edges in test_cases:
        file_name = f"../tests/{name}.in"
        generate_test(file_name, nodes, edges)
        print(f"Generated {file_name}")

if __name__ == "__main__":
    generate_all_tests()
