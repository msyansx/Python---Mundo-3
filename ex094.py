people = dict()
everybody = list()
soma = media = 0

while True:
    people.clear()
    people['nome'] = str(input("Nome: "))
    while True:
        people['sexo'] = str(input("Sexo M/F: ")).upper()[0]
        if people['sexo'] in 'FM':
            break
        print("Digite um sexo entre [F] e [M]")

    people['idade'] = int(input("Idade: "))

    soma += people['idade']

    everybody.append(people.copy())

    while True: 
        perg = str(input("Deseja continuar? [S]/[N]: ")).upper()[0]
        if perg in 'SN':
            break
        print("Erro! Selecione uma opção entre [S] e [N]")

    if perg == 'N':
        break

print("==" * 20)
print(f'A) Total de pessoas cadastradas: {len(everybody)}.')

media = soma / len(everybody)

print(f'B) A média de idade é: {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')

for c in everybody:
    if c['sexo'] == 'F':
        print(f'{c["nome"]} ', end='')
print()
print('D) A lista das pessoas que estão acima da média: ')

for x in everybody:
    if x['idade'] >= media:
        print('   ', end='')
        for ind, vlr in x.items(): 
            print(f'{ind} = {vlr}; ', end='')
        print()

print('=== ENCERRADO ===')