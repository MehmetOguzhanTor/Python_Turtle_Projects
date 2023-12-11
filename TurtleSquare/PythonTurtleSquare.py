import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
my_turtle = turtle.Turtle()

# Make the turtle draw a square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Close the turtle graphics window on click
screen.exitonclick()
