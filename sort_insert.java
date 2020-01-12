public class sort_insert {

    //바로 옆(짝꿍)과 비교하는 정렬
    static int array[] = {1, 13, 2, 6, 34, 8, 5, 3, 9, 20};

    public static void main(String[] args) {

        for (int i=0; i<array.length -1; i++){
            int j=i;
            while(array[j] > array[j+1]){
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
                j--;
            }
        }
        
        for(int i : array) System.out.print(i + " ");
    }
}

// O(N*N)
// 필요할때만 자리를 바꾸기에 O(N*N) 중에선 퍼포먼스가 가장 좋음