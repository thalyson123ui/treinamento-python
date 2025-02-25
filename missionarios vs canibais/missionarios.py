from collections import deque

def is_valid(state):
    """"verifica se o estado é válido"""
    m1, c1, _ = state
    m2, c2 = 3 - m1, 3 - c1 # lado oposto
    if (m1 < c1 and m1 > 0) or (m2 < c2 and m2 > 0):
        return False # missionarios numca podem ser menos que canibais
    return 0 <= m1 <= 3 and 0 <= c1 <= 3

def get_sucessors(state):
    """gera todos os estados possiveis a partir de um estado valido"""
    m, c, b = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)] # possiveis movimentos
    sucessors = []

    for dm, dc in moves:
        if b == 1: # indo para o outro lado
            new_state = (m - dm, c - dc, 0)
        else: # voltando
            new_state = (m + dm, c + dc, 1)

        if is_valid(new_state):
            sucessors.append(new_state)

    return sucessors

def bfs():
    """busca em largura para encontrar a solução"""
    initial_state = (3, 3, 1) # todos na margem inicial
    goal_state = (0, 0, 0) # todos na margem final
    queue = deque([initial_state])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        if state == goal_state:
            return path + [state] # caminho encontrado
        
        for sucessor in get_sucessors(state):
            queue.append((sucessor, path + [state]))

    return None # não encontrou solução

if __name__ == "__main__":
    solution = bfs()
    if solution:
        for state in solution:
            print(state)
    else:
        print("Não encontrou solução")