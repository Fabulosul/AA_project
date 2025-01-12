import time
import os
import subprocess
from colorama import init, Fore, Style
from algorithms.welsh_powell_graph_coloring import add_edge as add_edge_wp, graph_coloring_welsh_powell as wp_coloring
from algorithms.greedy_graph_coloring import add_edge as add_edge_greedy, greedy_coloring as greedy_coloring
from algorithms.backtracking_graph_coloring import add_edge as add_edge_backtracking, graph_colouring as backtracking_coloring

# Initialize colorama
init(autoreset=True)

def read_graph_from_file(filename, add_edge_func):
    '''Reads graph data from a file and returns a list of graphs and number of colors'''
    graphs = []
    num_nodes = None
    num_edges = None
    with open(filename, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if lines[i].startswith("#") or not lines[i].strip():
                i += 1
                continue  # Skip comments or empty lines

            num_nodes, num_edges = map(int, lines[i].split())
            graph = [[] for _ in range(num_nodes)]
            i += 1
            for _ in range(num_edges):
                u, v = map(int, lines[i].split())
                add_edge_func(graph, u, v)
                i += 1
            graphs.append(graph)
    return graphs, num_nodes, num_edges

def measure_time(graph_coloring_function, graph, nr_runs=10):
    '''Measures the execution time of the graph_coloring function'''
    times = []
    for _ in range(nr_runs):
        start_time = time.perf_counter()
        nr_colors, node_colors = graph_coloring_function(graph)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    average_time = sum(times) / len(times)
    return average_time, nr_colors

def process_test_directory(directory):
    '''Processes all test files in a given directory and its subdirectories'''
    results = []
    chromatic_numbers = {}

    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".in"):  # Only process .in files
                filepath = os.path.join(root, filename)
                print(f"\nProcessing file: {Fore.CYAN}{filepath}{Style.RESET_ALL}")
                
                # Backtracking (calculate chromatic number first)
                graphs_backtracking, num_nodes, num_edges = read_graph_from_file(filepath, add_edge_backtracking)
                for i, graph in enumerate(graphs_backtracking):
                    print(f"  Running {Fore.YELLOW}Backtracking{Style.RESET_ALL} graph coloring on graph {i + 1}")
                    exec_time, chromatic_number = measure_time(backtracking_coloring, graph)
                    print(f"  Chromatic Number: {Fore.MAGENTA}{chromatic_number}{Style.RESET_ALL} after {exec_time:.12f} seconds.")
                    chromatic_numbers[(filename, i + 1)] = chromatic_number
                    results.append((filename, i + 1, "Backtracking", exec_time, "PASSED", num_nodes, num_edges, chromatic_number))

                # Welsh-Powell
                graphs_wp, _, _ = read_graph_from_file(filepath, add_edge_wp)
                for i, graph in enumerate(graphs_wp):
                    print(f"  Running {Fore.YELLOW}Welsh-Powell{Style.RESET_ALL} graph coloring on graph {i + 1}")
                    exec_time, num_colors = measure_time(wp_coloring, graph)
                    chromatic_number = chromatic_numbers.get((filename, i + 1), float('inf'))
                    status = "PASSED" if num_colors == chromatic_number else "FAILED"
                    print(f"  Test {Fore.GREEN if status == 'PASSED' else Fore.RED}{status}{Style.RESET_ALL} after {exec_time:.12f} seconds.")
                    results.append((filename, i + 1, "Welsh-Powell", exec_time, status, num_nodes, num_edges, num_colors))
                
                # Greedy
                graphs_greedy, _, _ = read_graph_from_file(filepath, add_edge_greedy)
                for i, graph in enumerate(graphs_greedy):
                    print(f"  Running {Fore.YELLOW}Greedy{Style.RESET_ALL} Algorithm on graph {i + 1}")
                    exec_time, num_colors = measure_time(greedy_coloring, graph)
                    chromatic_number = chromatic_numbers.get((filename, i + 1), float('inf'))
                    status = "PASSED" if num_colors == chromatic_number else "FAILED"
                    print(f"  Test {Fore.GREEN if status == 'PASSED' else Fore.RED}{status}{Style.RESET_ALL} after {exec_time:.12f} seconds.")
                    results.append((filename, i + 1, "Greedy", exec_time, status, num_nodes, num_edges, num_colors))

    return results


def save_results_by_algorithm(results, output_directory):
    '''Saves the results into separate files for each algorithm, including chromatic number.'''
    os.makedirs(output_directory, exist_ok=True)

    # Extract chromatic numbers from backtracking results
    chromatic_numbers = {}
    for result in results:
        filename, graph_num, algorithm, exec_time, status, num_nodes, num_edges, num_colors = result
        if algorithm == "Backtracking":
            chromatic_numbers[(filename, graph_num)] = num_colors

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
        chromatic_number = chromatic_numbers.get((filename, graph_num), "N/A")  # Default to "N/A" if not available
        entry = {
            "filename": filename,
            "graph_num": graph_num,
            "num_nodes": num_nodes,
            "num_edges": num_edges,
            "num_edges_and_nodes": num_nodes + num_edges,
            "num_colors": num_colors,
            "chromatic_number": chromatic_number,
            "execution_time": exec_time,
            "status": status
        }
        algorithm_data[algorithm].append(entry)

    for algorithm, data in algorithm_data.items():
        # Sort data by filename (numeric order) and then by graph number
        data.sort(key=lambda x: (extract_numeric_part(x['filename']), x['graph_num']))
        
        new_dir = os.path.join(output_directory, algorithm)
        os.makedirs(new_dir, exist_ok=True)
        output_file = os.path.join(new_dir, f"{algorithm}_results.txt")

        with open(output_file, "w") as file:
            file.write("Filename,Nodes,Edges,Nodes + Edges,Colors,Chromatic Number,Execution Time (s),Status\n")
            for entry in data:
                file.write(
                    f"{entry['filename']},{entry['num_nodes']},{entry['num_edges']},"
                    f"{entry['num_edges_and_nodes']},{entry['num_colors']},{entry['chromatic_number']},"
                    f"{entry['execution_time']:.12f},{entry['status']}\n"
                )

        print(f"Results written to {output_file}")

def run_main():
    test_directory = "../tests"  # Directory containing test files
    results_directory = "results"  # Directory to save results

    if not os.path.isdir(test_directory):
        print(f"Directory {test_directory} not found!")
    else:
        for subdir in os.listdir(test_directory):
            subdir_path = os.path.join(test_directory, subdir)
            if os.path.isdir(subdir_path):
                # Process all test files in the subdirectory and collect results
                results = process_test_directory(subdir_path)

                # Create results directory for the subdirectory if it doesn't exist
                subdir_results_directory = os.path.join(results_directory, subdir)
                os.makedirs(subdir_results_directory, exist_ok=True)

                # Sort results by filename (numeric order) and then by graph number
                def extract_numeric_part(filename):
                    '''Extracts the numeric part of a filename for correct sorting'''
                    import re
                    match = re.search(r'\d+', filename)
                    return int(match.group()) if match else float('inf')

                results.sort(key=lambda x: (extract_numeric_part(x[0]), x[1]))

                # Save sorted results to a summary file
                summary_file = os.path.join(subdir_results_directory, "results_summary.txt")
                with open(summary_file, "w") as output_file:
                    output_file.write("Filename,Algorithm,Nodes,Edges,Execution Time (s),Status,Colors\n")
                    for filename, test_num, algorithm, exec_time, status, num_nodes, num_edges, colors in results:
                        output_file.write(f"{filename} | {algorithm} | {num_nodes} | {num_edges} | {exec_time:.12f} | {status} | {colors}\n")
                print(f"\nResults summary saved to {summary_file}")

                # Save organized results by algorithm
                save_results_by_algorithm(results, subdir_results_directory)

if __name__ == "__main__":
    run_main()