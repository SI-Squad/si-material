package Backtracking.sol;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Optional;
import java.util.Scanner;
import java.util.*;

/**
 * This class implements the necessary methods to solve a KenKen puzzle
 * using the Backtracking interface from the CS department.
 */
public class KenKenConfiguration implements Configuration {

    /* A 2d array to represent the board */
    private int[][] board;
    /* The dimensions of the board */
    private int dim;
    /* The set of rules or regions for this board */
    private ArrayList<Rule> rules;
    /* The row of the cell we must fill next */
    private int currentRow;
    /* The column of the cell we must fill next */
    private int currentCol;

    /**
     * Main constructor for a KenKenConfiguration
     * Reads the board and rules from a file and initializes the state
     */
    public KenKenConfiguration(String filename){
        this.currentRow = 0;
        this.currentCol = 0;
        try(Scanner file = new Scanner(new FileReader(filename))){
            dim = file.nextInt();
            board = new int[dim][dim];
            rules = new ArrayList<>();
            file.nextLine();
            while(file.hasNextLine()){
                String[] line = file.nextLine().split(" ");

                String operationString = line[0];
                Operation operation;
                if (operationString.equals("+")){
                    operation = Operation.SUM;
                } else {
                    operation = Operation.SUBTRACTION;
                }

                int goal = Integer.parseInt(line[1]);

                ArrayList<Coordinate> cells = new ArrayList<>();
                for (int i = 2; i < line.length; i++){
                    String[] coordinates = line[i].split(",");
                    Coordinate coordinate = new Coordinate(Integer.parseInt(coordinates[0]), Integer.parseInt(coordinates[1]));
                    cells.add(coordinate);
                }
                Coordinate[] coordinates = new Coordinate[cells.size()];
                cells.toArray(coordinates);
                Rule rule = new Rule(coordinates, goal, operation);
                rules.add(rule);
            }

        }catch (FileNotFoundException fnfe){
            System.out.println(fnfe.getMessage());
            System.exit(1);
        }
    }

    /**
     * A copy constructor to copy all the state by value and not by reference
     */
    public KenKenConfiguration(KenKenConfiguration kenKenConfiguration){

        if (kenKenConfiguration.currentCol == kenKenConfiguration.dim - 1) {
            this.currentCol = 0;
            this.currentRow = kenKenConfiguration.currentRow + 1;
        }
        else {
            this.currentCol = kenKenConfiguration.currentCol + 1;
            this.currentRow = kenKenConfiguration.currentRow;
        }

        this.board = new int[kenKenConfiguration.dim][kenKenConfiguration.dim];
        for (int row = 0; row < kenKenConfiguration.dim; row++) {
            for (int col = 0; col < kenKenConfiguration.dim; col++) {
                this.board[row][col] = kenKenConfiguration.board[row][col];
            }
        }

        this.rules = kenKenConfiguration.rules;
        this.dim = kenKenConfiguration.dim;

    }

    /**
     * For debugging purposes, the toString returns a string representing
     * the current state of the board
     */
    @Override
    public String toString() {
        String result = "\n";
        for(int i = 0; i < dim; i++){
            for(int j = 0; j < dim; j++){
                result += this.board[i][j];
            }
            result += "\n";
        }
        return result;
    }

    /**
     * Returns a list of all the successors of this configuration
     * TODO: Group A
     */
    @Override
    public Collection<Configuration> getSuccessors() {
        ArrayList<Configuration> successors = new ArrayList<>();

        if (this.currentRow == this.dim) {
            return successors;
        }

        for (int i = 1; i <= this.dim; i++) {
            KenKenConfiguration newConfig = new KenKenConfiguration(this);
            newConfig.board[this.currentRow][this.currentCol] = i;
            successors.add(newConfig);
        }

        return successors;
    }

    /**
     * Returns whether this configuration is valid or not
     * Used for pruning
     * @return
     */
    @Override
    public boolean isValid() {
        for(int i = 0; i < dim; i++){
            TreeSet<Integer> numbers = new TreeSet<>();
            for(int j =0; j < dim; j++){
                int number = this.board[i][j];
                if(number != 0 && numbers.contains(number)){
                    return false;
                }
                numbers.add(number);
            }
        }

        for(int i = 0; i < dim; i++){
            TreeSet<Integer> numbers = new TreeSet<>();
            for(int j =0; j < dim; j++){
                int number = this.board[j][i];
                if(number != 0 && numbers.contains(number)){
                    return false;
                }
                numbers.add(number);
            }
        }

        return true;
    }

    /**
     * Return whether this configuration is a goal
     */
    @Override
    public boolean isGoal() {

        if (currentRow != dim) {
            return false;
        }

        for (Rule rule: rules) {

            if (!(rule.isSatisfied(this.board))) {
                return false;
            }
        }

        return true;
    }

    /**
     * Starts the program and runs the backtracking algorithm
     * @param args
     */
    public static void main(String[] args) {
        KenKenConfiguration configuration = new KenKenConfiguration("5x.txt");
        Backtracker backtracker = new Backtracker(false);
        Optional<Configuration> solution = backtracker.solve(configuration);
        if(solution.isPresent()){
            KenKenConfiguration realSolution = (KenKenConfiguration) solution.get();
            System.out.println(realSolution);
        }
    }
}
