import java.io.*;
import java.util.*;

public class dijkstra {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String[] ll = input.readLine().strip().split(" ");
        int node = Integer.parseInt(ll[0]);
        int line = Integer.parseInt(ll[1]);

        int next = Integer.parseInt(input.readLine());

        int[][] map = new int[node+1][node+1];
        for(int i=0; i<line; i++) {
            String[] info = input.readLine().strip().split(" ");
            int start = Integer.parseInt(info[0]);
            int end = Integer.parseInt(info[1]);
            int cost = Integer.parseInt(info[2]);
            map[start][end] = cost;
            map[end][start] = cost;
        }

        int[] cost = new int[node+1];
        Arrays.fill(cost, Integer.MAX_VALUE);
        boolean[] visited = new boolean[node+1];

        int curr = 0;
        int[] small = {0, Integer.MAX_VALUE}; // 위치, 코스트
        visited[0] = true;
        visited[1] = true;
        cost[1] = 0;
        cost[0] = 0;
        boolean go = true;

        while (go){
            curr = next;
            for(int i=1; i<node+1; i++){
                if(i==curr) continue;
                if(map[curr][i] != (int)0 && !visited[i]){
                    System.out.println("교환점 찾기: "+curr+"to"+i);
                    cost[i] = Math.min( cost[i], cost[curr] + map[curr][i] );
                    if(small[1] >= cost[i]) {small[0] = i; small[1] = cost[i];}
                }
            }
            
            for(int cc : cost) System.out.print(cc+" ");
            System.out.println();

            next = small[0];
            visited[next] = true;
            int cnt = 0;
            System.out.println("끝일까? next = "+next+"/"+curr);
            for(boolean b : visited){
                if(b==true) cnt ++;
            }
            if(cnt==node) go = false;
        }

        for(int cc : cost) System.out.print(cc+" ");
        System.out.println();
    }    
}
