import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# List of .csv and directory path where all the data will be saved
# Example of object (as a tuple): (file_path, out_dir_path, graph_colour, graph_label)
all_graphs = []
common_graph_path = "results/Overlaped.png"

# Just append your files here
file_path_one = "results/Backtracking/Backtracking_results.txt"
out_dir_one = "results/Backtracking/Backtracking_graph.png"
all_graphs.append((file_path_one, out_dir_one, "green", "Backtracking"))

file_path_two = "results/Greedy/Greedy_results.txt"
out_dir_two = "results/Greedy/Greedy_graph.png"
all_graphs.append((file_path_two, out_dir_two, "blue", "Greedy"))

file_path_three = "results/Welsh-Powell/Welsh-Powell_results.txt"
out_dir_three = "results/Welsh-Powell/Welsh-Powell_graph.png"
all_graphs.append((file_path_three, out_dir_three, "orange", "Welsh-Powell"))
# End of appending objects

class Plots():
    def __init__(self, all_graphs, common_dir_path):
        self.all_graphs = all_graphs
        self.common_dir_path = common_dir_path
                
    def make_graphs(self):
        for path in self.all_graphs:
            self.make_single_graph(path)
            
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
        plt.figure(figsize=(10, 6))
        plt.title("Graph Coloring Complexity: Execution Time vs Nodes")
        plt.xlabel("Number of Nodes + Edgess")
        plt.ylabel("Execution Time (seconds)")
        plt.grid(True)
        
        for path in self.all_graphs:
            self.add_to_plot(path)
        
        plt.legend()
        plt.tight_layout()
        plt.savefig(self.common_dir_path, format='png', dpi=300)
    
    def add_to_plot(self, path):
        file_path = path[0]
        my_color = path[2]
        my_label = path[3]

        df = pd.read_csv(file_path)
        columns_needed = ["Nodes + Edges", "Execution Time (s)"]
        data = df[columns_needed]
    
        sns.lineplot(data=data, x="Nodes + Edges", y="Execution Time (s)",
                     marker="o", color=my_color, label=my_label)


__all__ = ['Plots', 'all_paths']