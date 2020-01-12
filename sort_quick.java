public class sort_quick {

    //바로 옆(짝꿍)과 비교하는 정렬
    static int array[] = {1, 13, 2, 6, 34, 8, 5, 3, 9, 20};

    public static void main(String[] args) {
        quick(array, 0, array.length-1);
        
        for(int i : array) System.out.print(i + " ");
    }

    public static void quick(int[] data, int start, int end){
        int left = start;
        int right = end;
        int pivot = (start + end) / 2; // 제일 처음꺼 해도 되고, 중간꺼 해도 되고. 맘대로.

        while (left <= right){
            // 부호 반대로 하면 내림차순
            while(data[left] < data[pivot]) left++;
            while(data[right] > data[pivot]) right--;
            if(left <= right){
                int temp = data[left];
                data[left] = data[right];
                data[right] = temp;
                left++;
                right--;
            }
        }
        
        if(start < right) quick(data, start, right);
        if(end > left) quick(data, left, end);
    }
}

// O(N*logN)
// 이미 정렬되어 있으면 최악의 경우. O(N*N)