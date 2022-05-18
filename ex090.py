dados = dict()

dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f"Média de {dados['nome']}: "))

if dados['media'] >= 7:
    print(f"Parabéns {dados['nome']}, você foi aprovado com a media {dados['media']}.")

elif dados['media'] > 4 and dados['media'] < 7:
    print(f"{dados['nome']}, você está de recuperação com a média {dados['media']}!")

else:
    print(f"Poxa {dados['nome']}, você foi reprovado com a média {dados['media']}.")
