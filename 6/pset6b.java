import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;

public class pset6b {

    public static void main(String[] args) throws FileNotFoundException {
        
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        int count = 0;
        boolean first = true;
        int[] questions = new int[26];
        Arrays.fill(questions, 0);
        while (sc.hasNext()) {
            String next = sc.nextLine();
            if (next.isBlank()) {
                for (int j: questions) 
                    count += j;
                Arrays.fill(questions, 0);
                first = true;
                continue;
            }
            if (first) {
                for (int i = 0; i < next.length(); i++) {
                    int nextchar = next.charAt(i);
                    questions[nextchar - 97] = 1;
                }
                first = false;
            } else {
                for (int i = 0; i < questions.length; i++) {
                    boolean found = false;
                    if (questions[i] == 0) continue;
                    for (int j = 0; j < next.length(); j++ ) {
                        int nextchar = next.charAt(j);
                        if (i == nextchar - 97) {
                            found = true;
                            break;
                        }
                    }
                    if (!found) questions[i] = 0;
                }
            }
        }

        // Last group
        for (int j: questions) 
            count += j;
        sc.close();
        System.out.println(count);

    }

}
