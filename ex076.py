valores = list()

for pos in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

print(f'O maior valor digitado foi {max(valores)} e está na posição: {valores.index(max(valores))+1}')
print(f'O menor valor digitado foi {min(valores)} e está na posição: {valores.index(min(valores))+1}')