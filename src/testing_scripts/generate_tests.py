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

def generate_all_tests():
    """
    Generates test cases and saves them in the 'tests' folder.
    """
    os.makedirs("../tests/random_graphs", exist_ok=True)
    os.makedirs("../tests/complete_graphs", exist_ok=True)

    test_cases = []
    # Random graphs
    for i in range(1, 15):
        probabilities = numpy.linspace(0, 0.3, 100)
        for j, probability in enumerate(probabilities, start=1):
            test_cases.append((f"random_graphs/test{(i-1)*1000 + j}", i, generate_random_graph(i, probability)))
                          


    # Complete graphs
    for i in range(1, 10):
        test_cases.append((f"complete_graphs/test{i}", i, generate_complete_graph(i)))



    for name, nodes, edges in test_cases:
        file_name = f"../tests/{name}.in"
        generate_test(file_name, nodes, edges)
        print(f"Generated {file_name}")

if __name__ == "__main__":
    generate_all_tests()
