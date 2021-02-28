import java.util.HashMap;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class numberOfCard2_10816 {
    
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, Integer> hash = new HashMap<>();
        String answer = "";

        input.readLine();
        for(String s : input.readLine().strip().split(" "))
            hash.put(s, hash.getOrDefault(s, 0) + 1);

        input.readLine();
        for(String s : input.readLine().strip().split(" "))
            answer += hash.getOrDefault(s, 0) + " ";
            System.out.print(answer);
    }
}
