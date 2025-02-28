import math

def calcular():
    print("Bem-vindo ao Bot Calculadora! Digite 'sair' para encerrar.")
    while True:
        try:
            expressao = input("Digite a operação matemática (ex: 2 + 2, sqrt(9), 3**2): ")
            if expressao.lower() == 'sair':
                print("Encerrando o bot... Até logo!")
                break
            
            resultado = eval(expressao, {"__builtins__": None}, {"sqrt": math.sqrt, "pow": pow})
            print(f"Resultado: {resultado}\n")
        
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.\n")
        except Exception as e:
            print(f"Erro: Entrada inválida ({e}).\n")

if __name__ == "__main__":
    calcular()
