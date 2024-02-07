import turtle
import time

# Function to draw a cow with mogogolwane
def draw_cow():
    turtle.color("brown")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-20, 50)
    turtle.pendown()

    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    # Draw mogogolwane
    turtle.penup()
    turtle.goto(-40, 70)
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(20)
    turtle.end_fill()

# Function to draw a cat
def draw_cat():
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

# Function to draw a mouse
def draw_mouse():
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

# Function to animate the story
def animate_story():
    turtle.speed(1)

    # Scene 1: Cow with mogogolwane
    draw_cow()
    turtle.write("Cow with Mogogolwane", align="center", font=("Arial", 14, "normal"))
    time.sleep(2)
    turtle.clear()

    # Scene 2: Cat approaching Cow
    draw_cow()
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    draw_cat()
    turtle.write("Cat approaches Cow", align="center", font=("Arial", 14, "normal"))
    time.sleep(2)
    turtle.clear()

    # Scene 3: Animals searching for Cat
    turtle.write("Animals searching for Cat", align="center", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    for _ in range(4):
        draw_mouse()
        turtle.forward(30)
    time.sleep(2)
    turtle.clear()

    turtle.hideturtle()

# Run the animation
animate_story()

# Keep the window open
turtle.mainloop()
exec(open("c:/Users/User/Downloads/The Great Cow - ZAR ANIMATION HOUSE.py").read())