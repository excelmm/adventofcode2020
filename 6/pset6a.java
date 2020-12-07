import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class pset6a {

    public static void main(String[] args) throws FileNotFoundException {
        
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        ArrayList<ArrayList<String>> inputs = new ArrayList<ArrayList<String>>();
        ArrayList<String> temp = new ArrayList<String>();

        while (sc.hasNext()) {
            String next = sc.nextLine();
            if (next.isBlank()) {
                inputs.add((ArrayList)temp.clone());
                temp.clear();
                continue;
            }
            temp.add(new String(next));
        }
        sc.close();
        System.out.println(inputs);

        System.out.println(compute(inputs));

    }
    
    public static int compute(ArrayList<ArrayList<String>> inputs) {
        
        int count = 0;
        int questions = new int[26];
        
        for (i = 0; i < inputs.size(); i++) {
            ArrayList<String> subArrayList = inputs.get(i);
            Arrays.fill(questions, 0);
            for (int j = 0; j < subArrayList.size(); j++) {
                for (int k = 0; k < subArrayList.get(j).size(); k++ ) {
                    int index = Integer.parseInt(subArrayList.get(j).charAt(k));
                }
            }
        }


        return 0;
    }

}
