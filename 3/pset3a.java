import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class pset3a {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("C:\\Users\\Excel PC\\Documents\\GitHub\\excelmm\\adventofcode2020\\3\\pset3.txt");
        Scanner sc = new Scanner(file);
        char [][] map = new char [323][31];
        for(int i=0; i<323; i++){
            String currentstr = sc.nextLine();
            for(int j=0; j<31; j++){
                char chartoinput = currentstr.charAt(j);
                map[i][j] = chartoinput;
            }
        }
        sc.close();

        System.out.println(countTrees(map));
    }
    
    public static int countTrees(char [][] map){
        int count=0;
        int col=0;
        int row=0;
        while(row<323) {
            if (map[row][col] == '#') {
                count++;
            }
            row++;
            col += 3;
            if (col >= 31) {
                col -= 31;
            }
        }
        return count;
    }
}