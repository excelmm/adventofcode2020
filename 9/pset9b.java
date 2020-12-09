import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class pset9b {

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
        
        long sumofarr = 0;
        ArrayList<Long> conset = new ArrayList<Long>();
        for (int i = 0; i < input.size(); i++) {
            conset = new ArrayList<Long>();
            for (int j = i + 1; j < input.size(); j++) {
                conset.add(input.get(j));
                sumofarr = conset.stream().mapToLong(Long::longValue).sum();
                if (sumofarr >= number) break;
            }
            if (sumofarr == number) break;
        }
        System.out.println(Collections.max(conset) + Collections.min(conset));
    }

    public static ArrayList<Long> calculate(List<Long> preamble) {

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