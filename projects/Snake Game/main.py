# imports
import turtle as t
import random
import time

# global variables
height = 600
width = 900
score = 0
high_score = 0
snake_body = []
scorekeeper = t.Turtle()
delay = 0.1

# setup
screen = t.Screen()
screen.setup(width = width, height = height)
screen.title("Snake Game")
screen.bgcolor("black")

head = t.Turtle()
head.shape("square")
head.color("dark green")
head.penup()
head.goto(0, 0)
head.direction = "stop"
head.speed(1)

food = t.Turtle()
food.shape('circle')
food.color("red")
food.speed(0)
food.penup()
food.goto(100, 100)


def scoreboard(score): 
    scorekeeper.clear()
    scorekeeper.hideturtle()
    scorekeeper.penup()
    scorekeeper.pencolor("white")
    scorekeeper.goto(325, 250)
    scorekeeper.pendown()
    scorekeeper.write('Score: ' + str(score), font = ('Oswald', 18))
scoreboard(score)

def generate_food():
    food_giver = t.Turtle()
    food_giver.hideturtle()

def auto_move():
    head.speed(1)
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


def moveright():
    if head.direction != "left":
        head.direction = "right"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

screen.listen()

t.onkeypress(moveright, "Right")
t.onkeypress(moveleft, "Left")
t.onkeypress(moveup, "Up")
t.onkeypress(movedown, "Down")

# moving logic
while True:
    screen.update()

    # collision control
    if head.xcor() < -450 or head.xcor() > 450 or head.ycor() < -300 or head.ycor() > 300:
        head.speed(0)
        head.goto(0,0)
        head.direction = 'stop'
        for i in range(len(snake_body)):
            snake_body[i].goto(10000, 10000)
        snake_body.clear()
        score = 0
        dealy = 0.1

    # adding segment (increasing snake size)
    if head.distance(food) < 15:
        random_y = random.randint(-290, 290)
        random_x = random.randint(-440, 440)
        food.goto(random_x, random_y)

        scale = t.Turtle()
        scale.shape("square")
        scale.color("green")
        scale.penup()
        scale.speed(0)
        snake_body.append(scale)
        delay -= 0.001
        score += 10
        scoreboard(score)

    for i in range(len(snake_body) - 1, 0, -1):
        x = snake_body[i-1].xcor()
        y = snake_body[i-1].ycor()
        snake_body[i].goto(x, y)
    
    if len(snake_body) > 0:
        x, y = head.xcor(), head.ycor()
        snake_body[0].goto(x, y)

    auto_move()

    for segment in snake_body:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.speed(0)
            head.goto(0,0)
            head.direction = 'stop'
            for i in range(len(snake_body)):
                snake_body[i].goto(10000, 10000)
            snake_body.clear()
            score = 0
            delay = 0.1
            scoreboard(score)
                
    time.sleep(delay)
t.done()