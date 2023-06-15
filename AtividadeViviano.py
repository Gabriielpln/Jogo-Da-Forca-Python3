import os


# 1. Princípio Soma
def regra_soma():
    banco = ['SQL', 'NoSQL', 'GIS']
    prog = ['Python', 'Java', 'C', 'PHP']
    eng = ['Métodos Ágeis', 'Processos de Software']

    cont = 0

    print(''' Temos essas disciplinas: 
    
    Banco de Dados = SQL, NoSQL, GIS,
    Programação = Python, Java, C, PHP,
    Engenharia de Sogtware = Métodos Ágeis, Processos de Software
    ''')

    for bc in banco:
        print(bc)
        cont += 1

    for pg in prog:
        print(pg)
        cont += 1

    for eg in eng:
        print(eg)
        cont += 1
    print(f'\nVocê optou por regra da soma e as possibilidades são {cont}\n\n')
    os.system('pause')
    os.system('cls')


# 2. Princípio Produto
def regra_produto():
    banco = ['SQL', 'NoSQL', 'GIS']
    prog = ['Python', 'Java', 'C', 'PHP']
    eng = ['Métodos Ágeis', 'Processos de Software']

    cont = 0
    print(''' Temos essas disciplinas: 

    Banco de Dados = SQL, NoSQL, GIS,
    Programação = Python, Java, C, PHP,
    Engenharia de Sogtware = Métodos Ágeis, Processos de Software
    ''')

    for bc in banco:
        for pg in prog:
            for eg in eng:
                print(bc, pg, "e", eg)
                cont += 1
    print(f'\nVocê optou por regra do produto e as possibilidades são {cont}\n\n')
    os.system('pause')
    os.system('cls')


# 5. Amostragem com Reposição
def reposicao():

    import random

    quantidade_populacao = int(input("Digite a quantidade de elementos: "))
    quantidade_amostra = int(input("Digite o tamanho da amostra desejada: "))

    populacao = []

    for i in range(quantidade_populacao):
        elemento = input(f"Agora, Digite o elemento, serão {quantidade_populacao} elementos: ")
        populacao.append(elemento)

    amostra = random.choices(populacao, k=quantidade_amostra)

    print(f'Amostra selecionada: {amostra}\n\n')
    os.system('pause')
    os.system('cls')


# 6. Amostragem Sem Reposição
def s_reposicao():
    import random

    quantidade_populacao = int(input("Digite a quantidade de elementos: "))
    quantidade_amostra = int(input("Digite o tamanho da amostra: "))

    populacao = []

    for i in range(quantidade_populacao):
        elemento = input(f"Agora, digite o elemento, serão {quantidade_populacao} elementos: ")
        populacao.append(elemento)

    amostra = random.sample(populacao, quantidade_amostra)

    print(f"Amostra selecionada: {amostra}\n\n")
    os.system('pause')
    os.system('cls')


# 7. Combinação
def combinacao():
    from itertools import combinations

    dados = input("\n\nDigite os dados separados por espaço: ").split()
    tamanho_combinacao = int(input("\nDigite o tamanho da combinação desejada: "))
    resultado = list(combinations(dados, tamanho_combinacao))

    print("Combinações:")
    for combinacao in resultado:
        print(combinacao)

    print('\n\n')
    os.system('pause')
    os.system('cls')


option = input('\n\n\t\tBem vindo, deseja navegar? S para sim ou N para sair: ').upper()

while option == 'S':
    op = int(input('''\n
    1. PRINCÍPIO DA REGRA DA SOMA
    2. PRINCÍPIO DA REGRA DO PRODUTO
    3. PERMUTAÇÃO
    4. PERMUTAÇÃO UTILIZANDO AS LETRAS DE UMA PALAVRA
    5. AMOSTRAGEM COM REPOSIÇÃO
    6. AMOSTRAGEM SEM REPOSIÇÃO
    7. COMBINAÇÕES
    Escolha uma operação:'''))
    os.system('cls')

    if op == 1:
        regra_soma()

    if op == 2:
        regra_produto()

    if op == 3:
        def permut(numero):

            import itertools

            digitos = list(str(numero))
            permutacoes = list(itertools.permutations(digitos))

            permutacoes_numeros = []
            for permutacao in permutacoes:
                permutacao_numero = int(''.join(permutacao))
                permutacoes_numeros.append(permutacao_numero)

            return permutacoes_numeros


        numero = input("Digite um número para fazer permutação: ")
        print(permut(numero))

        os.system('pause')
        os.system('cls')

    if op == 4:
        def permutacao_p(palavra):
            if len(palavra) == 0:
                return []

            if len(palavra) == 1:
                return [palavra]

            permutacoes = []

            for i in range(len(palavra)):
                letra_atual = palavra[i]
                letras_restantes = palavra[:i] + palavra[i + 1:]

                for permutacao_restante in permutacao_p(letras_restantes):
                    nova_permutacao = letra_atual + permutacao_restante
                    permutacoes.append(nova_permutacao)

            return permutacoes


        palavra = input('Digite uma palavra: ')
        print(permutacao_p(palavra))

        os.system('pause')
        os.system('cls')

    if op == 5:
        reposicao()

    if op == 6:
        s_reposicao()

    if op == 7:
        combinacao()

if option == 'n':
    print('Obrigado por utilizar!')
