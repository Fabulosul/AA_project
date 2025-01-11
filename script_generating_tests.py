


import random
import os
import networkx as nx
from networkx.generators import null_graph
from networkx.generators import cycle_graph
from networkx.generators import complete_graph
from networkx.generators import ladder_graph
from networkx.generators import circular_ladder_graph
from networkx.generators import dorogovtsev_goltsev_mendes_graph
from networkx.generators import complete_multipartite_graph
from networkx.generators.random_graphs import erdos_renyi_graph

random.seed(169)

def generate_random_graph():
    
    num_vertexes = random.randint(1, 15)
    p = random.uniform(0, 0.6)
    graph = erdos_renyi_graph(num_vertexes, p)
    return graph

def generate_random_cycles_graph():
    num_vertexes = random.randint(1, 15)
    graph = cycle_graph(num_vertexes)
    return graph

def generate_random_complete_graph():
    num_vertexes = random.randint(1, 6)
    graph = complete_graph(num_vertexes)
    return graph

def generate_random_ladder_graph():
    num_vertexes = random.randint(1, 15)
    graph = ladder_graph(num_vertexes)
    return graph

def generate_random_circulant_ladder_graph():
    num_vertexes = random.randint(1, 8) # will generate 2 * n vertexes
    graph = circular_ladder_graph(num_vertexes)
    return graph

# def generate_random_dgm_graph():
#     num_vertexes = random.randint(2, 4)
#     graph = dorogovtsev_goltsev_mendes_graph(num_vertexes)
#     return graph

def generate_random_multipartite_graph():
    num_of_partitions = random.randint(2, 20)
    sizes = []
    for i in range(num_of_partitions):
        sizes.append(random.randint(2, 20))

    graph = complete_multipartite_graph(*sizes)
    return graph, num_of_partitions

def generate_big_graph():
    k = random.randint(2, 20)   
    
    G = nx.Graph()

    clique_nodes = list(range(k))
    G.add_nodes_from(clique_nodes)
    for i in range(k):
        for j in range(i + 1, k):
            G.add_edge(i, j)
    
    num_additional_nodes = random.randint(0, 30)
    total_nodes = k + num_additional_nodes
    for new_node in range(k, total_nodes):
        G.add_node(new_node)

        num_edges = random.randint(1, k)
        neighbors = random.sample(range(total_nodes), num_edges)
        for neighbor in neighbors:
            G.add_edge(new_node, neighbor)
    
    while len(set(nx.algorithms.coloring.greedy_color(G, strategy="largest_first").values())) < k:
        additional_node = total_nodes
        total_nodes += 1
        G.add_node(additional_node)
        for i in range(k - 1):
            G.add_edge(additional_node, random.choice(list(G.nodes)))
    
    return G, k

def write_graph_to_files(graph, filename=""):
    with open(filename, "w") as file:
            file.write(f"{graph.number_of_nodes()} {graph.number_of_edges()}\n")
            for source, destination in graph.edges():
                file.write(f"{source} {destination}\n")
                
def write_kgraph_to_files(graph, k ,filename=""):
    with open(filename, "w") as file:
            file.write(f"{graph.number_of_nodes()} {graph.number_of_edges()}\n")
            for source, destination in graph.edges():
                file.write(f"{source} {destination}\n")
            file.write(f"{k}\n")
if _name_ == "_main_":

    input_folder = './tests/input'

    if not os.path.exists(input_folder):
        os.makedirs(input_folder)

    my_graph = null_graph()
    filename = "test_graph_coloring0.in"
    write_graph_to_files(my_graph, os.path.join(input_folder, filename))

    for i in range(1, 2000):
        my_graph = generate_random_graph()
        filename = f"test_graph_coloring{i}.in"
        write_graph_to_files(my_graph, os.path.join(input_folder, filename))

    for i in range(2000, 2020):
        my_graph = generate_random_cycles_graph()
        filename = f"test_graph_coloring{i}.in"
        write_graph_to_files(my_graph, os.path.join(input_folder, filename))

    for i in range(2020, 2030):
        my_graph = generate_random_complete_graph()
        filename = f"test_graph_coloring{i}.in"
        write_graph_to_files(my_graph, os.path.join(input_folder, filename))

    for i in range(2030, 2040): 
        my_graph = generate_random_ladder_graph()
        filename = f"test_graph_coloring{i}.in"
        write_graph_to_files(my_graph, os.path.join(input_folder, filename))

    for i in range(2040, 2050):
        my_graph = generate_random_circulant_ladder_graph()
        filename = f"test_graph_coloring{i}.in"
        write_graph_to_files(my_graph, os.path.join(input_folder, filename))

    # for i in range(40, 45):
    #     my_graph = generate_random_dgm_graph()
    #     filename = f"test_graph_coloring{i}.in"
    #     write_graph_to_files(my_graph, os.path.join(input_folder, filename))

    for i in range(2050, 3050):
        my_graph, num_of_partitions = generate_big_graph()
        filename = f"test_graph_coloring{i}.in"
        write_kgraph_to_files(my_graph, num_of_partitions ,os.path.join(input_folder, filename))