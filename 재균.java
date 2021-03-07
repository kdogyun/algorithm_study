public class 재균 {

    public static void main(String[] args) {
        String a = "codecopecoxe";
        int count = 0;
        for (int i=0; i<a.length()-3; i++){
            if (a.charAt(i) == 'c'){
                if (a.charAt(i+1) == 'o'){
                    if (a.charAt(i+3) == 'e'){
                        count ++;
                        i += 3;
                    }
                }
            }
        }
        System.out.println(count
        );
    }
}