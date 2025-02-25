import random

def jogar_jogo_do_milhao():
    # banco de perguntas
    perguntas = [
        {
            "pergunta": "Qual é a cor primária que, quando combinada com azul, resulta em verde?",
            "opcoes": ["A) vermelho", "B) amarelo", "C) laranja", "D) roxo"],
            "resposta": "B",
        },
        {
            "pergunta": "Qual dessas opções não é um exemplo de dispositivo de entrada de dados em um computador?",
            "opcoes": ["A) teclado", "B) mouse", "C) monitor", "D) scanner"],
            "resposta": "C",
        },
        {
            "pergunta": "Qual dessas opções não é um exemplo de sistema operacional?",
            "opcoes": ["A) Windows", "B) Linux", "C) macOS", "D) Microsoft Word"],
            "resposta": "D",
        },
        {
            "pergunta": "Qual é o maior continente do planeta em extensão territorial?",
            "opcoes": ["A) Ásia", "B) África", "C) América do Norte", "D) Antártica"],
            "resposta": "A",
        },
        {
            "pergunta": "Qual é o maior oceano do planeta em extensão territorial?",
            "opcoes": ["A) Oceano Pacífico", "B) Oceano Atlântico", "C) Oceano Índico", "D) Oceano Ártico"],
            "resposta": "A",
        },
    ]

    # Lista de prêmios
    premios = [1000, 5000, 10000, 50000, 100000, 1000000]
    ajuda_disponivel = {"50:50": True, "plateia": True, "amigo": True}

    premio_atual = 0

    print("Bem-vindo ao Jogo do Milhão!\n")
    print("Responda corretamente às perguntas para ganhar até R$1.000.000!")
    print("Você pode sair do jogo a qualquer momento e levar o prêmio acumulado.")
    print("Se errar uma resposta, você perde tudo!\n")
    
    for nivel, pergunta in enumerate(perguntas):
        print(f"Pergunta {nivel + 1}: Valendo R${premios[nivel]}!\n")
        print(pergunta["pergunta"])
        for opcao in pergunta["opcoes"]:
            print(opcao)

        # Gerenciar ajudas
        if any(ajuda_disponivel.values()):
            print("\nAjudas disponíveis:")
            for ajuda, disponivel in ajuda_disponivel.items():
                if disponivel:
                    print(f"- {ajuda}")

        resposta = input("\nEscolha uma opção (A, B, C, D) ou digite 'sair' para encerrar: ").strip().upper()

        if resposta == "SAIR":
            print(f"Você decidiu sair do jogo. Parabéns, você ganhou R${premio_atual}!")
            break

        if resposta == "50:50" and ajuda_disponivel["50:50"]:
            ajuda_disponivel["50:50"] = False
            corretas_erradas = [
                pergunta["resposta"],
                random.choice([op for op in ["A", "B", "C", "D"] if op != pergunta["resposta"]])
            ]
            random.shuffle(corretas_erradas)
            print("Ajudas 50:50 - Alternativas restantes:")
            for op in corretas_erradas:
                print(f"- {op}) {pergunta['opcoes'][ord(op) - 65]}")
            resposta = input("\nEscolha uma opção (A, B, C, D): ").strip().upper()

        if resposta == "PLATEIA" and ajuda_disponivel["plateia"]:
            ajuda_disponivel["plateia"] = False
            print("A plateia acha que a resposta correta é:", pergunta["resposta"])
            resposta = input("\nEscolha uma opção (A, B, C, D): ").strip().upper()

        if resposta == "AMIGO" and ajuda_disponivel["amigo"]:
            ajuda_disponivel["amigo"] = False
            print("Seu amigo acha que a resposta correta é:", pergunta["resposta"])
            resposta = input("\nEscolha uma opção (A, B, C, D): ").strip().upper()

        if resposta == pergunta["resposta"]:
            premio_atual = premios[nivel]
            print(f"\nParabéns! Você acertou e ganhou R${premio_atual}!\n")
            if premio_atual == premios[-1]:
                print("Você venceu o Jogo do Milhão! Parabéns!")
                break
        else:
            print(f"\nVocê errou! A resposta correta era {pergunta['resposta']}.\n")
            print("Infelizmente, você perdeu tudo. Até a próxima!")
            break

# Chamando o jogo
# jogar_jogo_do_milhao()
