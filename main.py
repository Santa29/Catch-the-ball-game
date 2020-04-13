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
    if math.pow((math.pow((second_target.get_x - event.x), 2) + math.pow((second_target.get_y - event.y), 2)), 0.5)\
            <= second_target.get_r:
        player.score += second_target.points_value
        second_target.new_ball()
    if math.pow((math.pow((third_target.get_x - event.x), 2) + math.pow((third_target.get_y - event.y), 2)), 0.5)\
            <= third_target.get_r:
        player.score += third_target.points_value
        third_target.new_ball()


def move(ball_1, ball_2, ball_3):
    finish = time.time() + 25
    while time.time() < finish:
        first_target.move_check()
        second_target.move_check()
        third_target.move_check()
        canv.after(10, canv.move(ball_1, first_target.get_delta_x, first_target.get_delta_y))
        canv.after(10, canv.move(ball_2, second_target.get_delta_x, second_target.get_delta_y))
        canv.after(10, canv.move(ball_3, third_target.get_delta_x, third_target.get_delta_y))
        canv.update()


first_target = Target.TargetBall()
second_target = Target.TargetBall()
third_target = Target.TargetBall()
ball_target_1 = canv.create_oval(first_target.new_ball(), fill=first_target.color, width=0)
ball_target_2 = canv.create_oval(second_target.new_ball(), fill=second_target.color, width=0)
ball_target_3 = canv.create_oval(third_target.new_ball(), fill=third_target.color, width=0)
player = VictoryPoints()
player.name = input()
player.score = 0
canv.bind('<Button-1>', click)
move(ball_target_1, ball_target_2, ball_target_3)
root.mainloop()
print(player.name, player.score)
