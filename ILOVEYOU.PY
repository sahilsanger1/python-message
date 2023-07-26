import turtle

def draw_heart(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

def heart_animation():
    screen = turtle.Screen()
    screen.bgcolor('white')
    screen.title('I love You')

    turtle.speed(1)

    # Draw the heart
    draw_heart(0, 0)

    # Show the "I Love You" message
    turtle.penup()
    turtle.goto(0, -150)
    turtle.color('black')
    turtle.write("I Love You", align="center", font=("Arial", 24, "normal"))

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    heart_animation()