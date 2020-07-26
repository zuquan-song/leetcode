package training;

import java.util.Arrays;
import java.util.List;

public class PersonModel {
    String name;
    int age;
    String sex;

    public PersonModel(String name, int age, String sex) {
        this.name = name;
        this.age = age;
        this.sex = sex;
    }

    public PersonModel() {

    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getSex() {
        return sex;
    }

    @Override
    public String toString() {
        return String.format("name %s, age %d, sex %s", this.name, this.age, this.sex);
    }

    public static List<PersonModel> getData() {
        PersonModel wu = new PersonModel("wu qi", 18, "男");
        PersonModel zhang = new PersonModel("zhang san", 19, "男");
        PersonModel wang = new PersonModel("wang si", 20, "女");
        PersonModel zhao = new PersonModel("zhao wu", 20, "男");
        PersonModel chen = new PersonModel("chen liu", 21, "男");
        return Arrays.asList(wu, zhang, wang, zhao, chen);
    }
}
