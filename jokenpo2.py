jogadas = ['pedra', 'papel','tesoura']

jogador = input('Faça a sua jogada: ').lower()

import random

posicao= random.randint(0,2)

pc = jogadas [posicao]

if jogador not in jogadas: 
    print ('jogada inválida')

elif jogador == pc:
    print ('empate')
elif (pc == 'pedra' and jogador == 'tesoura') or pc == 'tesoura' and jogador == 'papel' or pc == 'papel' and jogador == 'pedra':
    print ('pc ganhou')
else:
    print('jogador ganhou')