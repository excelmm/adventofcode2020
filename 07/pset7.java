import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class pset7 {

    public static void main(String[] args) throws FileNotFoundException {
        
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        Map<String, List<String>> adj_list = new HashMap<String, List<String>>();

        while (sc.hasNext()) {

            // Match
            String input = sc.nextLine();
            Pattern r = Pattern.compile("(\\w+ \\w+) bags contain ([^\\.]*)");
            Matcher m = r.matcher(input);
            m.find();

            // Add bag to list
            String type = m.group(1);
            String contents[] = m.group(2).split(", ");
            List<String> contentsarray = new ArrayList<String>();
            contentsarray = Arrays.asList(contents);
            adj_list.put(type, contentsarray);

        }

        ArrayList<String> visited = new ArrayList<String>();
        ArrayList<String> contains = new ArrayList<String>();        
        
        Iterator<String> iter = adj_list.keySet().iterator();
        for (int i = 0; i < adj_list.keySet().size(); i++) {
            String next = iter.next();
            dfs(visited, next, next, contains, adj_list);
            visited.clear();
        }

        System.out.println(contains.size());
        System.out.println(add(adj_list, "shiny gold"));
        sc.close();
    }

    
    public static void dfs(ArrayList<String> visited, String current, String root, ArrayList<String> containsbag, Map<String, List<String>> adj_list) {

        if (!visited.contains(current)) {
            visited.add(current);
            for (String content: adj_list.get(current)) {
                // System.out.printf("visit %s\n", content);
                if (content.contains("no other")) {
                    return;
                }
                if (content.contains("shiny gold")) {
                    // System.out.println("found");
                    if (!containsbag.contains(root)) {
                        containsbag.add(root);
                    }
                    return;
                }
                Pattern p = Pattern.compile("[a-zA-Z\\s]+\\s*[^bags?]");
                Matcher m = p.matcher(content.substring(2));
                m.find();
                dfs(visited, m.group(0).trim(), root, containsbag, adj_list);
            }
        }
        return;
    }

    public static int add(Map<String, List<String>> adj_list, String current) {
        int count = 0;
        for (String content: adj_list.get(current)) {
            if (content.contains("no other")) {
                return 0;
            }
            int currentcount = Integer.parseInt(content.substring(0, 1));
            Pattern p = Pattern.compile("[a-zA-Z\\s]+\\s*[^bags?]");
            Matcher m = p.matcher(content.substring(2));
            m.find();
            count += currentcount + currentcount * add(adj_list, m.group(0).trim());
        }
        return count;
    }
    
}

class Bag {

    String type;
    List<String> contents = new ArrayList<String>();
    List<String> unnumberedcontents = new ArrayList<String>();

    Bag() {

    }

    Bag(String type, List<String> contents) {
        this.type = type;
        this.contents = contents;
        for (String i: contents) unnumberedcontents.add(i.substring(2));
    }


}