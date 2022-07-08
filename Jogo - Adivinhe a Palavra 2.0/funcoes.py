import random

def sorteioPalavra(menu):
    listaPalavras = list()

    if menu == 1:
        arquivo = open('objetos.txt', 'r')
        for l in arquivo:
            listaPalavras.append(l)
    elif menu == 2:
        arquivo = open('animais.txt', 'r')
        for l in arquivo:
            listaPalavras.append(l)
    elif menu == 3:
        arquivo = open('nomes.txt', 'r')
        for l in arquivo:
            listaPalavras.append(l)
    elif menu == 4:
        arquivo = open('paises.txt', 'r')
        for l in arquivo:
            listaPalavras.append(l)

    pos = random.randint(1, len(listaPalavras))
    palavra = str(listaPalavras[pos]).strip().upper()

    return palavra


def newPrint(txt, color, pular = True):
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"

    if color == 'red':
        cor = "\033[1;31m"
    elif color == 'blue':
        cor = "\033[1;34m"
    elif color == 'cyan':
        cor = "\033[1;36m"
    elif color == 'green':
        cor = "\033[0;32m"


    if pular:
        print(cor + f'{txt}' + RESET)
    else:
        print(cor + f'{txt}' + RESET, end=' ')



def verificarWord(t):
    valido = False
    while True:
        print()
        words = str(input(f'Sugestão: ')).strip().upper()
        if words.isalpha():
            if len(words) < t or len(words) > t:
                newPrint('ERRO, quantidade de letras inválidas', 'red', pular = False)
                words = ''
            elif len(words) == t:
                valido = True
        else:
            newPrint('Digite uma palavra correta', 'red', pular = False)
        if valido:
            break

    return words


def topo():
    Op = True
    msg = '~~ Jogo da Adivinhação 2.0 ~~ '
    tamMsg = len(msg) + 2
    print('~' * tamMsg)
    print(f' {msg}')
    print('~' * tamMsg)
    print('Digite uma palavra com a quantidade de \nletras correspondente a palavra secreta\n')
    newPrint('Letra em Verde:', 'green', pular = True)
    print('   A letra está na posição correta')
    newPrint('Letra em Ciano: ', 'cyan', pular = True)
    print('   A letra contém na palavra')
    newPrint('Letra em Vermelho: ', 'red', pular = True)
    print('   A letra não contém na palavra')
    print('~' * tamMsg)
    print(' ... ! MENU ! ... ')
    print('[ 1 ] - Objetos')
    print('[ 2 ] - Animais')
    print('[ 3 ] - Nomes')
    print('[ 4 ] - Paises')
    opcao = int(input('Opção: '))

    return opcao