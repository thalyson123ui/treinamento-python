import heapq

def dijkstra(graph, start, targets):
    # Inicialização
    queue = []
    heapq.heappush(queue, (0, start, [])) # (custo acumulado, nó atual, caminho percorrido)
    visited = set()
    shortest_path = None
    shortest_distance = float('inf')

    while queue:
        cost, current, path = heapq.heappop(queue)

        if current in visited:
            continue
        visited.add(current)

        # Atualizar caminho
        path = path + [current]

        # Verificar se chegou a uma farmácia
        if current in targets:
            if cost < shortest_distance:
                shortest_path = path
                shortest_distance = cost
                # Como queremos o mais próximo, podemos parar aqui
                break

        # Adicionar vizinhos na fila de prioridade
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return shortest_path, shortest_distance

# Exemplo de grafo
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('E', 3)],
    'D': [('B', 7), ('E', 2), ('F', 5)],
    'E': [('C', 3), ('D', 2), ('F', 1)],
    'F': [('D', 5), ('E', 1)]
}

# Entrada do usuário
start = 'A'
pharmacies = ['D', 'F']

# Encontrar o caminho mais curto
path, distance = dijkstra(graph, start, pharmacies)

# Exibir resultados
print(f"O caminho mais rápido para a farmácia é: {' -> '.join(path)} com distância total de {distance}.")
