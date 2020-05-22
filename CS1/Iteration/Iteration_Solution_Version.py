"""
A iterative turtle drawing solution to learn how to work on iterative skills and move from recursion to iteration.
Created by Emma Lubes, eml5244, for the Academic Success Center Supplemental Instruction Program.
"""
import turtle


# Draw depth of 1
def draw_depth_1(length):
    # TODO: Start the color fill and put the pen down
    turtle.begin_fill()
    turtle.down()
    # TODO: Draw the triangle (Hint: make sure to return to where you started drawing the triangle!)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    # TODO: Pick the pen up and end the fill color
    turtle.up()
    turtle.end_fill()


# Finish this recursive function!
def draw_rec(length, depth):
    # TODO: Create the base case
    if depth == 1:
        draw_depth_1(length)
    # TODO: Finish the recursive case
    # Hint: Enter the correct calls to make the function recursive!
    else:
        draw_rec(length, 1)
        turtle.forward(length/2)
        turtle.left(120)
        turtle.forward(length/2)
        turtle.right(120)
        draw_rec(length/2, depth-1)
        turtle.right(60)
        turtle.forward(length/2)
        turtle.left(60)
        turtle.forward(length/2)
        turtle.right(120)
        turtle.forward(length/2)
        turtle.left(120)
        draw_rec(length/2, depth-1)
        turtle.right(120)
        turtle.forward(length/2)
        turtle.right(120)
        turtle.forward(length/2)
        turtle.left(60)
        turtle.forward(length/2)
        turtle.left(180)
        draw_rec(length/2, depth-1)
        turtle.forward(length/2)
        turtle.left(120)
        turtle.forward(length/2)
        turtle.right(120)


def draw_tail_rec(length, depth):
    if depth == 0:
        pass
    else:
        pass


def draw_iter(length, depth):
    while depth > 0:
        pass


def main():
    # TODO: Get a length distance from the user
    length = int(input("Enter a length: "))
    # TODO: Get a recursive depth from the user
    depth = int(input("Enter a recursive depth: "))
    turtle.speed(0)
    turtle.fillcolor("black")
    # TODO Make the iterative call
    draw_rec(length, depth)
    turtle.done()

