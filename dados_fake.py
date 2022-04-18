from faker import Faker

# inicializa a lib

fake = Faker()

# cria variáveis com dados fakes
def ger_dados_fake():
    
    nome = fake.name()
    prim_nome_feminino = fake.first_name_female()
    usuario = fake.user_name()
    senha = fake.password()
    mes = fake.month()

    print('=='*25)
    print(f'\033[34mNome:\033[m {nome}')
    print(f'\033[34mNome feminino:\033[m {prim_nome_feminino}')
    print(f'\033[34mUsuário:\033[m {usuario}')
    print(f'\033[34mSenha:\033[m {senha}')
    print(f'\033[34mMês:\033[m {mes}')


perg =  ' '

while True:
    perg = input("Deseja gerar mais dados? [S]/[N]: ").strip().upper()[0]

    if perg == 'S':
        ger_dados_fake()
    else:
        print("Obrigado por usar nosso gerador de dados.")
        break
            


