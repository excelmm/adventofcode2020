import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class pset1b {

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("C:\\Users\\Excel PC\\Documents\\GitHub\\excelmm\\adventofcode2020\\1\\pset1.txt");
        Scanner sc = new Scanner(file);
        ArrayList<Integer> inputs = new ArrayList<Integer>();

        while(sc.hasNextLine()) {
           inputs.add(Integer.parseInt(sc.nextLine()));
        }
        sc.close();

        for (int i = 0; i < inputs.size() - 2; i++) {
            for (int j = i + 1; j < inputs.size() -1; j++) {
                for (int k = j + 1; k < inputs.size(); k++) {
                    if (inputs.get(i) + inputs.get(j) + inputs.get(k)== 2020) { 
                        System.out.printf("%d * %d * %d = %d", inputs.get(i), inputs.get(j), inputs.get(k), inputs.get(i) * inputs.get(j) * inputs.get(k));
                    }
                }
            }
        }
    }

}