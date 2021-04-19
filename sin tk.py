# Created by Helga on 19.04.2021
from math import sin
from tkinter import *

# Создаем окно программы
window = Tk()

# Создаем область для рисования
c = Canvas(window, width=800, height=300, bg="black")
c.pack()

i = 0
point = []


def find_y(n, x):  # расчет y - т.е сумма синусов для нужного n (sin(x)/1 + sin(3x/3) + sin(5x)/5 + sin(7x)/7) и т.д.
    func = 0
    for i in range(1, n, 2):  # c с шагом, т.к функция нечетная
        func += sin(i * x) / i

    return func


def render():  # отрисовка меняющихся значений
    global i, point
    s = -1
    for i in range(0, len(point), 2):  # смещаем x
        point[i] += 1

    x = i * 0.04  # расчет x (маленькие значения для точности функции)
    y = find_y(spin_var.get(), x)  # считаем y
    x *= 100  # масштабирование
    y *= 100
    point.append(150)
    point.append(150 - y)
    if len(point) > 2:  # для линии - 2 точки
        c.coords(hline, point)  # отрисовка
    i = i + 1
    c.after(30, render)  # отрисовка с задержкой


count = 0
spin_var = IntVar(window, count)  # для изменения кол-ва итераций в функции
spin = Spinbox(window, from_=1, to=100, width=5, wrap=True, textvariable=spin_var)
spin.place(x=50, y=250)

hline = c.create_line(0, 0, 0, 0, width=2, fill='violet red')

render()
window.mainloop()