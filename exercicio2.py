import matplotlib.pyplot as plt
import numpy as np

# https://matplotlib.org/stable/users/getting_started/index.html
RU = "3710807".replace("0", "1")

num1 = int(RU[-(len(RU) - 1)])
num2 = int(RU[-(len(RU) - 2)])
num3 = int(RU[-(len(RU) - 3)])

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
