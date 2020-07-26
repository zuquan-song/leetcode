package amazon;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

public class Zombie {

    public static void main(String[] args) {
//        int[][] grid = {{1, 1, 1, 1, 1},
//                        {1, 1, 1, 1, 1},
//                        {0, 1, 0, 1, 1},
//                        {1, 1, 1, 0, 1}};
//        int[][] grid = {{0, 1, 1, 0, 1},
//                        {0, 1, 0, 1, 0},
//                        {0, 0, 0, 0, 1},
//                        {0, 1, 0, 0, 0}};
        int[][] grid = {{0, 1, 0, 0, 0},
                        {0, 0, 0, 1, 0},
                        {0, 0, 0, 0, 0},
                        {0, 1, 0, 0, 0}};
        System.out.println(infect(grid));

    }

    public static int infect(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        Queue<Integer> que = new ArrayDeque<>();
        int counter = 0;
        int full = m * n;

        for (int i = 0; i < grid.length; i ++) {
            for (int j = 0; j < grid[0].length; j ++) {
                if (grid[i][j] == 1) {
                    que.offer(i * n + j);
                    counter ++;
                }
            }
        }
        for (int[] arr: grid) {
            System.out.println(Arrays.toString(arr));
        }
        System.out.println();
        int step = 0;
        while (counter < full && step < Math.max(m, n)) {
            Queue<Integer> tmp = new ArrayDeque<>();
            step ++;
            while (!que.isEmpty()) {
                int idx = que.poll();
                int x = idx / n, y = idx % n;
                counter ++;
                if (x > 0 && grid[x - 1][y] == 0)       {tmp.offer((x - 1) * n + y); grid[x - 1][y] = 1;}
                if (x < m - 1 && grid[x + 1][y] == 0)   {tmp.offer((x + 1) * n + y); grid[x + 1][y] = 1;}
                if (y > 0 && grid[x][y - 1] == 0)       {tmp.offer(x * n + (y - 1)); grid[x][y - 1] = 1;}
                if (y < n - 1 && grid[x][y + 1] == 0)   {tmp.offer(x * n + (y + 1)); grid[x][y + 1] = 1;}
            }
            for (int[] arr: grid) {
                System.out.println(Arrays.toString(arr));
            }
            System.out.println();
            que = tmp;
        }
        return step;
    }
}
