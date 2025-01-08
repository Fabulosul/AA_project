def add_edge(graph, u, v):
    """Adauga o muchie intre nodul u si nodul v in lista de adiacenta."""
    graph[u].append(v)
    graph[v].append(u)

def is_safe(graph, v, node_colors, color):
    """Verifica daca este posibil sa se atribuie culoarea color nodului v."""
    for neighbour in graph[v]:
        if node_colors[neighbour] == color:
            return False
    return True

def graph_colour_util(graph, nr_colors, node_colors, u):
    """Functie auxiliara recursiva pentru a rezolva problema colorarii."""
    # Daca toate nodurile sunt colorate, returnam True
    if u == len(graph):
        return True

    # Incercam fiecare culoare de la 0 la nr_colors-1
    for color in range(nr_colors):
        if is_safe(graph, u, node_colors, color):
            node_colors[u] = color
            if graph_colour_util(graph, nr_colors, node_colors, u + 1):
                return True
            node_colors[u] = -1  # Resetam culoarea daca nu se potriveste

    return False

def graph_colouring(graph):
    """Determina numarul minim de culori necesare si returneaza vectorul de culori."""
    nr_nodes = len(graph)
    node_colors = [-1] * nr_nodes

    # Incepem cu o singura culoare si crestem pana gasim o solutie valida
    for nr_colors in range(1, nr_nodes + 1):
        if graph_colour_util(graph, nr_colors, node_colors, 0):
            return nr_colors, node_colors