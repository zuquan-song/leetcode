package amazon;

import java.util.*;

public class KClosePoints {
    public int[][] kClosest(int[][] points, int K) {
        this.helper(points, 0, points.length - 1, K);
        return Arrays.copyOfRange(points, 0, K);
    }

    private void helper(int[][] points, int l, int r, int k) {
        int[] pivot = points[r];
        int i = l;
        int j = l;
        while (j < r) {
            if (pivot[0] * pivot[0] + pivot[1] * pivot[1] > points[j][0] * points[j][0] + points[j][1] * points[j][1]) {
                int[] tmp = points[i];
                points[i] = points[j];
                points[j] = tmp;
                i ++;
            }
            j ++;
        }
        int[] tmp = points[r];
        points[r] = points[i];
        points[i] = tmp;
        if (i + 1 > k) {
            helper(points, l, i - 1, k);
        } else if (i + 1 < k) {
            helper(points, i + 1, r, k);
        }
        List<Character> list;
        Map<String, Integer> map = new HashMap<>();
        for (Map.Entry<String, Integer> entry: map.entrySet()) {
            entry.getValue();
            entry.getKey();
        }

        System.out.println();

        List<Integer> arrayList = new ArrayList<>();


    }
}
