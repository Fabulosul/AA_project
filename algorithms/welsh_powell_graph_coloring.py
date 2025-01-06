def add_edge(graph, u, v):
    '''Adaugă o muchie între nodurile "u" și "v"'''
    graph[u].append(v)
    graph[v].append(u)

def has_edge(graph, u, v):
    '''Verifică dacă există o muchie între nodurile "u" și "v"'''
    return v in graph[u]

def neighbors_same_color(graph, node_color, u, color):
    '''Verifică dacă nodul "u" are vecini colorați cu aceeași culoare cu cea dată "color"'''
    for neighbour in graph[u]:
        if node_color[neighbour] == color:
            return True
    return False

def graph_coloring(graph):
    '''Colorează un graf folosind algoritmul Welsh-Powell'''
    nr_nodes = len(graph)

    # Vector pentru culorile nodurilor
    node_color = [-1] * nr_nodes

    # Calculează gradele și le asociază cu nodurile
    node_degrees = [None] * nr_nodes
    for u in range(nr_nodes):
        node_degrees[u] = (u, len(graph[u]))
    
    # Sortează nodurile descrescător după grad
    node_degrees.sort(key=lambda x: x[1], reverse=True)
    
    # Vector pentru culorile existente
    colors = [None] * nr_nodes
    for i in range(nr_nodes):
        # Inițializează "culorile" cu care vom colora
        colors[i] = i

    # Atribuie culorile
    # Parcurge nodurile în ordinea descrescătoare a gradelor pana cand vectorul e gol
    while node_degrees:
        u, _ = node_degrees.pop(0)

        # Daca nodul a fost deja colorat, trecem la următorul
        if node_color[u] != -1:
            continue

        color = colors.pop(0)
        node_color[u] = color

        for v, _ in node_degrees:
            # Dacă nodul nu are culoare și nu este vecin cu nodul curent și nici cu alte noduri colorate cu aceeași culoare
            # atunci îi atribuim culoarea curenta
            if not has_edge(graph, u, v) and node_color[v] == -1 and not neighbors_same_color(graph, node_color, v, color):
                node_color[v] = color
    return True