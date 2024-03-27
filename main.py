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
text_turtle.write("Press Space to start!", align= "center", font = ("Comic Sans MS",40, "bold"))

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
  text_turtle.clear()
  text_turtle.write("Game Over!", align = "center", font = ("Arial", 50, "bold"))
def display_score(score):
  score_turtle.clear()
  score_turtle.setpos(180,180)
  score_turtle.write(score, align = "center", font = ("Arial", 50, "Bold"))
def start_game():
  global game_started
  if game_started:
    return
  game_started = True 
  text_turtle.clear()
  score = 0
  snake_speed = 1
  place_food()
  display_score(score)
  snake.st()
  while True:
    snake.forward(snake_speed)
    if snake.distance(food)<20:
      score +=1
      snake_speed+=1
      place_food()
    if crash():
      game_over()
      break
#def move_up():
  if snake.heading()==180 or snake.heading()==0 or snake.heading==(270):
  snake.setheading(90)
def move_down():
    if snake.heading()==180 or snake.heading==0 or snake.heading==(270)
def move_right():
  if snake.heading()==90 or snake.heading()==270 or snake.heading()==0:
def move_left():
  if snake.heading()==90 or snake.heading()==270 or snake.heading==0: 
  snake.setheading(180)
window = t.Screen()
window.onkey(move_up, "Up")
window.onkey(move_down,"Down")
window.onkey(move_left,"Left")
window.onkey(move_right, "Right")
window.onkey(start_game, "Space")
window.listen()
t.mainloop()  