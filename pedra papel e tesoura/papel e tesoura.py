import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']

    print("bem vindo ao pedra,papel e tesoura")
    jogador = input("escolha pedra papel e tesoura").strip().lower()

    if jogador not in opcoes:
        print("escolha invalida! tente novamente.")
        return
    
    computador = random.choice(opcoes)
    print(f"o computador escolheu: {computador}")

    if jogador == computador:
        print("empate!")
    elif (jogador == 'pedra' and computador == 'tesoura') or \
        (jogador == 'papel' and computador == 'pedra') or \
        (jogador == 'tesoura' and computador == 'papel'):
        print("voce venceu")
    else:
        print("voce perdeu")

if __name__ == "__main__":
    jogar()