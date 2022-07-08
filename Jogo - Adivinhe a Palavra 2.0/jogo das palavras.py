import funcoes

f = funcoes
tentativas = 0

menu = f.topo()
word = f.sorteioPalavra(menu)
tamPalavra = len(word)
contLetras = ''

print(f'\nA palavra sorteada contém \n{tamPalavra} letras')

for pos in word:
    print('_', end=' ')

while True:
    palavra = f.verificarWord(tamPalavra)
    tentativas += 1
    if palavra == word:
        print(f'PARABÉNS ! Você acertou a palavra {word.upper()} em {tentativas} tentativas')
        break
    for p, letra in enumerate(palavra):
        if letra == word[p]:
            f.newPrint(letra, 'green', pular = False)
            contLetras += letra.upper()
        else:
            if word.count(letra) > 0:
                f.newPrint(letra, 'cyan', pular = False)
            else:
                f.newPrint(letra, 'red', pular = False)

