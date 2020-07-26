import java.util.*;

public class VLA2 implements Comparator<VLA2> {
    int dishSize;

    public static void main(String[] args) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1 - o2 >= 0 ? 1: -1;
            }
        });
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();

        minHeap.offer(5);
        minHeap.offer(4);
        System.out.println(minHeap.poll());
    }

    public int compare(VLA2 a, VLA2 b) {
        return b.dishSize - a.dishSize;
    }

    VLA2(int d) { dishSize = d; }
}

class AA {

}

abstract class BB extends AA {
    class CC {

    }
    public void print() {

    }
}