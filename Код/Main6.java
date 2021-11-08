public class Main6 {

    public static void main(String[] args) {
        System.out.println(getSum(2, 2, 1, 6));
    }

    private static int getSum(int last, int q, int count, int max) {
        return last + (count < max ? getSum(last * q, q, count + 1, max) : 0);
    }
}
