# Implementarea algoritmului Greedy pentru colorarea unui graf 

# Adauga o muchie intre nodurile u si v
def addEdge(neighbours, u, v):
    neighbours[u].append(v)
    neighbours[v].append(u)
    return neighbours
 

def greedyColoring(neighbours, nr_nodes):
    # Initializam un vector ce retine culoarea finala 
    # a fiecarui nod
    colored_graph = [-1] * nr_nodes

    # Initializam un vector de culori ce retine toate culorile disponibile
    # culorile reprezinta numerele de la 0 la V-1
    colors = [None] * nr_nodes
    for i in range(nr_nodes):
        colors[i] = i
    
    # Initializam primul nod cu culoarea 0
    colored_graph[0] = colors[0]
 
    # Initializam un vector care retine daca o culoare
    # este disponibila sau nu pentru un anumit nod
    available_colors = [True] * nr_nodes
 
    # Procesam toate nodurile
    for u in range(1, nr_nodes):
        for i in neighbours[u]:
            if (colored_graph[i] != -1):
                available_colors[colored_graph[i]] = False
 
        # Gasim prima culoare disponibila
        color_index = 0
        while color_index < nr_nodes:
            if (available_colors[color_index] == True):
                break
            color_index += 1
             
        # Coloram nodul u cu culoarea gasita
        colored_graph[u] = colors[color_index] 
 
        # Resetam vectorul de culori disponibile pentru urmatoarea iteratie
        for i in neighbours[u]:
            available_colors[colored_graph[i]] = True

    return True
 