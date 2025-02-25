import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    """
    Implementa a busca gulosa pelo melhor primeiro caminho.
    
    :param graph: Dicionário representando o grafo {nó: [(vizinho, custo), ...]}
    :param start: Nó inicial
    :param goal: Nó objetivo
    :param heuristic: Dicionário com valores heurísticos estimados {nó: valor}
    :return: Caminho do nó inicial ao objetivo
    """
    priority_queue = []  # Fila de prioridade (menor heurística primeiro)
    heapq.heappush(priority_queue, (heuristic[start], start, [start]))
    visited = set()
    
    while priority_queue:
        _, current, path = heapq.heappop(priority_queue)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        if current == goal:
            return path  # Caminho encontrado
        
        for neighbor, _ in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))
    
    return None  # Caminho não encontrado

# Definição do Grafo
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 2)],
    'E': [('G', 3)],
    'F': [('G', 2)],
    'G': []
}

# Heurística estimada para cada nó até 'G'
heuristic = {
    'A': 7, 'B': 6, 'C': 4, 'D': 3, 'E': 2, 'F': 1, 'G': 0
}

# Execução do Algoritmo
target_path = greedy_best_first_search(graph, 'A', 'G', heuristic)
print("Caminho encontrado:", target_path)
