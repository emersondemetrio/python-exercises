from pylab import *
import matplotlib.pyplot as plt

# Mesmo que ex. 01
RU = "3710807".replace("0", "1")

a = int(RU[-(len(RU) - 1)])  # 8
b = int(RU[-(len(RU) - 2)])  # 1
c = int(RU[-(len(RU) - 3)])  # 7


def resolve_equation(a, b, c, x):
    return (a * x) + (b * x) - c


x1 = 5
x2 = 7
x3 = 9

# cria todos os pontos (fixados) de x
x_axis = [
    None,
    x1,
    x2,
    x3
]

# Cria todos os pontos de x resolvendo as equações
y_axis = [
    None,
    resolve_equation(a, b, c, x1),
    resolve_equation(a, b, c, x2),
    resolve_equation(a, b, c, x3)
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
for dot_x, dot_y in zip(x_axis, y_axis):
    plot(
        [dot_x, dot_x],
        [0, dot_y],
        '-',
        linewidth=3
    )

# Desenha todas as coordenadas de 'y'
for dot_x, dot_y in zip(x_axis, y_axis):
    plot(
        [0, dot_x],
        [dot_y, dot_y],
        '-',
        linewidth=3
    )

# Desenha os pontos onde as coordenadas se encontram (x, y)
scatter(
    x_axis,
    y_axis,
    s=100,
    marker='o',
)

# Imprime uma grade
grid()

# Mostra a figura resultante
show()
