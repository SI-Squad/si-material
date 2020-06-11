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
    enqueue(drivethru, car)


def place_order(drivethru, car):
    """
    Attempts to place an order and drive off.
    A car can place an order only if they're the first one up
    Returns True if succesful, False otherwise
    """
    if front(drivethru) == car:
        dequeue(drivethru)
        return True
    else:
        return False


def print_drivethru(drivethru):
    """
    Prints the current state of the driveway
    Because of the nature of stacks, 
    we can only print the top car and the size of the driveway
    """
    if is_empty(drivethru):
        print("--Empty Drivethru--")
    else:
        front_car = front(drivethru)
        back_car = back(drivethru)
        print("Drivethru(Front: {0}, Back: {1})".format(front_car, back_car))



def main():
    """
    Runs the program by making a new drivethru and listening for commands
    """
    drivethru = make_empty_queue()
    print_drivethru(drivethru)
    print("Commands: \n \tIn [car]\n \tOut [car]\n \tPrint\n \tQuit")
    while(True):
        command = input("Command: ").lower()
        command = command.split(" ")
        if command[0] == "in":
            queue_up(drivethru, command[1])
            print("--{0} queued up--".format(command[1]))
        elif command[0] == "out":
            success = place_order(drivethru, command[1])
            if not success:
                print("-- It's not {0}'s turn!--".format(command[1]))
            else:
                print("-- {0} ordered and drove off happily--".format(command[1]))
        elif command[0] == "print":
            print_drivethru(drivethru)
        elif command[0] == "quit":
            break


if __name__ == "__main__":
    main()

