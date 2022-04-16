pais = [str(input("Digite o nome da sua mãe: ")), str(input("Digite o nome do seu pai: ")) ]

amt = [str(input("Deseja adicionar uma terceira pessoa? ")).strip().upper()[0]]

if amt in 'Ss':
    pais = [str(input("Digite o nome dessa terceira pessoa: "))]
    for filho in range(0, len(pais) + len(amt)):
        if filho % 2 == 1:
            print("Então cara..... Você é corno. ")
else:      
    print("Parabéns, você não é corno!")