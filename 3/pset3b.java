import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class pset3b {

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        char [][] map = new char [323][31];
        for(int i=0; i < 323; i++){
            String currentstr = sc.nextLine();
            for(int j=0; j < 31; j++){
                char chartoinput = currentstr.charAt(j);
                map[i][j] = chartoinput;
            }
        }
        sc.close();
        System.out.println(countTrees(map, 1, 1) * countTrees(map, 1, 3) * countTrees(map, 1, 5) * countTrees(map, 1, 7) * countTrees(map, 2, 1));
    }
    
    public static long countTrees(char [][] map, int rowinc, int colinc){
        long count = 0;
        int col = 0 ;
        int row = 0;
        while(row < 323) {
            if (map[row][col] == '#') {
                count++;
            }
            row += rowinc;
            col += colinc;
            if (col >= 31)
                col -= 31;
            if (row > 323)
                break;
        }
        System.out.println(count);
        return count;
    }
    
}
