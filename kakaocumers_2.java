import java.util.*;

class kakaocumers_2{
    public static int Solution(int[][] needs, int r){
        int answer = 0;
        ArrayList array = new ArrayList<>();
        for (int index=0; index < needs[0].length; index ++ ){
            array.add(new ArrayList<>());
        }

        for( int index=0; index < needs.length; index ++ ){
            for( int part = 0; part < needs[0].length; part ++ ){
                ArrayList temp = (ArrayList) array.get(part);
                temp.add(index);
                array.set(part, temp);
            }
        }

        ArrayList choose = new ArrayList<>();
        

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