package Backtracking;

import java.util.ArrayList;
import java.util.Collections;

/**
 * This class represents one of the rules or regions in a KenKen puzzle
 */
public class Rule {

    /* An array of coordinates to represent the cells in this region */
    private Coordinate[] cells;
    /* The goal number that these regions must add/subtract/multiply to */
    private int goal;
    /* The operation to perform with the numbers in the region */
    private Operation operation;

    /**
     * Simple (auto-generated) constructor for a Rule
     */
    public Rule(Coordinate[] cells, int goal, Operation operation) {
        this.cells = cells;
        this.goal = goal;
        this.operation = operation;
    }

    /**
     * This method checks whether the cells in this region satisfy the requirements
     * TODO: Group B
     */
    public boolean isSatisfied(int[][] board){
        ArrayList<Integer> numbers = new ArrayList<>();
        // TODO: Get all the numbers from the board and stored them in the numbers array


        // This line sorts the array in descending order so that the subtraction
        // works properly
        Collections.sort(numbers, Collections.reverseOrder());

        // TODO: Check which operation we're dealing with
        //  If we have a sum, we want to sum all the numbers
        //      If they add up to the goal, this rule is satisfied
        //  If we have a subtraction, we want to subtract all the small numbers from the biggest one
        //      If the result is the goal, this rule is satisfied

        return false;
    }
}