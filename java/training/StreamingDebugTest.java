package training;

import java.util.List;

import static java.util.stream.Collectors.toList;

public class StreamingDebugTest {

    public static void main(String[] args) {
        List<PersonModel> data = PersonModel.getData();

        //peek打印出遍历的每个per
        data.stream().map(per->per.getName()).peek(p->{
            System.out.println(p);
        }).collect(toList());
    }
}
