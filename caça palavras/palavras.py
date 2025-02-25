import random
import string

def criar_grade(tamanho):
    return [['' for _ in range(tamanho)] for _ in range(tamanho)]

def exibir_grade(grade):
    for linha in grade:
        print(' '.join(linha))

def pode_colocar_palavra(grade, palavra, linha, coluna, direção):
    tamanho = len(grade)
    dx, dy = direção

    for i in range(len(palavra)):
        x, y = linha + i * dx, coluna + i * dy
        if not (0 <= x < tamanho and 0 <= y  < tamanho) or (grade[x][y] != '' and grade[x][y] != palavra[i]):
            return False
    return True

def colocar_palavra(grade, palavra, linha, coluna, direção):
    dx, dy = direção
    for i in range(len(palavra)):
        grade[linha + i * dx][coluna + i * dy] = palavra[i]

def prencher_grade(grade, palavras):
    tamanho = len(grade)
    direções = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for palavra in palavras:
        colocada = False
        tentativas = 0
        while not colocada and tentativas < 100:
            linha = random.randint(0, tamanho - 1)
            coluna = random.randint(0, tamanho - 1)
            direção = random.choice(direções)
            if pode_colocar_palavra(grade, palavra, linha, coluna, direção):
                colocar_palavra(grade, palavra, linha, coluna, direção)
                colocada = True
            tentativas += 1

    for i in range(tamanho):
        for j in range(tamanho):
            if grade[i][j] == '':
                grade[i][j] = random.choice(string.ascii_uppercase)

if __name__ == '__main__':
    palavras = ['PYTHON', 'JAVA', 'RUBY', 'JAVASCRIPT', 'PHP']
    tamanho = 10
    grade = criar_grade(tamanho)
    prencher_grade(grade, palavras)
    exibir_grade(grade)

    grade = criar_grade(tamanho)
    prencher_grade(grade, palavras)
    exibir_grade(grade)