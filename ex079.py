#EX 79 
print("=="*25)
print(f"ADICIONANDO E ORDENANDO NUMEROS EM LISTA")
lista = list()

while True:

    adic = int(input("Digite um valor: "))

    if adic not in lista:
        lista.append(adic)
    else:
       print("Valor duplicado, não vou adicionar.")         

    perg = input("Deseja continuar? [S]/[N]: ").strip().upper()[0]

    if perg == 'N':
        break

print("=="*25)
print(f"Você digitou os valores: {lista}")

lista.sort()

print(f"E esses valores em ordem crescente ficam: {lista}")
print("=="*25)
print("Código finalizado")