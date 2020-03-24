from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']


class Target:
    """The target class. Target can move, take death and rebirth. Each iteration have random values."""
    def __init__(self):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(15, 80)
        self.delta_x = rnd(1, 15)
        self.delta_y = rnd(1, 15)
        self.color = choice(colors)
        self.points_value = 100 // self.r
        self.ball = canv.create_oval(self.x + self.r, self.y + self.r, self.x - self.r, self.y - self.r, self.color)

    def move(self):
        if self.x + self.delta_x > 800:
            self.delta_x = -1 * self.delta_x
        if self.x - self.delta_x < 0:
            self.delta_x = -1 * self.delta_x
        if self.y + self.delta_y > 600:
            self.delta_x = -1 * self.delta_x
        if self.y + self.delta_y < 0:
            self.delta_x = -1 * self.delta_x
        canv.move(self.ball, self.delta_x, self.delta_y)
        self.x += self.delta_x
        self.y += self.delta_y

    def death(self):
        canv.delete(self.ball)

    def new_ball(self):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(15, 80)
        self.delta_x = rnd(1, 15)
        self.delta_y = rnd(1, 15)
        self.color = choice(colors)
        self.points_value = 100 // self.r
        self.ball = canv.create_oval(self.x + self.r, self.y + self.r, self.x - self.r, self.y - self.r, self.color)

    @property
    def get_x(self):
        return self.x

    @property
    def get_y(self):
        return self.y

    @property
    def get_r(self):
        return self.r
