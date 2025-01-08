import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# List of .csv and directory path where all the data will be saved
# Example of object (as a tuple): (file_path, out_dir_path)
all_paths = []

# Just append your files here
file_path_one = "results/Backtracking/Backtracking_results.txt"
out_dir_one = "results/Backtracking/Backtracking_graph.png"
all_paths.append((file_path_one, out_dir_one))

file_path_two = "results/Greedy/Greedy_results.txt"
out_dir_two = "results/Greedy/Greedy_graph.png"
all_paths.append((file_path_two, out_dir_two))

file_path_three = "results/Welsh-Powell/Welsh-Powell_results.txt"
out_dir_three = "results/Welsh-Powell/Welsh-Powell_graph.png"
all_paths.append((file_path_three, out_dir_three))
# End of appending objects

class Plots():
    def __init__(self, all_paths):
        self.all_paths = all_paths
                
    def make_graphs(self):
        for path in self.all_paths:
            self.make_single_graph(path)
            
    def make_single_graph(self, path):
        file_path = path[0]
        dir_path = path[1]

        df = pd.read_csv(file_path)
        columns_needed = ["Nodes + Edges", "Execution Time (s)"]
        data = df[columns_needed]
        
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data, x="Nodes + Edges", y="Execution Time (s)", marker="o", label="Execution Time")

        plt.title("Graph Coloring Complexity: Execution Time vs Nodes")
        plt.xlabel("Number of Nodes + Edgess")
        plt.ylabel("Execution Time (seconds)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        plt.savefig(dir_path, format='png', dpi=300)


__all__ = ['Plots', 'all_paths']