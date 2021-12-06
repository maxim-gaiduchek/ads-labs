import java.util.Random;

public class Main8 {

    public static void main(String[] args) {
        int[][] matrix = createMatrix();

        System.out.println("Input matrix:");
        printMatrix(matrix);

        int[] arr = new int[matrix[0].length];

        for (int j = 0; j < matrix[0].length; j++) {
            int sum = 0;

            for (int i = 0; i < matrix.length; i++) {
                sum += matrix[i][j];
            }

            arr[j] = sum;
        }

        System.out.print("Sum of columns array: ");
        printArray(arr);

        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        System.out.print("Sorted array: ");
        printArray(arr);
    }

    private static int[][] createMatrix() {
        Random random = new Random();
        int[][] matrix = new int[5][7];

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                matrix[i][j] = random.nextInt(10);
            }
        }

        return matrix;
    }

    private static void printArray(int[] arr) {
        for (int i : arr) {
            System.out.print(i + ", ");
        }
        System.out.println();
    }

    private static void printMatrix(int[][] matrix) {
        for (int[] arr : matrix) {
            printArray(arr);
        }
        System.out.println();
    }
}
