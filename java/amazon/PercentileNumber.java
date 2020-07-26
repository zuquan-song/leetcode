package amazon;

import java.util.List;
import java.util.Random;

public class PercentileNumber<T extends Comparable> {
     public T getPercentileNumber(List<T> numbers, float percentile) {
        int n = numbers.size();
        topK(numbers, 0, n - 1, (int) (n * percentile));
        return numbers.get((int) (n * percentile));
     }

    private void topK(List<T> numbers, int lo, int hi, int k) {
        int idx = lo + new Random().nextInt(hi - lo);
        T tmp = numbers.get(idx);
        numbers.set(idx, numbers.get(hi));
        numbers.set(hi, tmp);


    }
}
