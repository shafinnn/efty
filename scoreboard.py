from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.right_score = 0
        self.left_score = 0
        self.update()

    def update(self):
        self.goto(-100, 210)
        self.write(f'SK {self.left_score}', align='center', font=('Arial', 30, 'normal'))
        self.goto(100, 210)
        self.write(f'SRK {self.right_score}', align='center', font=('Arial', 30, 'normal'))

    def increase_left(self):
        self.left_score += 1
        self.clear()
        self.update()

    def increase_right(self):
        self.right_score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER SEXY!!', align='center', font=('Arial', 15, 'normal'))


