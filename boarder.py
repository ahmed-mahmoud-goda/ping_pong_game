from turtle import Turtle
borders_x = 380
borders_y = 295
class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.width(5)
        self.penup()
        self.hideturtle()
        self.goto(borders_x,borders_y)
        self.pendown()
        self.draw_border()

    def draw_border(self):
        self.goto(borders_x,-borders_y)
        self.goto(-borders_x,-borders_y)
        self.goto(-borders_x,borders_y)
        self.goto(borders_x,borders_y)