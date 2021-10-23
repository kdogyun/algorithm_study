import java.util.HashMap;

class kakaocumers_1{
    public static int Solution(int[] gift_cards, int[] wants){
        int answer = 0;
        HashMap<Integer, Integer> map1 = new HashMap<Integer, Integer>();
        for( int item : wants ){
            map1.put(item, map1.getOrDefault(item, 0) + 1);
        }
        for (int item : gift_cards){
            map1.put(item, map1.getOrDefault(item, 0) - 1);
        }

        for(int item : map1.values()){
            if (item > 0) answer += item;
        }

        return answer;
    }

    public static void main(String[] args) {
        // int[] a = {4, 5, 3, 2, 1};
        // int[] b = {2, 4, 4, 5, 1};
        int[] a = {5, 4, 5, 4, 5};
        int[] b = {1, 2, 3, 5, 4};
        System.out.println(Solution(a, b));
    }
}