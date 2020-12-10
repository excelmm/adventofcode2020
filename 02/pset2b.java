import java.io.*;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class pset2b {

    public static void main(String[] args) throws FileNotFoundException {
        
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        int finalCount = 0;
        while (sc.hasNext()) {
            String line = sc.nextLine();
            String pattern = "(\\d+)-(\\d+)\\s(\\w):\\s(.*)";
            Pattern r = Pattern.compile(pattern);
            Matcher m = r.matcher(line);
            m.find();

            // Parse inputs
            int min = Integer.parseInt(m.group(1)) - 1;
            int max = Integer.parseInt(m.group(2)) - 1;
            char requiredChar = m.group(3).charAt(0);
            String text = m.group(4);

            // See if it meets requirements
            if (text.charAt(min) == requiredChar && text.charAt(max) != requiredChar ||
            text.charAt(min) != requiredChar && text.charAt(max) == requiredChar) {
                finalCount++;
            }
        }
        sc.close();
        System.out.println(finalCount);

    }

}