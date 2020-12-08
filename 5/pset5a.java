import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class pset5a {

    public static void main(String[] args) throws FileNotFoundException {
        
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        int max = 0;
        while(sc.hasNext()) {
            int multiplier = 64, row = 0, col = 0;
            String seat = sc.nextLine();
            for (int i = 0; i < 7; i++) {
                row += (seat.charAt(i) == 'B' ? 1 : 0) * multiplier;
                multiplier /= 2;
            }
            multiplier = 4;
            for (int i = 7; i < 10; i++) {
                col += (seat.charAt(i) == 'R' ? 1 : 0) * multiplier;
                multiplier /= 2;
            }
            if (row * 8 + col > max) max = row * 8 + col;
        }
        sc.close();
        System.out.println(max);
    }

}