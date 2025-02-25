import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_especiais=True):
    """
    Gera uma senha aleatória com base nas opções fornecidas.
    
    :param tamanho: Comprimento da senha (padrão é 12).
    :param usar_maiusculas: Se True, inclui letras maiúsculas.
    :param usar_minusculas: Se True, inclui letras minúsculas.
    :param usar_numeros: Se True, inclui números.
    :param usar_especiais: Se True, inclui caracteres especiais.
    :return: Uma string com a senha gerada.
    """
    if tamanho < 1:
        raise ValueError("O tamanho da senha deve ser pelo menos 1.")
    
    # Conjuntos de caracteres possíveis
    caracteres = ""
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += string.punctuation
    
    if not caracteres:
        raise ValueError("Pelo menos uma opção de caracteres deve ser selecionada.")

    # Garante que a senha tenha pelo menos um caractere de cada tipo selecionado
    senha = []
    if usar_maiusculas:
        senha.append(random.choice(string.ascii_uppercase))
    if usar_minusculas:
        senha.append(random.choice(string.ascii_lowercase))
    if usar_numeros:
        senha.append(random.choice(string.digits))
    if usar_especiais:
        senha.append(random.choice(string.punctuation))
    
    # Completa o restante da senha de forma aleatória
    senha += random.choices(caracteres, k=tamanho - len(senha))
    random.shuffle(senha)  # Embaralha a senha para aumentar a aleatoriedade
    
    return ''.join(senha)

# Exemplo de uso:
senha = gerar_senha(tamanho=16, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_especiais=True)
print(f"Senha gerada: {senha}")