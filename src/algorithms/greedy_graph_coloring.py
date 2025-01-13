# Adauga o muchie intre nodurile u si v
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)
    return graph

def greedy_coloring(graph):
    # Initializam un vector ce retine culoarea finala a fiecarui nod
    nr_nodes = len(graph)
    colored_graph = [-1] * nr_nodes

    # Initializam primul nod cu culoarea 0
    colored_graph[0] = 0

    # Initializam un vector care retine daca o culoare
    # este disponibila sau nu pentru un anumit nod
    available_colors = [True] * nr_nodes

    # Procesam toate nodurile
    for u in range(nr_nodes):
        # Marcam culorile vecinilor ca indisponibile
        for i in graph[u]:
            if colored_graph[i] != -1:
                available_colors[colored_graph[i]] = False

        # Gasim prima culoare disponibila
        color_index = 0
        while color_index < nr_nodes:
            if available_colors[color_index]:
                break
            color_index += 1

        # Coloram nodul u cu culoarea gasita
        colored_graph[u] = color_index

        # Resetam vectorul de culori disponibile pentru urmatoarea iteratie
        available_colors = [True] * nr_nodes

    # Calculam numarul de culori utilizate
    nr_colors = max(colored_graph) + 1

    return nr_colors, colored_graph