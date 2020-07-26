package factual;

import java.util.ArrayList;
import java.util.List;

class TreeNode<T extends Number> {
    private final T val;
    private final List<TreeNode<T>> children;

    public TreeNode(T val) {
        this.val = val;
        this.children = new ArrayList<>();
    }

    public List<TreeNode<T>> getChildren() {
        return this.children;
    }

    public void addChild(T val) {
        this.children.add(new TreeNode<>(val));
    }

    public T getVal() {
        return this.val;
    }
}

interface Reducer<T extends Number> {
    T initVal();
    T reduceMethod(T a, T b);
}

public class TreeReducer <T extends Number, S extends Number> {

    public T reduce(TreeNode<T> root, Reducer<T> reducer) {
        T result = reducer.initVal();
        for (TreeNode node: root.getChildren()) {
            result = reducer.reduceMethod(result, (T) node.getVal());
        }
        return result;
    }

    public static void main(String[] args) {
        TreeReducer reducer = new TreeReducer();
        reducer.reduce(new TreeNode<>(0), new Reducer() {
            @Override
            public Number initVal() {
                return 0;
            }

            @Override
            public Number reduceMethod(Number a, Number b) {
                return a.intValue() + b.intValue();
            }
        });
    }
}

