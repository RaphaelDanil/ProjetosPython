import random
import fgame

while True:
    words = fgame.sorteioPalavra()
    fgame.topo('Jogo da Adivinhação')
    palavra = ''
    tentativas = acerto = 0
    while True:
        acerto = 0
        for pos in words:
            if pos in palavra:
                print(pos, end=' ')
            else:
                print('_', end=" ")
                acerto += 1

        if acerto == 0:
            print(f'\nParabéns você venceu, a palavra é {words}')
            print(f'Tentativas: {tentativas}')
            print('-=' * 30)
            break
        else:
            letra = fgame.checkLetra()
            tentativas += 1
            palavra += letra

    if acerto == 0:
        break