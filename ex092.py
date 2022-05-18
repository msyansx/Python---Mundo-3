from datetime import datetime

funcionario = dict()
funcionario['Nome'] = str(input("Nome do funcionário: "))

nasc = int(input("Ano de nascimento: "))
funcionario['Idade'] = datetime.now().year - nasc
funcionario['Ctps'] = int(input("Número da carteira de trabalho (0 não possui): "))

if funcionario['Ctps'] != 0:
    funcionario['Contratação'] = int(input("Ano de contratação: "))
    funcionario['Salario'] = float(input("Digite o salário: R$ "))
    funcionario['Idade que vai se aposentar'] = funcionario['Idade'] + ((funcionario['Contratação'] + 35) - datetime.now().year)

print('==' * 30)

for ind, val in funcionario.items():
    print(f' - {ind}: {val}')