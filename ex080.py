#EX 080

lista = list()

for pos in range(0, 5):
    num = int(input("Digite um valor: "))
    
    if pos == 0 or num > lista[-1]:
        lista.append(num)
        print("Valor adicionado ao final da lista")
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f"Valor adicionado na posição {posicao}")
                break
            posicao += 1


print(lista)