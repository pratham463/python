import turtle
import pygame
import random

# Function to draw a rectangle
def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Function to display dice dots
def draw_dots(x, y, number):
    positions = {
        1: [(0, 0)],
        2: [(-20, 20), (20, -20)],
        3: [(-20, 20), (0, 0), (20, -20)],
        4: [(-20, 20), (20, 20), (-20, -20), (20, -20)],
        5: [(-20, 20), (20, 20), (0, 0), (-20, -20), (20, -20)],
        6: [(-20, 20), (20, 20), (-20, 0), (20, 0), (-20, -20), (20, -20)],
    }
    turtle.penup()
    turtle.color("black")
    for pos in positions[number]:
        turtle.goto(x + pos[0], y + pos[1])
        turtle.dot(10)

# Function to roll dice and display results
def roll_dice():
    turtle.clear()
    dice_results = [random.randint(1, 6) for _ in range(2)]  # Two dice rolls
    x_positions = [-150, 50]  # Separate rectangles for dice

    for i, result in enumerate(dice_results):
        draw_rectangle(x_positions[i], 50, 100, 100, "white")  # Draw dice rectangle
        draw_dots(x_positions[i] + 50, 100, result)  # Draw dice dots

# Setup turtle screen
screen = turtle.Screen()
screen.title("Dice Rolling Simulator")
screen.bgcolor("lightblue")

# Roll dice on click
screen.listen()
screen.onkey(roll_dice, "space")  # Press 'Space' to roll dice

# Instructions
turtle.penup()
turtle.goto(0, -150)
turtle.write("Press SPACE to roll the dice!", align="center", font=("Arial", 16, "bold"))

turtle.hideturtle()
turtle.done()