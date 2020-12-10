import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class pset5b {

    public static void main(String[] args) throws FileNotFoundException {
        
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        ArrayList<Integer> seats = new ArrayList<Integer>();
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
            seats.add(row * 8 + col);
        }
        sc.close();
        for (int i = 0; i < seats.size() - 1; i++) {
            for (int j = i + 1; j < seats.size(); j++) {
                if (Math.abs(seats.get(i) - seats.get(j)) == 2) {
                    if (!seats.contains((Math.abs(seats.get(i) + seats.get(j)) / 2))) {
                        System.out.println((Math.abs(seats.get(i) + seats.get(j)) / 2));
                        System.exit(0);
                    }
                }
            }
        }
    }

}