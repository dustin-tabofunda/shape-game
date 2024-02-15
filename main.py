import turtle as t
import random

t.speed(0)
t.ht()
t.penup()
t.goto(-200,200)
t.pendown()
t.forward(400)
t.right(90)
t.forward(400)
t.right(90)
t.forward(400)
t.right(90)
t.forward(400)
t.penup()
t.goto(0, 0)
snake = t.Turtle()
snake.penup()
snake.hideturtle()
snake.speed(0)
snake.shape("square")
food = t.Turtle()
food.penup()
food.hideturtle()
food.speed(0)
food.shape("triangle")
game_started = False
text_turtle = t.Turtle()
text_turtle.penup()
text_turtle.ht()

def crash():
  left_wall = -200
  right_wall = 200
  top_wall = 200
  bottom_wall = -200
  
t.mainloop()