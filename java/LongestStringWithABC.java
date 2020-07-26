
import java.util.PriorityQueue;

public class LongestStringWithABC {
    public String solution(int A, int B, int C) {
        PriorityQueue<int[]> q = new PriorityQueue<>((a, b) -> (b[1] - a[1]));
        StringBuilder sb = new StringBuilder();
        int[] count = new int[3];
        count[0] = A;
        count[1] = B;
        count[2] = C;
        for (int i = 0; i < 3; i ++) {
            if (count[i] > 0) {
                q.offer(new int[]{i, count[i]});
            }
        }

        while (!q.isEmpty()) {
            int[] first = q.poll();
            if (q.isEmpty()) {
                char c = (char) ('a' + first[0]);
                if (first[1] >= 2) {
                    sb.append(c);
                }
                sb.append(c);
                return sb.toString();
            }
            int[] second = q.poll();
            while (first[1] >= 2 && second[1] >= 1) {
                sb.append((char) ('a' + first[0]));
                sb.append((char) ('a' + first[0]));
                first[1] -= 2;
                sb.append((char) ('a' + second[0]));
                second[1] -= 1;
            }

            if (first[1] >= 1 && second[1] >= 1) {
                sb.append((char) ('a' + first[0]));
                first[1] -= 1;
                sb.append((char) ('a' + second[1]));
            }

            if (first[1] > 0) {
                q.offer(first);
            } else {
                q.offer(second);
            }
        }


        return sb.toString();
    }

    public static void main(String[] args) {
        LongestStringWithABC lsabc = new LongestStringWithABC();
        String result = lsabc.solution(6,2,2);
        System.out.println(result);
        result = lsabc.solution(16, 2,2);
        System.out.println(result);
        result = lsabc.solution(16, 19,2);
        System.out.println(result);
    }
}
