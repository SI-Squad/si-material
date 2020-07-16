"""
SI exercise to simulate a drivethru using a queue
file: driveway.py
Created by Yancarlos Diaz, yxd3549, for the Academic Success Center Supplemental Instruction Program.
"""

from queue import *

def queue_up(drivethru, car):
    """
    Add a car to the end of the drivethru
    """
    # TODO: Add the car to the end of the queue 
    pass


def place_order(drivethru, car):
    """
    Attempts to place an order and drive off.
    A car can place an order only if they're the first one up
    Returns True if succesful, False otherwise
    """
    # TODO: Check if the given car is at the front of the queue
    #   If so, remove the car from the queue and return true
    #   Otherwise, return false
    pass


def print_drivethru(drivethru):
    """
    Prints the current state of the driveway
    Because of the nature of stacks, 
    we can only print the top car and the size of the driveway
    """
    # TODO: Check if the drivethru is empty.
    #   If it is, print a message
    #   Otherwise, print the Front and Back car
    pass


def main():
    """
    Runs the program by making a new drivethru and listening for commands
    """
    # TODO: Make an empty queue to represent the drivethru and print it
    print("Commands: \n \tIn [car]\n \tOut [car]\n \tPrint\n \tQuit")
    while(True):
        command = input("Command: ").lower()
        command = command.split(" ")
        if command[0] == "in":
            # TODO: Place the car at the end of the queue
            print("--{0} queued up--".format(command[1]))
        elif command[0] == "out":
            # TODO: Attempt to place an order and save the result in a variable
            #   Print a different message based on whether the operation was succesful
            pass
        elif command[0] == "print":
            # TODO: display the drivethru
            pass
        elif command[0] == "quit":
            break


if __name__ == "__main__":
    main()

