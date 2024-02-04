import turtle
import time
import random
#import winsound

delay = 60  # milliseconds
score = 0
high_score = 0

#muza nie dziala ;c
#winsound.PlaySound("muza.wav", winsound.SND_ASYNC)

# Okno gry
wn = turtle.Screen()
wn.title("Rudol")
wn.bgcolor("white")
wn.setup(width=700, height=700)
wn.tracer(0)

#border
border = turtle.Turtle()
border.speed(0)
border.penup()
border.color("black")
border.goto(-290, -290)
border.pendown()
border.pensize(2)
for _ in range(4):
    border.forward(580)
    border.left(90)
border.hideturtle()

# Glowa
head = turtle.Turtle()
head.speed(0)
head_image = ("kot.gif")
wn.register_shape(head_image)
head.shape(head_image)
#head.shape("square")
#head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Jedzenie
food = turtle.Turtle()
food.speed(0)
food_image = "mysz.gif"
wn.register_shape(food_image)
food.shape(food_image)
food.penup()
food.goto(0, 100)

segments = []

# Funkcje
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Klawiatura
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# loop gry
def game_loop():

    global score, high_score

    wn.update()



    # Sprawdzenie kolizji z jedzeniem
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Dodaj tulow
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("turtle")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        # Zwieksz wynik
        score += 10

        if score > high_score:
            high_score = score

    # Tulow 
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # tulow do glowy
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Ruch 
    move()

    # Kolizja z sciana
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_game()

    # Kolizja z samym soba
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()


    display_score()

    # Delay
    wn.ontimer(game_loop, delay)

# Funkcja resetu
def reset_game():
    global score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "Stop"

    # ukryj tulow
    for segment in segments:
        segment.goto(1000, 1000)

    # clear
    segments.clear()

    # reset
    score = 0


    display_score()

# Stworz turtla dla wyniku
text_turtle = turtle.Turtle()
text_turtle.speed(0)
text_turtle.color("black")
text_turtle.penup()
text_turtle.hideturtle()
text_turtle.goto(0, 300)

# Wyswietl wynik
def display_score():
    text_turtle.clear()
    text_turtle.write("Wynik: {}  Najlepszy wynik: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# Start gry
game_loop()

display_score()

# Start glownego loopa
wn.mainloop()
