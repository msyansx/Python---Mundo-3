teste = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n1 = None

while True:
    print("="*25)
    n1 = int(input("Digite um número entre 0 e 20: "))

    while n1 < 0 or n1 > 20:
        n1 = int(input("Digite um número dentro do intervalo: "))
    
    if n1 >= 0 and n1 < 21:
        print(f"Você digitou o número: {n1}, que escrito por extenso é: {teste[n1]}")

    perg = ' '
    
    while perg not in 'S' and perg not in 'N':
        perg = str(input("Deseja continuar? [S]/[N]: ")).strip().upper()

    if perg[:1] == 'N':
        break
    else:
        continue

print("\033[34mCódigo finalizado!\033[m")