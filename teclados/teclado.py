# teclados_mais_vendidos.py

def teclados_mais_vendidos():
    """
    Exibe os teclados mais vendidos de 2024.
    Os dados são fictícios neste exemplo.
    """
    # Dados fictícios: teclado e quantidade de vendas
    teclados = [
        {"nome": "Teclado Mecânico HyperX Alloy", "vendas": 35000},
        {"nome": "Logitech MX Keys", "vendas": 50000},
        {"nome": "Razer Huntsman Mini", "vendas": 45000},
        {"nome": "Corsair K95 RGB Platinum", "vendas": 30000},
        {"nome": "Keychron K2", "vendas": 40000}
    ]
    
    # Ordenar os teclados por vendas em ordem decrescente
    teclados_ordenados = sorted(teclados, key=lambda x: x["vendas"], reverse=True)
    
    print("Os teclados mais vendidos de 2024 são:\n")
    for i, teclado in enumerate(teclados_ordenados, start=1):
        print(f"{i}. {teclado['nome']} - {teclado['vendas']} unidades vendidas")


if __name__ == "__main__":
    teclados_mais_vendidos()
