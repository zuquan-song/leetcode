package training;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;
import static java.util.stream.Collectors.toSet;



public class StreamingTest {

    public void filterSex(List<PersonModel> data) {
        List<PersonModel> collect = data.stream()
                .filter(person -> "男".equals(person.getSex())).collect(toList());
        System.out.println(collect);
    }

    public void filterSexAndAge(List<PersonModel> data) {
        List<PersonModel> collect = data.stream().filter(person -> ("男".equals(person.getSex()) && person.getAge() < 20)).collect(toList());
        System.out.println(collect);
    }

    public void getUserNameList(List<PersonModel> data) {
        List<String> collect = data.stream().map(PersonModel::getName).collect(toList());
        System.out.println(collect);
    }

    public void flatMapString(List<PersonModel> data) {
        List<String> collect = data.stream().flatMap(person -> Arrays.stream(person.getName().split(" "))).collect(toList());
        List<Stream<String>> collect1 = data.stream().map(person -> Arrays.stream(person.getName().split(" "))).collect(toList());
        System.out.println(collect);
    }

    public void reduceTest() {
        Integer reduce = Stream.of(1, 2, 3, 4).reduce(10, (count, item) -> count + item);
        System.out.println(reduce);

        String reduce2 = Stream.of("1", "2", "3", "4").reduce("0", (x, y) -> x + "," + y);
        System.out.println(reduce2);
    }

    public void toListTest(List<PersonModel> data) {
        List<String> collect = data.stream().map(PersonModel::getName).collect(Collectors.toList());
        System.out.println(collect);
    }

    public void toMapTest(List<PersonModel> data) {
        Map<String, Integer> collect = data.stream().collect(Collectors.toMap(PersonModel::getName, PersonModel::getAge));
        System.out.println(collect);
    }

    public void toSetTest(List<PersonModel> data) {
        Set<String> collect = data.stream().map(PersonModel::getName).collect(toSet());
        System.out.println(collect);
    }

    /**
     * Custom type
     */
    public void toTreeSetTest(List<PersonModel> data) {
        TreeSet<PersonModel> collect = data.stream().collect(Collectors.toCollection(TreeSet::new));
        TreeSet<PersonModel> collect1 = new TreeSet<>(Comparator.comparing(PersonModel::getName));
        System.out.println(collect);
    }

    public void toGroupTest(List<PersonModel> data) {
        Map<Boolean, List<PersonModel>> collect = data.stream().collect(Collectors.groupingBy(person -> "男".equals(person.getSex())));
        System.out.println(collect);
        Map<String, List<PersonModel>> collect1 = data.stream().collect(Collectors.groupingBy(person -> person.getSex()));
        System.out.println(collect1);
    }

    public void toJoiningTest(List<PersonModel> data) {
        String collect = data.stream().map(PersonModel::getName).collect(Collectors.joining(",", "{", "}"));
        System.out.println(collect);
    }

    public void reduce(){
        List<String> collect = Stream.of("1", "2", "3").map(x -> Arrays.asList(x)).reduce(new ArrayList<>(), (y, z) -> {
            y.addAll(z);
            return y;
        });
        System.out.println(collect);
    }

    public static void main(String[] args) {

        List<PersonModel> data = PersonModel.getData();

        StreamingTest test = new StreamingTest();

//        test.filterSex(data);
//        test.filterSexAndAge(data);
//        test.getUserNameList(data);
//        test.flatMapString(data);
//        test.reduceTest();
        test.toListTest(data);
        test.toMapTest(data);
        test.toSetTest(data);
        test.toGroupTest(data);
        test.toJoiningTest(data);
        test.reduce();

        ArrayList<int[]> embededList = new ArrayList<>();
        Object[] val = embededList.toArray();
        int[][] transferVal = new int[val.length][((int[]) val[0]).length];
        for (int i = 0; i < transferVal.length; i ++) {
            transferVal[i] = ((int[]) val[i]);
        }
        Integer a = new Integer(2);
    }

}
