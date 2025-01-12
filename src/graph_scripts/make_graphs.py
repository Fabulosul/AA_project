import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# List of .csv and directory path where all the data will be saved
# Example of object (as a tuple): (file_path, out_dir_path, graph_colour, graph_label)
common_graph_path = "results/Overlaped.png"


root = "results/"
bkt = "/Backtracking/Backtracking_results.txt"
welsh = "/Welsh-Powell/Welsh-Powell_results.txt"
greedy = "/Greedy/Greedy_results.txt"

out_bkt = "/Backtracking/Backtracking_graph.png"
out_greedy = "/Greedy/Greedy_graph.png"
out_welsh = "/Welsh-Powell/Welsh-Powell_graph.png"

overlapped_graphic = "/Overlapped.png"

class Plots():
    def __init__(self, top_directory):
        all_graphs = []

        a, directories, _ = next(os.walk(top_directory))
        for directory in directories:
            common_dir_path = root + directory + overlapped_graphic
            pathBkt = root + directory + bkt
            outPathBkt = root + directory + out_bkt
            bktTuple = (pathBkt, outPathBkt, "green", "Backtracking")

            pathWelsh = root + directory + welsh
            outPathWelsh = root + directory + out_welsh
            welshTupple = (pathWelsh, outPathWelsh, "blue", "Welsh-Powell")

            pathGreedy = root + directory + greedy
            outPathGreedy = root + directory + out_greedy
            greedyTuple = (pathGreedy, outPathGreedy, "orange", "Greedy")

            all_graphs.append((bktTuple, welshTupple, greedyTuple, common_dir_path))

        self.all_graphs = all_graphs

    def make_graphs(self):
        for graphs in self.all_graphs:
            self.make_single_graph(graphs[0])
            self.make_single_graph(graphs[1])
            self.make_single_graph(graphs[2])
            
    def make_single_graph(self, graph):
        file_path = graph[0]
        dir_path = graph[1]

        df = pd.read_csv(file_path)
        columns_needed = ["Nodes + Edges", "Execution Time (s)"]
        data = df[columns_needed]
        
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data, x="Nodes + Edges", y="Execution Time (s)", marker="o", label="Execution Time")

        plt.title("Graph Coloring Complexity: Execution Time vs Nodes")
        plt.xlabel("Number of Nodes + Edges")
        plt.ylabel("Execution Time (seconds)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        plt.savefig(dir_path, format='png', dpi=300)
    
    def make_overlapped_graphs(self):
        
        for graphs in self.all_graphs:
            plt.figure(figsize=(10, 6))
            plt.title("Graph Coloring Complexity: Execution Time vs Nodes")
            plt.xlabel("Number of Nodes + Edgess")
            plt.ylabel("Execution Time (seconds)")
            plt.grid(True)
            
            self.add_to_plot(graphs[0])
            self.add_to_plot(graphs[1])
            self.add_to_plot(graphs[2])
        
            plt.legend()
            plt.tight_layout()
            plt.savefig(graphs[3], format='png', dpi=300)
            plt.close()
    
    def add_to_plot(self, path):
        file_path = path[0]
        my_color = path[2]
        my_label = path[3]

        df = pd.read_csv(file_path)
        columns_needed = ["Nodes + Edges", "Execution Time (s)"]
        #columns_needed = ["Edges", "Execution Time (s)"]
        data = df[columns_needed]

        sns.lineplot(data=data, x="Nodes + Edges", y="Execution Time (s)",
                     marker="o", color=my_color, label=my_label)
        #sns.lineplot(data=data, x="Edges", y="Execution Time (s)",
        #             marker="o", color=my_color, label=my_label)

__all__ = ['Plots', 'all_paths']