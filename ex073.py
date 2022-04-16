times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 
'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 
'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 
'Ponte Preta', 'Atlético-GO')

from time import sleep

while True:
    print("=="*35)

    # ------------------------ PARTE A DO EXERCICIO
    print(f"\033[32mOs primeiros 5 times são: \033[m", end='')

    for prim in range(0, len(times[:5])):
        print(f"{times[prim]}", end=' | ')

    print('\n')
    print("=="*35)

    # ------------------------ PARTE B DO EXERCICIO
    print(f"\033[33mOs últimos 4 colocados são: \033[m", end='')

    for ult in range(16, len(times[:20])):
        print(f"{times[ult]}", end=' | ')
    
    print('\n')
    print("=="*35)

    # ------------------------ PARTE C DO EXERCICIO
    print("\033[34mTimes em ordem alfabética: \033[m", sorted(times))

    print("=="*35)

    # ------------------------ PARTE D DO EXERCICIO
    print(f"\033[31mChapecoense está na posição: \033[m{times.index('Chapecoense')+1}")

    sleep(2)

    break
print('\n')
print("\033[32mCódigo finalizado\033[m")