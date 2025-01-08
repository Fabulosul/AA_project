import random
import os

def generate_test(file_name, num_nodes, edges):
    """
    Generates a graph with the given parameters and saves it to a file.
    """
    with open(file_name, 'w') as file:
        file.write(f"{num_nodes} {len(edges)}\n")
        for u, v in edges:
            file.write(f"{u} {v}\n")

def generate_complete_graph(num_nodes):
    edges = [(i, j) for i in range(num_nodes) for j in range(i + 1, num_nodes)]
    return edges

def generate_bipartite_graph(set1_size, set2_size):
    edges = [(i, j) for i in range(set1_size) for j in range(set1_size, set1_size + set2_size)]
    return edges

def generate_cycle_graph(num_nodes):
    edges = [(i, (i + 1) % num_nodes) for i in range(num_nodes)]
    return edges

def generate_tree_graph(num_nodes):
    edges = [(i, random.randint(0, i - 1)) for i in range(1, num_nodes)]
    return edges

def generate_star_graph(num_nodes):
    edges = [(0, i) for i in range(1, num_nodes)]
    return edges

def generate_grid_graph(rows, cols):
    edges = []
    for r in range(rows):
        for c in range(cols):
            node = r * cols + c
            if c < cols - 1:
                edges.append((node, node + 1))  # Right
            if r < rows - 1:
                edges.append((node, node + cols))  # Down
    return edges

def generate_random_graph(num_nodes, density):
    max_edges = num_nodes * (num_nodes - 1) // 2
    num_edges = int(max_edges * density)
    edges = set()
    while len(edges) < num_edges:
        u, v = random.sample(range(num_nodes), 2)
        if u > v:
            u, v = v, u
        edges.add((u, v))
    return list(edges)

def generate_adversarial_graph(num_nodes):
    edges = []
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if abs(i - j) != 1:  # Skip consecutive nodes
                edges.append((i, j))
    return edges

def generate_tests():
    os.makedirs("tests", exist_ok=True)

    # test_cases = [
        # Basic tests
        # ("test1_dense", 5, generate_complete_graph(5)),
        # ("test2_sparse", 5, [(0, 1), (1, 2)]),
        # ("test3_bipartite", 10, generate_bipartite_graph(5, 5)),
        # ("test4_cycle", 10, generate_cycle_graph(10)),
        # ("test5_tree", 50, generate_tree_graph(50)),
        # ("test6_star", 250, generate_star_graph(250)),
        # ("test7_grid", 400, generate_grid_graph(20, 20)),

        # # Larger tests for scalability
        # ("test8_large_dense", 100, generate_complete_graph(100)),
        # ("test9_large_sparse", 100, generate_random_graph(100, 0.1)),
        # ("test10_large_bipartite", 100, generate_bipartite_graph(50, 50)),

        # # Adversarial cases
        # ("test11_adversarial", 20, generate_adversarial_graph(20)),
        # ("test12_worst_case_greedy", 10, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]),

        # # Randomized cases
        # ("test13_random_dense", 50, generate_random_graph(50, 0.8)),
        # ("test14_random_sparse", 50, generate_random_graph(50, 0.2)),

        # Stress tests
        
    # ]
    test_cases = []
    for i in range(10, 15):
        
        test_cases.append(("test" + f"{i - 9}" + "_stress", i, generate_random_graph(i, 0.2)))

    for name, nodes, edges in test_cases:
        file_name = f"tests/{name}.in"
        generate_test(file_name, nodes, edges)
        print(f"Generated {file_name}")

if __name__ == "__main__":
    generate_tests()
