- run:
```bash
git clone https://github.com/2XL/junit-daemon && cd junit-daemon
make all
```

- output:
```bash
x@x ~/Github/2XL/junit-daemon (master)
└─ $ ▶ time make all
Available tasks:

  build   Provision the project with the provided payload
  clean   Cleans up generated files, clean all files in source


%%CREATE%%src/Person.java%%
public class Person {
  String name;

  public Person(String personName) {
          name = personName;
  }

  public String greet(String yourName) {
          return String.format("Konbanwa!  My name is %s.  It is nice to meet you, %s!", this.name, yourName);
  }
}
%%END


%%CREATE%%tests/PersonTest.java%%
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;


public class PersonTest {
  @Test
  public void testGreet() {
    Person shoki = new Person("Shoki, the Demon Queller");
    assertEquals("Konbanwa!  My name is Shoki, the Demon Queller.  It is nice to meet you, Sun Wukong, the Monkey King!", shoki.greet("Sun Wukong, the Monkey King"));
  }
}
%%END

java -cp out:tests:libs/junit-4.12.jar:libs/hamcrest-core-1.3.jar org.junit.runner.JUnitCore PersonTest
JUnit version 4.12
.
Time: 0.003

OK (1 test)


real	0m1.063s
user	0m1.720s
sys	0m0.124s
x@x ~/Github/2XL/junit-daemon (master)
└─ $ ▶

```
 - [HOW_TO_CREATE_FIXTURE.md](https://github.com/2XL/junit-daemon/blob/master/fixture/README.md)

 - [TODO.md](https://github.com/2XL/junit-daemon/blob/master/TODO.md)