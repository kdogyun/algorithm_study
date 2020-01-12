public class sort_bubble {

    //바로 옆(짝꿍)과 비교하는 정렬
    static int array[] = {1, 13, 2, 6, 34, 8, 5, 3, 9, 20};

    public static void main(String[] args) {
        for (int i=0; i<array.length; i++){
            for (int j=0; j<array.length -i -1; j++){
                if(array[j]>array[j+1]){
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
        for(int i : array) System.out.print(i + " ");
    }
}

// O(N*N)
// 자리를 계속 바꿈으로 선택정렬보다 느림