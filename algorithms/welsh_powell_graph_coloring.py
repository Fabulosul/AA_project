def add_edge(graph, u, v):
    '''Adaugă o muchie între nodurile "u" și "v"'''
    graph[u].append(v)
    graph[v].append(u)

def has_edge(graph, u, v):
    '''Verifică dacă există o muchie între nodurile "u" și "v"'''
    return v in graph[u]

def calculate_degrees(graph):
    '''Calculează gradul fiecărui nod'''
    return [(u, len(graph[u])) for u in range(len(graph))]

def get_uncolored_highest_degree(degree_list, node_color):
    '''Returnează nodul necolorat cu cel mai mare grad'''
    for u, degree in degree_list:
        if node_color[u] == -1:
            return u
    return None

def update_V_prime(graph, current_colored_node, node_color):
    '''Actualizează setul V' cu noduri necolorate care nu sunt vecine cu nodul curent colorat'''
    V_prime = []
    active_color = node_color[current_colored_node]
    for v in range(len(graph)):
        if (
            node_color[v] == -1 and  # Nod necolorat
            not has_edge(graph, current_colored_node, v) and  # Nu este adiacent nodului curent
            all(node_color[neighbor] != active_color for neighbor in graph[v])  # Niciun vecin nu are culoarea curentă
        ):
            V_prime.append(v)
    return V_prime

def graph_coloring_welsh_powell(graph):
    '''Colorează graful utilizând algoritmul Welsh-Powell'''
    nr_nodes = len(graph)
    node_color = [-1] * nr_nodes  # -1 indică noduri necolorate
    color_set = []  # Lista de culori utilizate

    # Step 1: Calculează gradele și sortează descrescător
    degrees = calculate_degrees(graph)
    degrees.sort(key=lambda x: x[1], reverse=True)

    # Step 4: Repetă până toate nodurile sunt colorate
    while any(color == -1 for color in node_color):
        # Selectează o nouă culoare din paleta de culori
        active_color = len(color_set)
        color_set.append(active_color)

        # Step 2: Găsește nodul necolorat cu grad maxim
        highest_degree_node = get_uncolored_highest_degree(degrees, node_color)

        # Step 3: Colorează nodul selectat și actualizează V'
        while highest_degree_node is not None:
            node_color[highest_degree_node] = active_color
            V_prime = update_V_prime(graph, highest_degree_node, node_color)

            # Selectează următorul nod necolorat din V' pentru aceeași culoare
            next_node = None
            max_degree = -1
            for v in V_prime:
                current_degree = len(graph[v])
                if current_degree > max_degree:
                    max_degree = current_degree
                    next_node = v

            highest_degree_node = next_node

    return len(color_set), node_color