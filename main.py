from turtle import Screen
import time
from scoreboard import Score
from boarder import Border
from players import Player
from ball import Ball

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

ball = Ball()
score = Score()
border = Border()
player1 = Player((350, 0))
player2 = Player((-350, 0))

screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")
screen.onkey(player2.go_up, "w")
screen.onkey(player2.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.001)
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(player1) < 50 and ball.xcor() > 330 or ball.distance(player2) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.reset_position()
        score.score1_increment()
    if ball.xcor() < -370:
        ball.reset_position()
        score.score2_increment()

    if score.score_1 == 5 or score.score_2 == 5:
        score.game_over()
        game_is_on=False

screen.exitonclick()
