import math
import Target
from tkinter import *
import time


root = Tk()
canv = Canvas(root, width=800, height=600, bg="white")
canv.pack()


class VictoryPoints:
    """Player name and scores"""
    score = 0
    name = ''


def click(event):
    """If you catch the ball, this function will increase your score. Otherwise it print your total scores"""
    if math.pow((math.pow((first_target.get_x - event.x), 2) + math.pow((first_target.get_y - event.y), 2)), 0.5)\
            <= first_target.get_r:
        player.score += first_target.points_value
        first_target.new_ball()


def move(ball):
    finish = time.time() + 25
    while time.time() < finish:
        first_target.move_check()
        canv.after(50, canv.move(ball, first_target.get_delta_x, first_target.get_delta_y))
        canv.update()


first_target = Target.TargetBall()
ball_target = canv.create_oval(first_target.new_ball(), fill=first_target.color, width=0)
player = VictoryPoints()
player.name = input()
player.score = 0
canv.bind('<Button-1>', click)
move(ball_target)
root.mainloop()
print(player.name, player.score)
