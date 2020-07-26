import java.util.TreeMap;

class Flag {
    public boolean odd;
    public boolean even;
    public Flag() {
        this.odd = true;
        this.even = true;
    }
}

public class OddEvenJump {
    public int oddEvenJumps(int[] A) {
        if (A.length == 1) {
            return 1;
        }
        TreeMap<Integer, Flag> tree = new TreeMap<>();
        tree.put(A[A.length - 1], new Flag());
        int result = 1;
        for (int i = A.length - 2; i >= 0; i --) {
            Integer keyOdd = tree.ceilingKey(A[i]);
            Integer keyEven = tree.floorKey(A[i]);
            Flag flag = new Flag();
            if (keyOdd == null) {
                flag.odd = false;
            } else {
                Flag nextJump = tree.get(keyOdd);
                if (nextJump.even) {
                    // System.out.printf("start i=%d jumpTo nextJump=%d%n", i, nextJump.idx);
                    result ++;
                } else {
                    flag.odd = false;
                }
            }
            if (keyEven == null) {
                flag.even = false;
            } else {
                Flag nextJump = tree.get(keyEven);
                if (nextJump.odd) {
                } else {
                    flag.even = false;
                }
            }
            tree.put(A[i], flag);
        } 
        return result;
    }
}
