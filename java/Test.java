import java.util.*;

public class MaxFinder

class Color<T extends Number> {
    private final Collection<T> collection;

    public Color(Collection<T> collection) {
        this.collection = collection;
    }

    public void add(Collection<T> ele) {
        this.collection.addAll(ele);
    }

    public void add(T ele) {
        this.collection.add(ele);
    }

    public Number max() {
        Iterator iter = this.collection.iterator();
        Number maxVal = null;

        while (iter.hasNext()) {
            if (maxVal == null) {
                maxVal = (Number) iter.next();
            } else {
                Number ele = (Number) iter.next();
                if (ele instanceof Integer && ele.intValue() > maxVal.intValue()) {
                    maxVal = ele;
                } else if (ele instanceof Float && ele.floatValue() > maxVal.floatValue()) {
                    maxVal = ele;
                } else if (ele instanceof Double && ele.doubleValue() > maxVal.doubleValue()) {
                    maxVal = ele;
                } else if (ele instanceof Long && ele.longValue() > maxVal.longValue()) {
                    maxVal = ele;
                }
            }
        }
        return maxVal;
    }

}

public class Test  {

    public static void main(String args[])  {
        List<int[]> list = new ArrayList<>();
        list.add(new int[4]);
        list.add(new int[3]);
        list.add(new int[6]);

        int[] ele = list.get(2);
        Integer a = ele[1];
        System.out.println(a);
    }

}

