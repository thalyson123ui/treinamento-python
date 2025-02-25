
# Lista fictícia de notebooks com suas especificações
notebooks = [
    {"marca": "Dell", "modelo": "XPS 15", "preco": 2000, "desempenho": 9.5, "bateria": 8, "popularidade": 9.0},
    {"marca": "Apple", "modelo": "MacBook Pro 16", "preco": 2500, "desempenho": 9.8, "bateria": 10, "popularidade": 9.8},
    {"marca": "Asus", "modelo": "ROG Zephyrus G14", "preco": 1800, "desempenho": 9.2, "bateria": 7.5, "popularidade": 8.5},
    {"marca": "Lenovo", "modelo": "ThinkPad X1 Carbon", "preco": 1700, "desempenho": 8.8, "bateria": 9, "popularidade": 8.7},
    {"marca": "HP", "modelo": "Spectre x360", "preco": 1600, "desempenho": 8.5, "bateria": 8.5, "popularidade": 8.4},
]

# Função para classificar os notebooks com base em um critério
def classificar_notebooks(notebooks, criterio="desempenho"):
    """
    Classifica os notebooks com base em um critério especificado.

    :param notebooks: Lista de dicionários representando os notebooks.
    :param criterio: Critério de classificação (default: desempenho).
    :return: Lista de notebooks classificados.
    """
    return sorted(notebooks, key=lambda x: x[criterio], reverse=True)

# Exibir os notebooks classificados
print("Bem-vindo ao programa dos melhores notebooks de 2024!\n")
print("Critérios disponíveis: desempenho, preco, bateria, popularidade\n")

criterio = input("Escolha o critério para classificar os notebooks: ").strip().lower()

# Verifica se o critério é válido
if criterio not in notebooks[0]:
    print("Critério inválido! Usando desempenho como padrão.")
    criterio = "desempenho"

notebooks_classificados = classificar_notebooks(notebooks, criterio)

print(f"\nMelhores notebooks de 2024 classificados por {criterio}:\n")
for i, notebook in enumerate(notebooks_classificados, start=1):
    print(f"{i}. {notebook['marca']} {notebook['modelo']} - {criterio.capitalize()}: {notebook[criterio]} - Preço: ${notebook['preco']}")
