package training;

import java.util.*;

public class OptionalTest {
    public static void main(String[] args) throws Exception {
        PersonModel person = new PersonModel();

        Optional<Object> o = Optional.of(person);
        System.out.println(o.orElse("-"));

        Optional<String> name = Optional.ofNullable(person.getName());
        System.out.println(name.orElse("-"));

        Optional.ofNullable("test").ifPresent(na -> {
            System.out.println(na + " ifPresent");
        });

        System.out.println(Optional.ofNullable("1").orElseThrow(()-> new RuntimeException("ss")));
    }

}
