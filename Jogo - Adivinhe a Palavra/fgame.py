import random

def topo(msg):
    tam = len(msg) + 10
    print('~' * tam)
    print(f'     {msg}')
    print('~' * tam)
    print('- Tente adivinhar a palavra sorteada. Boa Sorte !')


def sorteioPalavra():
    with open("palavras.txt", "r") as file:
        data = file.read()
        words = data.split()

    pos_palavra = random.randint(0,len(words)-1)
    palavra = str(words[pos_palavra]).upper()
    return palavra

def checkLetra():
    while True:
        letra = input('\nDigite uma letra: ').upper().strip()[0]
        if letra.isalpha():
            break
        else:
            print('ERRO!')
    return str(letra)