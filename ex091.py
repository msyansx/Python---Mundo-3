from operator import itemgetter
from time import sleep
from random import randint

jogadores = {'Jogador 1:': randint(1, 6),
'Jogador 2:': randint(1, 6),
'Jogador 3:': randint(1, 6),
'Jogador 4:': randint(1, 6)}

print( '=' * 10, 'VALORES SORTEADOS', '=' * 10)

# Organizando o placar
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print( '=' * 10, 'RANK DOS JOGADORES',  '=' * 10)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for ind, vlr in enumerate(rank):
    print(f'{ind+1}º lugar: {vlr[0]} com {vlr[1]} pontos.')
    sleep(1)