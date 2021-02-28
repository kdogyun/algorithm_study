import java.io.*;
import java.util.*;

public class aPersonWhoInTheOffice_7785 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, Integer> hash = new HashMap<>();
        int n = Integer.parseInt(input.readLine());

        for(int i=0; i<n; i++){
            String[] log = input.readLine().strip().split(" ");
            if (log[1].equals("enter")) hash.put(log[0], 1);
            else hash.remove(log[0]);
        }
        String answer = "";
        for(String s : hash.keySet()) answer += s + "\n";
        
        System.out.println(answer);
    }
}
