import numpy as np
import matplotlib.pyplot as plt

# quantidade de vendas para o produto A 

vlr_A = [6, 7, 8, 4, 4]

# quantidade de vendas para o produto B 

vlr_B = [3, 12, 3, 4.1, 6]

# cria eixo x para produto A e produto B com uma separação de 0.25 entre as barras

x1 = np.arange(len(vlr_A))
x2 = [x + 0.25 for x in x1]

# plota as barras 

plt.bar(x1, vlr_A, width = 0.25, label = 'Produto A', color = 'deepskyblue')
plt.bar(x2, vlr_B, width = 0.25, label = 'Produto B', color = 'mediumseagreen')

# coloca o nome dos meses como label do eixo X

meses = ['Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
plt.xticks([x + 0.25 for x in range(len(vlr_A))], meses)

# insere uma legenda no gráfico

plt.legend()

plt.title('Quantidade de Vendas')
plt.show()