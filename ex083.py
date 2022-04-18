#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
#fechados na ordem correta.

exp = input('Digite a expressão: ')
verif = list()

for simbolo in exp:
    if simbolo == '(':
        verif.append('(')
    elif simbolo == ')':
        if len(verif) > 0:
            verif.pop()
        else: 
            verif.append(')')
            break

if len(verif) == 0:
    print("Sua expressão é válida")
else:
    print('Sua expressão está errada')