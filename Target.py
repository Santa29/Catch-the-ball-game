from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']


class Target:
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

    def death(self):
        canv.delete(self.ball)
