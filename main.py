from turtle import Turtle, Screen
import random


def move_forward(x):    # Function to move the turtle forward by a random integral distance from 1 to 10 (both included)
    return x.forward(random.randint(1, 10))

# ************************ Graphical interface settings *************************
screen = Screen()
screen.colormode(255)
screen.title('Turtle Race')
screen.setup(width=600, height=600)
# *******************************************************************

color = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

while True:     # Error checking. Keeps asking the user for input till they enter a proper value
    prediction = screen.textinput(title='Make a prediction', prompt='Enter the colour of turtle you support:').lower()
    if prediction not in color:
        print('Please enter VIBGYOR colour.')
        continue
    else:
        break

turtles = [Turtle(shape='turtle') for _ in range(7)]  # create a list of 7 objects of Turtle class

is_race_on = True
y_index = [-150, -100, -50, 0, 50, 100, 150]        # Y-coordinates of starting position of turtles

for turtle in turtles:  # This is to move the turtles to the starting position
    turtle.penup()
    turtle.color(color[turtles.index(turtle)])
    turtle.goto(-290, y_index[turtles.index(turtle)])

while is_race_on:
    for turtle in turtles:
        turtle.fd(random.randint(1, 10))
        pos_x = turtle.xcor()
        if pos_x >= 290:    # Winner is decided here
            winner = turtle.pencolor()
            is_race_on = False
            break

if prediction == winner:   # Comparing user prediction to actual winnner
    print(f'You win. The winner is {winner.upper()} coloured turtle')
else:
    print(f'You lose. The winner is {winner.upper()} coloured turtle.')

screen.exitonclick()
