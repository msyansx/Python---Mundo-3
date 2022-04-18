import matplotlib.pyplot as plt
import numpy as np

# valores do gráfico

y = np.array([35, 25, 25, 15])

# itens do gráfico

etiquetas = ['Notebook', 'All in One', 'Desktop', 'iPad']

# espaçamento entre os dados

espac_graf = [0.05, 0.05, 0.05, 0.05]

# monta o gráfico e depois mostra na tela

plt.pie (y, labels = etiquetas, explode = espac_graf, shadow = False)
plt.show()