package netflix;

import java.util.*;

public class SolutionFirst {

    public String solution(String name, String surname, int age) {
        return name.substring(0, 2) + surname.substring(0, 2) + String.valueOf(age);
    }

    public int solution2(int[] A) {
        int resZero = 0;
        int resOne = 0;
        for (int i = 0; i < A.length; i ++) {
            if (A[i] == i % 2) {
                resOne ++;
            }
            if (A[i] != i % 2) {
                resZero ++;
            }
        }
        return Math.min(resZero, resOne);
    }

    public static void main(String[] args) {
//        Map<String, Object> map = new TreeMap<>();
        Map<String, Object> map = new Hashtable<>();

        map.put("one", "lst");
        map.put("second", new Integer(2));
        map.put("third", "3rd");
        map.put("third", "III");
        Set mySet = map.entrySet();
        System.out.println(mySet);
        List<Integer> list = new ArrayList<>(new ArrayList<>());
    }
}
