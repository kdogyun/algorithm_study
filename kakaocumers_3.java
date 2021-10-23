import java.util.*;

class kakaocumers_3{
    public static int[] solution(int n, int[] passenger, int[][] train) {
        
        Graph g = new Graph(n);
        for(int[] path:train){
            int from = path[0];
            int to = path[1];
            g.input(from, to, -1*passenger[to-1]);
        }
        int[] answer = g.dijkstra(1);
        answer[1] += passenger[0];

        System.out.println(answer[0]);
        System.out.println(answer[1]);

        return answer;
    }

    public static void main(String[] args) {
        int n = 4;
        int[] passenger = {2,1,2,2};
        int[][] train = {{1,2},{1,3},{2,4}};
        System.out.println(solution(n, passenger, train).toString());
    }
}

class Graph{
    private int n;           //노드들의 수
    private int maps[][];    //노드들간의 가중치 저장할 변수
 
    public Graph(int n){
        this.n = n;
        maps = new int[n+1][n+1];
         
    }
    public void input(int i,int j,int w){
        maps[i][j] = w;
        maps[j][i] = w;
    }
 
    public int[] dijkstra(int v){
        int distance[] = new int[n+1];          //최단 거리를 저장할 변수
        boolean[] check = new boolean[n+1];     //해당 노드를 방문했는지 체크할 변수
         
        //distance값 초기화.
        for(int i=1;i<n+1;i++){
            distance[i] = Integer.MAX_VALUE;
        }
         
        //시작노드값 초기화.
        distance[v] =0;
        check[v] =true;
         
        //연결노드 distance갱신
        for(int i=1;i<n+1;i++){
            if(!check[i] && maps[v][i] !=0){
                distance[i] = maps[v][i];
            }
        }
         
         
        for(int a=0;a<n-1;a++){
            //원래는 모든 노드가 true될때까지 인데
            //노드가 n개 있을 때 다익스트라를 위해서 반복수는 n-1번이면 된다.
            //원하지 않으면 각각의 노드가 모두 true인지 확인하는 식으로 구현해도 된다.
            int min=Integer.MAX_VALUE;
            int min_index=-1;
             
            //최소값 찾기
            for(int i=1;i<n+1;i++){
                if(!check[i] && distance[i]!=Integer.MAX_VALUE){
                    if(distance[i]<min ){
                        min=distance[i];
                        min_index = i;
                    }
                }
            }
             
            check[min_index] = true;
            for(int i=1;i<n+1;i++){
                if(!check[i] && maps[min_index][i]!=0){
                    if(distance[i]>distance[min_index]+maps[min_index][i]){
                        distance[i] = distance[min_index]+maps[min_index][i];
                    }
                }
            }
 
        }
         
        //결과값 출력
        for(int i=1;i<n+1;i++){
            System.out.print(distance[i]+" ");
        }
        System.out.println("");

        int index = n;
        int min = distance[index];

        for (int i = n; n>=0; n--){
            if (distance[index] < min){
                min = distance[index];
                index = i;
            }
        }
        int[] result = {index, Math.abs(min)};

        

        return result; 
         
    }
}