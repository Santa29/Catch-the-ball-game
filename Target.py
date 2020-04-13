from random import randrange as rnd, choice

colors = ['red', 'orange', 'yellow', 'green', 'blue']


class TargetBall:
    """The target class. Target can move, take death and rebirth. Each iteration have random values."""

    def __init__(self):
        """Target initialization"""
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(10, 80)
        self.delta_x = rnd(1, 5)
        self.delta_y = rnd(1, 5)
        self.color = choice(colors)
        self.points_value = 100 // self.r

    def move_check(self):
        """Check the border interceptions and calculate the new x, y coordinates to draw a new position of target"""
        if self.x + self.delta_x > 800:
            self.delta_x = rnd(-15, 0, 1)
        elif self.x - self.delta_x < 0:
            self.delta_x = rnd(1, 16, 1)
        if self.y + self.delta_y > 600:
            self.delta_y = rnd(-15, 0, 1)
        elif self.y - self.delta_y < 0:
            self.delta_y = rnd(1, 16, 1)
        self.x += self.delta_x
        self.y += self.delta_y

    def new_ball(self):
        """Create new ball in random location"""
        self.r = rnd(15, 80)
        self.delta_x = rnd(1, 15)
        self.delta_y = rnd(1, 15)
        self.color = choice(colors)
        self.points_value = 100 // self.r
        return self.x + self.r, self.y - self.r, self.x - self.r, self.y + self.r

    @property
    def get_x(self):
        return self.x

    @property
    def get_y(self):
        return self.y

    @property
    def get_r(self):
        return self.r

    @property
    def get_delta_x(self):
        return self.delta_x

    @property
    def get_delta_y(self):
        return self.delta_y
