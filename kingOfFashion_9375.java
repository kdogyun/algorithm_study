import java.io.*;
import java.util.*;

public class kingOfFashion_9375 {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(input.readLine().strip());
        for(int i=0; i<testCase; i++){
            int n = Integer.parseInt(input.readLine().strip());
            HashMap<String, Integer> hash = new HashMap<>();
            for(int j=0; j<n; j++){
                String[] clothes = input.readLine().strip().split(" ");
                hash.put( clothes[1], hash.getOrDefault(clothes[1], 0)+1 );
            }
            int answer = 1;
            for(Map.Entry<String, Integer> entry : hash.entrySet()){
                answer *= entry.getValue() + 1;
            }
            System.out.println(answer-1);
        }
    }    
}
