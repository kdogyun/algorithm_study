import java.util.*;
import java.io.*;

public class namedNumberOfHouse_2667 {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine().strip());
        String map[][] = new String[n][n];
        ArrayList<Integer> houses = new ArrayList<>();
        for(int i=0; i<n; i++){
            int j=0;
            for(String s: input.readLine().strip().split("")){
                map[i][j] = s;
                j++;
            }
        }

        Deque<Node> q = new LinkedList<>();
        q.offer(find(map));
        map[q.peek().x][q.peek().y] = "0";
        int count = 1;
        while (true) {
            Node point = q.poll();
            if (point == null) break;

            if ( point.x+1 >= 0 && point.x+1 < n && map[point.x+1][point.y].equals("1")){
                count ++;
                map[point.x+1][point.y] = "0";
                q.offer(new Node(point.x+1, point.y));}
            if ( point.x-1 >= 0 && point.x-1 < n && map[point.x-1][point.y].equals("1")){
                count ++;
                map[point.x-1][point.y] = "0";
                q.offer(new Node(point.x-1, point.y)); }
            if ( point.y+1 >= 0 && point.y+1 < n && map[point.x][point.y+1].equals("1")){
                count ++;
                map[point.x][point.y+1] = "0";
                q.offer(new Node(point.x, point.y+1)); }
            if ( point.y-1 >= 0 && point.y-1 < n && map[point.x][point.y-1].equals("1")){
                count ++;
                map[point.x][point.y-1] = "0";
                q.offer(new Node(point.x, point.y-1)); }

            if (q.isEmpty()){
                houses.add(count);
                q.offer(find(map));
                if (q.peek() == null) break;
                count = 1;
                map[q.peek().x][q.peek().y] = "0";
            }
        }

        System.out.println(houses.size());
        Collections.sort(houses);
        for(int i: houses) System.out.println(i);

    }

    public static Node find(String[][] map){
        Node node = null;
        for(int i=0; i<map.length; i++){
            for(int j=0;  j<map[0].length; j++){
                if (map[i][j].equals("1")){
                    node = new Node(i, j);
                    break;
                }
            }
        }
        return node;
    }
}

class Node{
    int x, y;
    public Node(int _x, int _y){
        this.x = _x;
        this.y = _y;
    }
}
