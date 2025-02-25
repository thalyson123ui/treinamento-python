import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  # (x, y)
        self.parent = parent  # Nó pai
        self.g = g  # Custo do caminho do início até este nó
        self.h = h  # Heurística (estimativa do custo até o objetivo)
        self.f = g + h  # Custo total estimado
    
    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    """Calcula a distância Manhattan entre dois pontos."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, end):
    """Executa a busca A* para encontrar o caminho mais curto em uma grade."""
    open_list = []  # Fila de prioridade
    closed_set = set()  # Conjunto de nós já visitados
    
    start_node = Node(start, None, 0, heuristic(start, end))
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)  # Pega o nó com menor custo f
        
        if current_node.position == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Retorna o caminho do início ao fim
        
        closed_set.add(current_node.position)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Movimentos válidos (cima, baixo, esquerda, direita)
            neighbor_pos = (current_node.position[0] + dx, current_node.position[1] + dy)
            
            if (neighbor_pos[0] < 0 or neighbor_pos[0] >= len(grid) or
                neighbor_pos[1] < 0 or neighbor_pos[1] >= len(grid[0]) or
                grid[neighbor_pos[0]][neighbor_pos[1]] == 1 or  # 1 representa obstáculo
                neighbor_pos in closed_set):
                continue
            
            g_cost = current_node.g + 1
            h_cost = heuristic(neighbor_pos, end)
            neighbor_node = Node(neighbor_pos, current_node, g_cost, h_cost)
            
            heapq.heappush(open_list, neighbor_node)
    
    return None  # Caminho não encontrado

# Exemplo de uso:
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = a_star_search(grid, start, end)
print("Caminho encontrado:", path)
