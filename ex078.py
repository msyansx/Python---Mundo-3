#EX 78

valores = list()

for pos in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {pos+1}: ")))

print("=-"*30)

print(f'O maior valor digitado foi {max(valores)} e está nas posições: ', end=' ')

for ind, vlr in enumerate(valores):
    if vlr == max(valores):
        print(f'{ind}...', end=' ')

print(f'\nO menor valor digitado foi {min(valores)} e está nas posições: ', end=' ')

for x, y in enumerate(valores):
    if y == min(valores):
        print(f'{x}...', end=' ')