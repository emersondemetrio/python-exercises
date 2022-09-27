from pylab import *
import matplotlib.pyplot as plt

# Mesmo que ex. 01
RU = "3710807".replace("0", "1")

a = int(RU[-(len(RU) - 1)])  # 8
b = int(RU[-(len(RU) - 2)])  # 1
c = int(RU[-(len(RU) - 3)])  # 7


def resolver_equacao(a, b, c, x):
    return (a * x) + (b * x) - c


x1 = 5
x2 = 7
x3 = 9

# cria todos os pontos (fixados) de x
eixo_x = [
    None,
    x1,
    x2,
    x3
]

# Cria todos os pontos de x resolvendo as equações
eixo_y = [
    None,
    resolver_equacao(a, b, c, x1),
    resolver_equacao(a, b, c, x2),
    resolver_equacao(a, b, c, x3)
]


# Transfora o titulo em 'Exercicio 02'
result_figure = plt.figure('Exercicio 02')

# Cria todos os subplots do gráfico
ax = result_figure.add_subplot(111)

# Cria o label 'X'
ax.set_xlabel('X', size=14, labelpad=-24, x=1.03)

# Cria o label 'X'
ax.set_ylabel('Y', size=14, labelpad=5, rotation=0)


# Desenha todas as coordenadas de 'x'
for ponto_x, ponto_y in zip(eixo_x, eixo_y):
    plot(
        [ponto_x, ponto_x],
        [0, ponto_y],
        '-',
        linewidth=3
    )

# Desenha todas as coordenadas de 'y'
for ponto_x, ponto_y in zip(eixo_x, eixo_y):
    plot(
        [0, ponto_x],
        [ponto_y, ponto_y],
        '-',
        linewidth=3
    )

# Desenha os pontos onde as coordenadas se encontram (x, y)
scatter(
    eixo_x,
    eixo_y,
    s=100,
    marker='o',
)

# Imprime uma grade
grid()

# Mostra a figura resultante
show()
