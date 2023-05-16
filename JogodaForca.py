import random
from os import system, name


def limpa_tela():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")


def display_hangman(chances):
    stages = [  # estágio 6 (final)
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # estágio 5
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # estágio 4
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # estágio 3
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # estágio 2
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # estágio 1
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # estágio 0
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[chances]


def game():
    limpa_tela()
    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    palavra = random.choice(palavras)

    lista_letras_palavras = [letra for letra in palavra]

    tabuleiro = ["_"] * len(palavra)

    chances = 6

    letras_tentativas = []

    while chances > 0:
        print(display_hangman(chances))
        print("Palavra: ", tabuleiro)
        print("\n")

        tentativa = input("\nDigite uma letra: ")

        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue

        letras_tentativas.append(tentativa)

        if tentativa in lista_letras_palavras:
            print("Você acertou a letra!")

            for indice in range(len(lista_letras_palavras)):
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa

            if "_" not in tabuleiro:
                print(f"\nVocê venceu, a palavra era: {palavra}")
                break
        else:
            print("Ops. Essa letra não está na palavra ")
            chances -= 1

    if "_" in tabuleiro:
        print(f"\nVocê perdeu! A palavra era: {palavra}.")


if __name__ == "__main__":
    game()
    print("\nObirgado por jogar!\n")
