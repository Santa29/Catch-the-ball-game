from tkinter import *
import math
import time
import Target

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']


class VictoryPoints:
    """Player name and scores"""
    score = 0
    name = ''


def click(event):
    """If you catch the ball, this function will increase your score. Otherwise it print your total scores"""
    if math.pow((math.pow(first_target.get_x() - event.x, 2) + math.pow(first_target.get_y() - event.y, 2)), 0.5)\
            <= first_target.get_r():
        player.score += 1
    return player.score


first_target = Target
player = VictoryPoints()
player.name = input()
player.score = 0
first_target_catch = True
canv.bind('<Button-1>', click)
mainloop()
# print(player.name, player.score)
