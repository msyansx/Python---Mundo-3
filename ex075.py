#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
#
#A) Quantas vezes apareceu o valor 9.
#
#B) Em que posição foi digitado o primeiro valor 3.
#
#C) Quais foram os números pares.

tupla = ((int(input("Digite o primeiro valor: "))), (int(input("Digite o segundo valor: "))), 
(int(input("Digite o terceiro valor: "))),
(int(input("Digite o quarto: "))), (int(input("Digite o quinto valor: "))))

print(f"Você digitou os valores: {tupla}", end=' ')

#PARTE A DO EXERCÍCIO

cont_9 = tupla.count(9)
print(f"\n\nO número 9 apareceu {cont_9} vezes.")

#PARTE B DO EXERCÍCIO   

if 3 in tupla:
    posicao = tupla.index(3)+1

    print(f"O número 3 foi digitado {posicao}ª posição.")
else: 
    print("O número 3 não apareceu nenhuma vez")

# PARTE C DO EXERCÍCIO

print("Os números pares foram: ", end=' ')

for par in tupla:
    if par % 2 == 0:
        print(par, end=' | ')

