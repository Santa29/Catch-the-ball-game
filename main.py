import math
import Target


class VictoryPoints:
    """Player name and scores"""
    score = 0
    name = ''


def click(event):
    """If you catch the ball, this function will increase your score. Otherwise it print your total scores"""
    if math.pow((math.pow(first_target.get_x() - event.x, 2) + math.pow(first_target.get_y() - event.y, 2)), 0.5)\
            <= first_target.get_r():
        player.score += 1
    first_target.death()
    first_target.new_ball()


first_target = Target.TargetBall()
player = VictoryPoints()
player.name = input()
player.score = 0
Target.canv.bind('<Button-1>', click)
first_target.move()
Target.root.mainloop()
# print(player.name, player.score)
