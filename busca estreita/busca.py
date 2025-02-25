from collections import deque

def bfs(graph, start, goal):
    queue = deque([[start]])  # Fila contendo caminhos
    visited = set()
    
    while queue:
        path = queue.popleft()  # Remove o primeiro caminho da fila
        node = path[-1]  # Último nó do caminho
        
        if node in visited:
            continue
        
        visited.add(node)
        
        if node == goal:
            return path  # Retorna o caminho encontrado
        
        for neighbor in graph.get(node, []):
            new_path = list(path)  # Copia o caminho atual
            new_path.append(neighbor)  # Adiciona o vizinho ao caminho
            queue.append(new_path)  # Adiciona o novo caminho à fila
    
    return None  # Retorna None se não encontrar um caminho

# Exemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
goal = 'F'
caminho = bfs(graph, start, goal)
print("Caminho encontrado:", caminho)
