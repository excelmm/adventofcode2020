import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class pset4a {
    
    public static void main(String[] args) throws FileNotFoundException {
        
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        int count = 0, finalCount = 0;
        while(sc.hasNext()) {
            String nextline = sc.nextLine();
            if (nextline.isEmpty()) {
                count = 0;
                continue;
            }
            String[] words = nextline.split(" ");
            for (String word: words) {
                if (finalCount > 245) {
                }
                String pattern = "(\\w{3}):(.*)";
                Pattern r = Pattern.compile(pattern);
                Matcher m = r.matcher(word);
                m.find();
                if (m.group(1).equals("byr") || m.group(1).equals("iyr") || m.group(1).equals("eyr") || m.group(1).equals("hgt") || 
                m.group(1).equals("hcl") || m.group(1).equals("ecl") || m.group(1).equals("pid")) {
                    count++;
                    if (count == 7) finalCount++;
                }
            }
        }
        sc.close();
        System.out.println(finalCount);
    }

}
