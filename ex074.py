#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

print("="*30)

print("Os valores sorteados foram: ")

aleat = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

for c in range (0, 5):
    print(aleat[c], end=' ')

print('\n')
print(f"Maior valor: {max(aleat)}")
print(f"Menor valor: {min(aleat)}")
    
    


