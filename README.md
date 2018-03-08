- run:
```bash
git clone https://github.com/2XL/junit-daemon && cd junit-daemon
make all
```

- output:
```bash

└─ $ ▶ make all
Available tasks:

  build    Provision the project with the provided payload
  clean    Cleans up generated files, clean all files in source
  export   Generate fixture yml from src and tests
  report   Generate json reports from execution stdout

java -cp out:tests:libs/junit-4.12.jar:libs/hamcrest-core-1.3.jar org.junit.runner.JUnitCore PersonTest
JUnit version 4.12
.
Time: 0.003

OK (1 test)
```
```json
[
  {
    "err_run_test": []
  }, 
  {
    "out_compile_test": []
  }, 
  {
    "err_compile_source": []
  }, 
  {
    "out_compile_source": []
  }, 
  {
    "out_run_test": {
      "test_framework": "JUnit version 4.12", 
      "test_status": "OK", 
      "test_summary": "1 test", 
      "test_time": "0.003"
    }
  }, 
  {
    "err_compile_test": []
  }
]
```
 - [HOW_TO_CREATE_FIXTURE.md](https://github.com/2XL/junit-daemon/blob/master/fixture/README.md)

 - [TODO.md](https://github.com/2XL/junit-daemon/blob/master/TODO.md)