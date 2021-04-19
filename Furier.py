from tkinter import *
from math import *

root = Tk()
c = Canvas(root, width=1500, height=600, bg="black")
c.pack()

headX = 500
headY = 0
rounds = []
points = []


class Round:
    def __init__(self, canvas, center, dist, angleSpeed, color):
        self.angleSpeed = angleSpeed
        self.angle = 0  # текущий угол
        self.radius = 2  # радиус кружка
        self.canvas = canvas  # ссылка на рисовалку для удобства
        self.center = center  # центр окружности
        self.dist = dist  # расстояние до центра
        self.x, self.y = self.p2c()  # преобразуем угол в координаты.
        self.oval = canvas.create_oval(center[0] - dist, center[1] - dist, center[0] + dist, center[1] + dist,
                                       outline='white')
        self.dot = canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius,
                                      self.y + self.radius, fill=color)
        self.line = canvas.create_line(self.x, self.y, center[0], center[1], width=2, fill=color)

    def update(self):
        self.x, self.y = self.p2c()  # Вычисляем новые координаты
        self.canvas.coords(self.dot, self.x - self.radius, self.y - self.radius, self.x + self.radius,
                           self.y + self.radius)
        self.canvas.coords(self.line, self.x, self.y, self.center[0], self.center[1])
        self.angle += self.angleSpeed  # Увеличиваем угол

    def setpos(self, x, y):
        self.center[0] = x
        self.center[1] = y
        self.canvas.coords(self.oval, self.center[0] - self.dist, self.center[1] - self.dist,
                           self.center[0] + self.dist, self.center[1] + self.dist)

    def p2c(self):  # Преобразование от полярных к декартовым.
        return cos(self.angle) * self.dist + self.center[0], sin(self.angle) * self.dist + self.center[1]

    def clear(self):
        c.delete(self.dot)
        c.delete(self.line)
        c.delete(self.oval)


def createrounds(n, func):
    R, S = 150, -0.05
    radius = R
    speed = S
    for i in range(n):
        rounds.append(Round(c, [300, 300], radius, speed, 'white'))
        if func == 1:
            k = 2 * i + 3
        else:
            k = i + 2
        radius = R / k
        speed = S * k


def render():
    rx = 0
    ry = 0
    for r in rounds:
        if rx != 0:
            r.setpos(rx, ry)
        r.update()
        rx = r.x
        ry = r.y
    for i in range(0, len(points), 2):
        points[i] += 3
    points.append(headX)
    points.append(ry)
    c.coords(hline, rx, ry, headX, ry)
    if len(points) > 2:
        c.coords(line, points)
    c.after(30, render)


def func():
    f_text = spin2_var.get()
    if f_text == FUNC1:

        f2 = 1
    else:
        f2 = 2
    for i in rounds:
        i.clear()
    rounds.clear()
    points.clear()
    createrounds(spin_var.get(), f2)


FUNC1 = 'Прямоугольная функиция'
FUNC2 = 'Пилообразная функиция'

f_text = FUNC1
count, s, f, f2 = 1, 1, 1, 1
c.create_text(50, 50, anchor=NW, font="Arial",
              text="РЯДЫ ФУРЬЕ", fill="white")

spin_var = IntVar(root, count)
spin = Spinbox(root, from_=1, to=100, width=5, wrap=True, textvariable=spin_var, command=func)
spin.place(x=50, y=500)

spin2_var = StringVar(root, f_text)
spin2 = Spinbox(root, values=(FUNC1, FUNC2), width=25, textvariable=spin2_var, command=func)
spin2.place(x=50, y=530)

createrounds(1, 1)

hline = c.create_line(0, 0, 0, 0, width=2, fill='yellow')
line = c.create_line(0, 0, 0, 0, width=2, fill='medium violet red')

render()
root.mainloop()