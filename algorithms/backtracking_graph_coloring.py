def add_edge(graph, u, v):
    """ Adauga o muchie intre nodul u si nodul v in lista de adiacenta. """
    graph[u].append(v)
    graph[v].append(u)

def print_graph(node_colors):
    """ Printeaza culorile fiecarui nod """
    node_index = 0
    for colour in node_colors:
        print("Nodul", node_index , "are culoarea", colour)
        node_index += 1

def is_safe(graph, v, node_colors, colour):
    """ Verifica daca este posibil sa se atribuie culoarea c nodului v. """
    for neighbour in graph[v]:
        if node_colors[neighbour] == colour:
            return False
    return True

def graph_colour_util(graph, nr_colours, node_colors, u):
    """ Functie auxiliara recursiva pentru a rezolva problema colorarii cu nr_colours. """
    # Daca a ramas o singura culoare si un singur nod de colorat
    # atunci coloram nodul si returnam True
    if u == len(graph): 
        return True

    for colour in range(0, nr_colours):
        if is_safe(graph, u, node_colors, colour):
            node_colors[u] = colour
            if graph_colour_util(graph, nr_colours, node_colors, u + 1):
                return True
            node_colors[u] = 0  # Daca nu a fost posibila colorarea nodului u, resetam culoarea

    return False

def graph_colouring(graph, nr_colours):
    """ Rezolva problema colorarii cu nr_colours. """
    node_colors = [-1] * len(graph)  # Initializeaza culorile nodurilor cu -1

    if not graph_colour_util(graph, nr_colours, node_colors, 0):
        return False

    return True
