def add_edge(graph, u, v):
    '''Adaugă o muchie între nodurile "u" și "v"'''
    graph[u].append(v)
    graph[v].append(u)

def has_edge(graph, u, v):
    '''Verifică dacă există o muchie între nodurile "u" și "v"'''
    return v in graph[u]

def graph_coloring_welsh_powell(graph):
    '''Colorează graful folosind algoritmul Welsh-Powell'''
    nr_nodes = len(graph)
    node_color = [-1] * nr_nodes

    # Calculeaza gradele și sorteaza nodurile descrescător după grad
    degrees = sorted(range(nr_nodes), key=lambda u: len(graph[u]), reverse=True)

    color_set = []

    # Repetă până toate nodurile sunt colorate
    for node in degrees:
        if node_color[node] == -1:  # Nod necolorat
            current_color = len(color_set)  # Atribuie o nouă culoare
            color_set.append(current_color)
            
            # Colorează nodurile ce pot fi colorate cu aceeași culoare
            for v in degrees:
                if node_color[v] == -1 and all(node_color[neighbor] != current_color for neighbor in graph[v]):
                    node_color[v] = current_color

    return len(color_set), node_color
