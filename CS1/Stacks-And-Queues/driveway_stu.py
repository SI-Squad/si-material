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
    # TODO: Add the car to the top of the stack
    pass


def drive_out(driveway, car):
    """
    Attempts to drive out of the driveway
    Returns True if succesful, False otherwise
    """
    # TODO: Check if the given car is at the top of the stack
    #   If so, remove it and return true. Otherwise, return false
    pass


def print_driveway(driveway):
    """
    Prints the current state of the driveway
    Because of the nature of stacks, 
    we can only print the top car and the size of the driveway
    """
    # TODO: If the driveway is empty, print an apropriate message
    #   Otherwise, print the car at the top of the stack and the size of the driveway
    pass


def main():
    """
    Runs the program by making a new driveway and listening for commands
    """
    # TODO: Create an empty stack to represent the driveway and print it
    print("Commands: \n \tIn [car]\n \tOut [car]\n \tPrint\n \tQuit")
    while(True):
        command = input("Command: ").lower()
        command = command.split(" ")
        if command[0] == "in":
            # TODO: Add the car to the driveway
            print("--Drove {0} in--".format(command[1]))
        elif command[0] == "out":
            # TODO: Try to remove the car and store the result in a variable
            #   Print an appropriate message based on the operation's success
            pass
        elif command[0] == "print":
            # TODO: Print the driveway
            pass
        elif command[0] == "quit":
            break


if __name__ == "__main__":
    main()

