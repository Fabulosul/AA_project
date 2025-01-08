import time
import os
import shutil
from colorama import init, Fore, Style
from algorithms.welsh_powell_graph_coloring import add_edge as add_edge_wp, graph_coloring as wp_coloring
from algorithms.greedy_graph_coloring import addEdge as add_edge_greedy, greedyColoring as greedy_coloring
from algorithms.backtracking_graph_coloring import add_edge as add_edge_backtracking, graph_colouring as backtracking_coloring

# Initialize colorama
init(autoreset=True)

def read_graph_from_file(filename, add_edge_func):
    '''Reads graph data from a file and returns a list of graphs and number of colors'''
    graphs = []
    num_colors = None
    num_nodes = None
    num_edges = None
    with open(filename, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if lines[i].startswith("#") or not lines[i].strip():
                i += 1
                continue  # Skip comments or empty lines

            num_nodes, num_edges, num_colors = map(int, lines[i].split())
            graph = [[] for _ in range(num_nodes)]
            i += 1
            for _ in range(num_edges):
                u, v = map(int, lines[i].split())
                add_edge_func(graph, u, v)
                i += 1
            graphs.append(graph)
    return graphs, num_colors, num_nodes, num_edges

def measure_time(graph_coloring_function, graph, nr_nodes=None):
    '''Measures the execution time of the graph_coloring function'''
    start_time = time.time()
    if nr_nodes is not None:
        result = graph_coloring_function(graph, nr_nodes)
    else:
        result = graph_coloring_function(graph)
    end_time = time.time()
    return end_time - start_time, result

def process_test_directory(directory):
    '''Processes all test files in a given directory'''
    results = []
    for filename in os.listdir(directory):
        if filename.endswith(".in"):  # Only process .in files
            filepath = os.path.join(directory, filename)
            print(f"\nProcessing file: {Fore.CYAN}{filepath}{Style.RESET_ALL}")
            
            # Welsh-Powell
            graphs_wp, num_colors, num_nodes, num_edges = read_graph_from_file(filepath, add_edge_wp)
            for i, graph in enumerate(graphs_wp):
                print(f"  Running {Fore.YELLOW}Welsh-Powell{Style.RESET_ALL} graph coloring on graph {i + 1}")
                exec_time, result = measure_time(wp_coloring, graph)
                status = "PASSED" if result else "FAILED"
                print(f"  Test {Fore.GREEN if result else Fore.RED}{status}{Style.RESET_ALL} after {Fore.MAGENTA}{exec_time:.12f}{Style.RESET_ALL} seconds.")
                results.append((filename, i + 1, "Welsh-Powell", exec_time, status, num_nodes, num_edges, num_colors))
            
            # Greedy
            graphs_greedy, num_colors, num_nodes, num_edges = read_graph_from_file(filepath, add_edge_greedy)
            for i, graph in enumerate(graphs_greedy):
                print(f"  Running {Fore.YELLOW}Greedy{Style.RESET_ALL} Algorithm on graph {i + 1}")
                exec_time, result = measure_time(greedy_coloring, graph, len(graph))
                status = "PASSED" if result else "FAILED"
                print(f"  Test {Fore.GREEN if result else Fore.RED}{status}{Style.RESET_ALL} after {Fore.MAGENTA}{exec_time:.12f}{Style.RESET_ALL} seconds.")
                results.append((filename, i + 1, "Greedy", exec_time, status, num_nodes, num_edges, num_colors))
            
            # Backtracking
            graphs_backtracking, num_colors, num_nodes, num_edges = read_graph_from_file(filepath, add_edge_backtracking)
            for i, graph in enumerate(graphs_backtracking):
                print(f"  Running {Fore.YELLOW}Backtracking{Style.RESET_ALL} graph coloring on graph {i + 1}")
                exec_time, result = measure_time(backtracking_coloring, graph, num_colors)
                status = "PASSED" if result else "FAILED"
                print(f"  Test {Fore.GREEN if result else Fore.RED}{status}{Style.RESET_ALL} after {Fore.MAGENTA}{exec_time:.12f}{Style.RESET_ALL} seconds.")
                results.append((filename, i + 1, "Backtracking", exec_time, status, num_nodes, num_edges, num_colors))
    
    return results

def delete_pycache(directory):
    '''Deletes the __pycache__ directory if it exists'''
    pycache_path = os.path.join(directory, '__pycache__')
    if os.path.exists(pycache_path) and os.path.isdir(pycache_path):
        shutil.rmtree(pycache_path)
        print(f"Deleted {pycache_path}")

def save_results_by_algorithm(results, output_directory):
    '''Saves the results into separate files for each algorithm'''
    os.makedirs(output_directory, exist_ok=True)

    def extract_numeric_part(filename):
        '''Extracts the numeric part of a filename for correct sorting'''
        import re
        match = re.search(r'\d+', filename)
        return int(match.group()) if match else float('inf')

    algorithm_data = {
        "Welsh-Powell": [],
        "Greedy": [],
        "Backtracking": []
    }

    for result in results:
        filename, graph_num, algorithm, exec_time, status, num_nodes, num_edges, num_colors = result
        entry = {
            "filename": filename,
            "graph_num": graph_num,
            "num_nodes": num_nodes,
            "num_edges": num_edges,
            "num_edges_and_nodes": num_nodes + num_edges,
            "num_colors": num_colors,
            "execution_time": exec_time,
            "status": status
        }
        algorithm_data[algorithm].append(entry)

    for algorithm, data in algorithm_data.items():
        # Sort data by filename (numeric order) and then by graph number
        data.sort(key=lambda x: (extract_numeric_part(x['filename']), x['graph_num']))
        
        new_dir = output_directory + "/" + f"{algorithm}"
        os.makedirs(new_dir, exist_ok=True)
        output_file = os.path.join(new_dir, f"{algorithm}_results.txt")

        with open(output_file, "w") as file:
            # file.write(f"Results for {algorithm} Algorithm:\n")
            file.write("Filename,Nodes,Edges,Nodes + Edges,Colors,Execution Time (s),Status\n")
            # file.write("-" * 90 + "\n")

            for entry in data:
                file.write(f"{entry['filename']},{entry['num_nodes']},{entry['num_edges']},{entry['num_edges_and_nodes']},{entry['num_colors']},{entry['execution_time']:.12f},{entry['status']}\n")

        print(f"Results written to {output_file}")


if __name__ == "__main__":
    # Delete __pycache__ directories
    delete_pycache('algorithms')

    test_directory = "tests"  # Directory containing test files
    results_directory = "results"  # Directory to save results

    if not os.path.isdir(test_directory):
        print(f"Directory {test_directory} not found!")
    else:
        # Process all test files and collect results
        results = process_test_directory(test_directory)

        # Create results directory if it doesn't exist
        os.makedirs(results_directory, exist_ok=True)

        # Sort results by filename (numeric order) and then by graph number
        def extract_numeric_part(filename):
            '''Extracts the numeric part of a filename for correct sorting'''
            import re
            match = re.search(r'\d+', filename)
            return int(match.group()) if match else float('inf')

        results.sort(key=lambda x: (extract_numeric_part(x[0]), x[1]))

        # Save sorted results to a summary file
        summary_file = os.path.join(results_directory, "results_summary.txt")
        with open(summary_file, "w") as output_file:
            output_file.write("Filename,Algorithm,Nodes,Edges,Colors,Execution Time (s),Status\n")
            output_file.write("-" * 90 + "\n")
            for filename, test_num, algorithm, exec_time, status, num_nodes, num_edges, num_colors in results:
                output_file.write(f"{filename} | {algorithm} | {num_nodes} | {num_edges} | {num_colors} | {exec_time:.12f} | {status}\n")
        print(f"\nResults summary saved to {summary_file}")

        # Save organized results by algorithm
        save_results_by_algorithm(results, results_directory)
