import java.util.Arrays;

public class Main7 {

    public static void main(String[] args) {
        char[] first = new char[10], second = new char[10], third = new char[10];

        for (int i = 0; i < 10; i++) {
            first[i] = (char) (120 - i);
        }
        for (int i = 0; i < 10; i++) {
            second[i] = (char) (110 + i);
        }
        for (int i = 0; i < 10; i++) {
            third[i] = 0;
        }

        System.out.println("First array: " + Arrays.toString(first));
        System.out.println("Second array: " + Arrays.toString(second));
        System.out.println("Third array: " + Arrays.toString(third));

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (first[i] == second[j]) {
                    third[i] = first[i];
                }
            }
        }

        System.out.println("New third array: " + Arrays.toString(third));

        int count = 0;

        for (int i = 0; i < 10; i++) {
            if (third[i] > 0 && third[i] < 115) {
                count++;
            }
        }

        System.out.println("Count: " + count);
    }
}
