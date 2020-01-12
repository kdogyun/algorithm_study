import java.util.Scanner;

public class search_binary {

    //반씩 잘라서 검색
    static int array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int find = sc.nextInt();

        int start = 0;
        int end = array.length - 1;
        
        int result = -1;

        while (start <= end){
            int mid = (start + end) / 2;
            
            if (find == array[mid]){
                result = mid;
                break;
            }
            else if (find > array[mid]) start = mid + 1;
            else end = mid - 1;
        }

        System.out.println("find index is " + (result+1));

        sc.close();
    }
}

// O(logN)