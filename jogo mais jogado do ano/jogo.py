from operator import itemgetter

def get_most_played_games(games_data, top_n=5):
    """
    Ordena os jogos por quantidade de jogadores ou tempo jogado e retorna os mais populares.

    :param games_data: Lista de tuplas (nome_do_jogo, jogadores).
    :param top_n: Número de jogos mais populares a retornar.
    :return: Lista dos jogos mais populares.
    """
    # Ordena os jogos pela quantidade de jogadores (descendente)
    sorted_games = sorted(games_data, key=itemgetter(1), reverse=True)
    return sorted_games[:top_n]

# Dados simulados (jogo, jogadores em milhões)
games_2024_data = [
    ("Game A", 15),
    ("Game B", 30),
    ("Game C", 25),
    ("Game D", 40),
    ("Game E", 20),
    ("Game F", 35),
    ("Game G", 10)
]

# Número de jogos mais jogados a exibir
top_n = 5

# Chama a função para obter os jogos mais jogados
most_played_games = get_most_played_games(games_2024_data, top_n)

# Exibe os resultados
print(f"Os {top_n} jogos mais jogados de 2024 foram:")
for rank, (game, players) in enumerate(most_played_games, start=1):
    print(f"{rank}. {game} com {players} milhões de jogadores.")
