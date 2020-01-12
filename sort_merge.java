public class sort_merge {

    //바로 옆(짝꿍)과 비교하는 정렬
    static int array[] = {1, 13, 2, 6, 34, 8, 5, 3, 9, 20};

    public static void main(String[] args) {
        
        for(int i : array) System.out.print(i + " ");
    }
}

// O(N*logN) 보장.
