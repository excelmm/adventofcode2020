import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class pset9a {

    public static void main(String[] args) throws FileNotFoundException {

        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        ArrayList<Long> input = new ArrayList<Long>();
        while (sc.hasNext()) {
            input.add(Long.parseLong(sc.nextLine()));
        }
        ArrayList<Long> preamble = calculate(input.subList(0, 25));
        long number = 0;
        for (int i = 25; i < input.size();  i++) {
            if (!preamble.contains(input.get(i))) {
                number = input.get(i);
                break;
            }
            preamble = calculate(input.subList(i - 24, i + 1));
        }
        sc.close();
        System.out.println(number);
    }

    public static ArrayList<Long> calculate (List<Long> preamble) {

        ArrayList<Long> result = new ArrayList<Long>();
        for (int i = 0; i < preamble.size() - 1; i++) {
            for (int j = 0; j < preamble.size(); j++) {
                if (!preamble.contains(preamble.get(i) + preamble.get(j))) {
                    result.add(preamble.get(i) + preamble.get(j));
                }
            }
        }
        return result;

    }

}