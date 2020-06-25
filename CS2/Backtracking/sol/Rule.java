package Backtracking.sol;

import java.util.ArrayList;
import java.util.Collections;

/**
 * This class represents one of the rules or regions in a KenKen puzzle
 * Created by Yancarlos Diaz, yxd3549, for the Academic Success Center Supplemental Instruction Program.
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

        for (Coordinate cell : cells) {
            numbers.add(board[cell.getRow()][cell.getCol()]);
        }

        // This line sorts the array in descending order so that the subtraction
        // works properly
        Collections.sort(numbers, Collections.reverseOrder());

        int total = numbers.get(0);
        if (operation == (Operation.SUBTRACTION)) {
            for (int i = 1; i < numbers.size(); i++) {
                total -= numbers.get(i);
            }
        }
        else if (operation == (Operation.SUM)) {
            for (int i = 1; i < numbers.size(); i++) {
                total += numbers.get(i);
            }
        }

        return total == goal;
    }
}