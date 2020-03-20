from tkinter import *
from random import randrange as rnd, choice
import math
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']


class VictoryPoints:
    """Player name and scores"""
    score = 0
    name = ''


class Target:
    """Create new ball"""
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    delta_x = rnd(1, 15)
    delta_y = rnd(1, 15)
    score_value = r // 10
    canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)

    def move(self, x, y, r, delta_x, delta_y):
        """Move the ball to the new direction"""
        if x + delta_x > 800:
            delta_x = -delta_x
        elif x - delta_x < 0:
            delta_x = -delta_x
        elif y + delta_x > 600:
            delta_y = - delta_y
        elif y - delta_y < 0:
            delta_y = -delta_y
        else:
            x += delta_x
            y += delta_y
        canv.delete(self)
        canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)

    def death(self):
        """Destroy the object"""
        del self


def click(event):
    """If you catch the ball, this function will increase your score. Otherwise it print your total scores"""
    if math.pow((math.pow(first_target.x - event.x, 2) + math.pow(first_target.y - event.y, 2)), 0.5) <= first_target.r:
        player.score += 1
    return player.score


first_target = Target()
player = VictoryPoints()
player.name = input()
player.score = 0
canv.bind('<Button-1>', click)
finish = time.time() + 5

while time.time() < finish:
    pass
mainloop()
print(player.name, player.score)
