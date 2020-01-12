public class sort_select {

    //하나씩 비교하는 정렬
    static int array[] = {1, 13, 2, 6, 34, 8, 5, 3, 9, 20};

    public static void main(String[] args) {

        
        for( int i=0; i < array.length; i++){
            int index = i;
            // 내림차순 정렬
            //for(int j=i; j > array.length; j++)
            // 오름차순 정렬
            for(int j=i; j < array.length; j++){
                if( array[index] > array[j] ){
                    index = j;
                }
            }
            int temp = array[i];
            array[i] = array[index];
            array[index] = temp;
        }

        for (int i : array) System.out.print(i + " ");
    }
}

// O(N*N)