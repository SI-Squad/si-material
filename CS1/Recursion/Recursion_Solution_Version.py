import turtle


# Draw depth of 1
def draw_depth_1(length):
    # TO-DO: Start the color fill and put the pen down
    turtle.begin_fill()
    turtle.down()
    # TO-DO: Draw the triangle (Hint: make sure to return to where you started drawing the triangle!)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    # TO-DO: Pick the pen up and end the fill color
    turtle.up()
    turtle.end_fill()


# Draw depth of 2
def draw_depth_2(length):
    # Hint: Use draw_depth_1 to your advantage to draw depth 2!
    draw_depth_1(length)
    turtle.forward(length/2)
    turtle.left(120)
    turtle.forward(length/2)
    turtle.right(120)
    draw_depth_1(length/2)
    turtle.right(60)
    turtle.forward(length/2)
    turtle.left(60)
    turtle.forward(length/2)
    turtle.right(120)
    turtle.forward(length/2)
    turtle.left(120)
    draw_depth_1(length/2)
    turtle.right(120)
    turtle.forward(length/2)
    turtle.right(120)
    turtle.forward(length/2)
    turtle.left(60)
    turtle.forward(length/2)
    turtle.left(180)
    draw_depth_1(length/2)
    turtle.forward(length/2)
    turtle.left(120)
    turtle.forward(length/2)
    turtle.right(120)


# Draw depth of 3
def draw_depth_3(length):
    # Hint: Use draw_depth_1 AND draw_depth_2 to your advantage to draw depth 3!
    draw_depth_1(length)
    turtle.forward(length / 2)
    turtle.left(120)
    turtle.forward(length / 2)
    turtle.right(120)
    draw_depth_2(length / 2)
    turtle.right(60)
    turtle.forward(length / 2)
    turtle.left(60)
    turtle.forward(length / 2)
    turtle.right(120)
    turtle.forward(length / 2)
    turtle.left(120)
    draw_depth_2(length / 2)
    turtle.right(120)
    turtle.forward(length / 2)
    turtle.right(120)
    turtle.forward(length / 2)
    turtle.left(60)
    turtle.forward(length / 2)
    turtle.left(180)
    draw_depth_2(length / 2)
    turtle.forward(length / 2)
    turtle.left(120)
    turtle.forward(length / 2)
    turtle.right(120)


# Make recursive!
def draw_rec(length, depth):
    # TO-DO: Create the base case
    if depth == 1:
        draw_depth_1(length)
    # TO-DO: Create the recursive case
    # Hint: Use the repetitive structure you've seen. Don't forget what makes something recursive!
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


def main():
    # TO-DO: Get a length distance from the user
    length = int(input("Enter a length: "))
    # TO-DO: Get a recursive depth from the user
    depth = int(input("Enter a recursive depth: "))
    turtle.speed(0)
    turtle.fillcolor("black")
    draw_rec(length, depth)
    turtle.done()


main()
