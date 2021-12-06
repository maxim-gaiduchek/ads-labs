import java.util.Random;
import java.util.Scanner;

public class Main9 {

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        int[][] matrix = new int[n][n];
        int counter = 0;

        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = counter++;
                }
            } else {
                for (int j = n - 1; j >= 0; j--) {
                    matrix[i][j] = counter++;
                }
            }
        }

        System.out.println("Input matrix:");
        printMatrix(matrix);

        int sum = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                sum += matrix[i][j];
            }
        }

        System.out.println("Sum of elements under main diagonal: " + sum);
    }

    private static void printMatrix(int[][] matrix) {
        for (int[] arr : matrix) {
            for (int i : arr) {
                System.out.print(i + "\t");
            }
            System.out.println();
        }
        System.out.println();
    }
}
