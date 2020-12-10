import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class pset4b {
    
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
                String pattern = "(\\w{3}):(.*)";
                Pattern r = Pattern.compile(pattern);
                Matcher m = r.matcher(word);
                m.find();
                String first = m.group(1), second = m.group(2);
                if (first.equals("byr")) { 
                    if (Math.abs(1961 - Integer.parseInt(second)) <= 41) count++;
                } else if (first.equals("iyr")) {
                    if (Math.abs(2015 - Integer.parseInt(second)) <= 5) count++;
                } else if (first.equals("eyr")) {
                    if (Math.abs(2025 - Integer.parseInt(second)) <= 5) count++;
                } else if (first.equals("hgt")) {
                    if (second.substring(second.length() - 2, second.length()).equals("cm")) {
                        int height = Integer.parseInt(second.substring(0, second.length() - 2));
                        if (height >= 150 && height <= 193) count++;
                    } else if (second.substring(second.length() - 2, second.length()).equals("in")) {
                        int height = Integer.parseInt(second.substring(0, second.length() - 2));
                        if (height >= 59 && height <= 76) count++;
                    }
                } else if (first.equals("hcl")) {
                    if (second.matches("#[0-9a-f]{6}$")) count++;
                } else if (first.equals("ecl")) {
                    if (second.equals("amb") || second.equals("blu") || second.equals("brn") || second.equals("gry") || 
                    second.equals("grn") || second.equals("hzl") || second.equals("oth")) count++;
                } else if (first.equals("pid")) {
                    if (second.matches("^\\d{9}$")) count++;
                }
                if (count == 7){
                    finalCount++;
                    count = 0;
                }
            }
        }
        sc.close();
        System.out.println(finalCount);
    }

}
