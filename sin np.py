# Created by Helga on 02.10.2020

import matplotlib.pyplot as plt
import numpy as np
from math import sin

# #  Данные:
x = np.linspace(0, 10, 100)
y2 = np.sin(x) / 1 + np.sin(3 * x) / 3 + np.sin(5 * x) / 5 + np.sin(7 * x) / 7 + np.sin(
9 * x) / 9 + np.sin(11 * x) / 11 + np.sin(13 * x) / 13 + np.sin(15 * x) / 15 + np.sin(17 * x) / 17 + np.sin(
19 * x) / 19 + np.sin(21 * x) / 21 + np.sin(23 * x) / 23 + np.sin(25 * x) / 25 + np.sin(27 * x) / 27 + np.sin(
29 * x) / 29 + np.sin(31 * x) / 31 + np.sin(33 * x) / 33 + np.sin(35 * x) / 35 + np.sin(37 * x) / 37 + np.sin(
39 * x) / 39 + np.sin(41 * x) / 41

#  Создаем "Figure" и "Axes":
ax_2 = plt.figure().add_subplot(2, 1, 1)

#  Методы, отображающие данные:
ax_2.plot(x, y2)

plt.show()

