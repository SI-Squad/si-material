"""
A iterative turtle drawing to learn how to work on iterative skills and move from recursion to iteration.
Created by Emma Lubes, eml5244, for the Academic Success Center Supplemental Instruction Program.
"""
import turtle
import random

"""
A function which uses the random package to generate 3 random integers for RGB colors and returns it as a tuple which 
is then passed into turtle.color() to change the color of the line segement
"""
def ran_color_gen():
    color1 = random.randrange(0, 256)
    color2 = random.randrange(0, 256)
    color3 = random.randrange(0, 256)
    return color1, color2, color3


# Make the tail recursive function
def draw_tail_rec(length):
    # TODO: Make the base case
    # TODO: Make the recursive case
    # Hint: These color changing lines should go right before the end of the function!
        tup = ran_color_gen()
        turtle.color(tup)


# Make the recursive function
def draw_iter(length):
    # TODO: Set up the loop
        tup = ran_color_gen()
        turtle.color(tup)
        # TODO: Draw the spiral



def main():
    # TODO: Get a length distance from the user
    length = None
    turtle.speed(0)
    turtle.colormode(255)
    # TODO Make the iterative call

    turtle.hideturtle()
    turtle.done()

main()
