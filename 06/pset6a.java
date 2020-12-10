import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;

public class pset6a {

    public static void main(String[] args) throws FileNotFoundException {
        
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        int count = 0;
        int[] questions = new int[26];
        Arrays.fill(questions, 0);
        while (sc.hasNext()) {
            String next = sc.nextLine();
            if (next.isBlank()) {
                for (int j: questions) 
                    count += j;
                Arrays.fill(questions, 0);
                continue;
            }
            for (int i = 0; i < next.length(); i++) {
                int nextchar = next.charAt(i);
                questions[nextchar - 97] = 1;
            }
        }

        // Last group
        for (int j: questions) 
            count += j;
        sc.close();
        System.out.println(count);

    }

}
