package Backtracking;

/**
 * This class is used to represent a coordinate in a grid.
 * Simply put, it's just two numbers
 */
public class Coordinate {

    private int row;
    private int col;

    public Coordinate(int row, int col) {
        this.row = row;
        this.col = col;
    }

    public int getRow() {
        return row;
    }

    public int getCol() {
        return col;
    }
}
