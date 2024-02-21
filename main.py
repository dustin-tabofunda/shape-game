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
score_turtle = t.Turtle()
score_turtle.penup()
score_turtle.ht()

def crash():
  left_wall = -200
  right_wall = 200
  top_wall = 200
  bottom_wall = -200
  (x,y) = snake.position()
  outside = x>right_wall or y>top_wall or y<bottom_wall or x<left_wall
  return outside
def place_food():
  food.hideturtle()
  food.setpos(random.randint(-180,180),random.randint(-180,180))
  food.showturtle()
def game_over():
  snake.hideturtle()
  food.hideturtle()
  text_turtle.clear
  text_turtle.write("Game Over!", align = "center", font = ("Arial", 50, "bold"))
def display_score(score):
  score_turtle.clear
  score_turtle.setpos(180,180)
  score_turtle.write(score, alig)
t.mainloop()