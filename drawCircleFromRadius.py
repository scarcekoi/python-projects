import turtle
from catppuccin import PALETTE

def draw_circle(radius):
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor(PALETTE.mocha.colors.crust.hex)
    t = turtle.Turtle()
    t.hideturtle()
    t.color(PALETTE.mocha.colors.mauve.hex)
    t.speed(5)
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)
    turtle.done()

screen = turtle.Screen()
screen.bgcolor(PALETTE.mocha.colors.crust.hex)
radius_in_inches = screen.numinput("Circle Radius", "Enter the radius of the circle (in inches if you want):", minval=1)
if radius_in_inches:
    radius_in_pixels = radius_in_inches * 10
    draw_circle(radius_in_pixels)