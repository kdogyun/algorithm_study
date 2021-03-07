import java.util.*;
import java.io.*;

public class searchMaze_2178 {
    public static void main(String[] args) throws IOException{
        class Node{
            int x, y, cost;
            public Node(int _x, int _y, int _cost){
                this.x = _x;
                this.y = _y;
                this.cost = _cost;
            }
        }

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = input.readLine().strip().split(" ");
        String[][] maze = new String[Integer.parseInt(nm[0])][Integer.parseInt(nm[1])];
        for(int i=0; i< Integer.parseInt(nm[0]); i++){
            int j=0;
            for(String s: input.readLine().strip().split("")){
                maze[i][j] = s;
                j++;
            }
        }

        int[][] costMap = new int[Integer.parseInt(nm[0])][Integer.parseInt(nm[1])];
        for(int i=0; i<Integer.parseInt(nm[0]); i++){
            for(int j=0; j<Integer.parseInt(nm[1]); j++) costMap[i][j] = Integer.MAX_VALUE;
        }

        int answer = 0;
        Deque<Node> q = new LinkedList<>();
        q.offer(new Node(0, 0, 0));
        costMap[0][0] = 0;

        while (!q.isEmpty()){
            Node point = q.poll();
            if (point.x == Integer.parseInt(nm[0])-1 && point.y == Integer.parseInt(nm[1])-1){
                answer = point.cost;
                break;
            }
            int currCost = costMap[point.x][point.y];
            if ( point.x+1 >= 0 && point.x+1 < Integer.parseInt(nm[0]) && maze[point.x+1][point.y].equals("1") && currCost+1 < costMap[point.x+1][point.y] ){
                costMap[point.x+1][point.y] = point.cost+1;
                q.offer(new Node(point.x+1, point.y, point.cost+1));}
            if ( point.x-1 >= 0 && point.x-1 < Integer.parseInt(nm[0]) && maze[point.x-1][point.y].equals("1") && currCost+1 < costMap[point.x-1][point.y] ){
                costMap[point.x-1][point.y] = point.cost+1;
                q.offer(new Node(point.x-1, point.y, point.cost+1)); }
            if ( point.y+1 >= 0 && point.y+1 < Integer.parseInt(nm[1]) && maze[point.x][point.y+1].equals("1") && currCost+1 < costMap[point.x][point.y+1] ){
                costMap[point.x][point.y+1] = point.cost+1;
                q.offer(new Node(point.x, point.y+1, point.cost+1)); }
            if ( point.y-1 >= 0 && point.y-1 < Integer.parseInt(nm[1]) && maze[point.x][point.y-1].equals("1") && currCost+1 < costMap[point.x][point.y-1] ){
                costMap[point.x][point.y-1] = point.cost+1;
                q.offer(new Node(point.x, point.y-1, point.cost+1)); }
        }

        System.out.println(answer+1);
    }
}
