package training;

import java.util.function.Consumer;
import java.util.function.Function;

public class LambdaTest {

    public static void main(String[] args) {
        Function<String, Integer> function = (String value) ->  5;
        System.out.println(function.apply("zu quan"));
        invokeMethod(function, "zuquan");
        Consumer<String> function2 = (String name) -> System.out.println(name);
        function2.accept("zuquan");
    }

    private static void invokeMethod(Function<String, Integer> function, String zuquan) {

    }
}
