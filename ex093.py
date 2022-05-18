jogador = dict()
partidas = list()
jogador['Nome'] = str(input("Nome do jogador: "))
total = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))

for cont in range(0, total):
    partidas.append(int(input(f"  -- Quantos gols {jogador['Nome']} fez na {cont+1}ª partida: "))) 
    jogador['Gols'] = partidas[:]
    partidas.clear

jogador['Total'] = sum(partidas)

print('==' * 20)

print(f"O jogador {jogador['Nome']} jogou um total de {total} partidas")

for ind, val in jogador.items():
    print(f'    ==> {ind}: {val}')

print('==' * 20)

for i, v in enumerate(partidas):
    print(f'Na partida {i+1}, o jogador {jogador["Nome"]} fez um total de {v} gols.')

print('==' * 20)

print(f'Foi um total de {jogador["Total"]} gols.')
