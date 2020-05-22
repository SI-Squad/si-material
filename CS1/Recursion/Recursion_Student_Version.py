"""
Recursive turtle drawing to make a bunch of upside down
"""
import turtle


# Draw a triangle with a depth of 1
def draw_depth_1(length):
    # TODO: Start the color fill and put the pen down


    # TODO: Draw the triangle (Hint: make sure to return to where you started drawing the triangle!)


    # TODO: Pick the pen up and end the fill color
    pass


# Draw depth of 2
def draw_depth_2(length):
    # Hint: Use draw_depth_1 to your advantage to draw depth 2!
    pass


# Draw depth of 3
def draw_depth_3(length):
    # Hint: Use draw_depth_1 AND draw_depth_2 to your advantage to draw depth 3!
    pass


# Make recursive!
def draw_rec(length, depth):
    # TODO: Create the base case
    # TODO: Create the recursive case
    # Hint: Use draw_depth_1 and the repetitive structure you've seen. Don't forget what makes something recursive!
    pass


def main():
    turtle.speed(0)
    turtle.fillcolor("black")
    # TODO: Get a length distance from the user
    length = None

    # TODO: Get a recursive depth from the user
    depth = None
    draw_rec(length, depth)
    turtle.done()


main()