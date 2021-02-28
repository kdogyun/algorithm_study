import java.io.*;
import java.util.*;

public class pocketmonMaster_1620 {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = input.readLine().strip().split(" ");
        HashMap<String, Integer> nameTonum = new HashMap<>();
        HashMap<Integer, String> numToname = new HashMap<>();
        for(int i=0; i<Integer.parseInt(nm[0]); i++){
            String a = input.readLine().strip();
            nameTonum.put(a, i+1);
            numToname.put(i+1, a);
        }
        String answer = "";
        for(int i=0; i<Integer.parseInt(nm[1]); i++){
            String a = input.readLine().strip();
            try{
                answer += numToname.get(Integer.parseInt(a)) + "\n";
            } catch (Exception e){
                answer += nameTonum.get(a) + "\n";
            }
        }
        System.out.print(answer);
    }
}
