"""
SI exercise to simulate a driveway using a stack
file: driveway.py
Created by Yancarlos Diaz, yxd3549, for the Academic Success Center Supplemental Instruction Program.
"""

from stack import *

def drive_in(driveway, car):
    """
    Add a car to the end of the driveway
    """
    push(driveway, car)


def drive_out(driveway, car):
    """
    Attempts to drive out of the driveway
    Returns True if succesful, False otherwise
    """
    if top(driveway) == car:
        pop(driveway)
        return True
    else:
        return False


def print_driveway(driveway):
    """
    Prints the current state of the driveway
    Because of the nature of stacks, 
    we can only print the top car and the size of the driveway
    """
    if is_empty(driveway):
        print("--Empty Driveway--")
    else:
        top_car = top(driveway)
        driveway_size = size(driveway)
        print("Driveway(Top: {0}, Size: {1})".format(top_car, driveway_size))


def main():
    """
    Runs the program by making a new driveway and listening for commands
    """
    driveway = make_empty_stack()
    print_driveway(driveway)
    print("Commands: \n \tIn [car]\n \tOut [car]\n \tPrint\n \tQuit")
    while(True):
        command = input("Command: ").lower()
        command = command.split(" ")
        if command[0] == "in":
            drive_in(driveway, command[1])
            print("--Drove {0} in--".format(command[1]))
        elif command[0] == "out":
            success = drive_out(driveway, command[1])
            if not success:
                print("--Could not drive {0} out--".format(command[1]))
            else:
                print("--Drove {0} out--".format(command[1]))
        elif command[0] == "print":
            print_driveway(driveway)
        elif command[0] == "quit":
            break


if __name__ == "__main__":
    main()

