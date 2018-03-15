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


# workflow


<PRE>

[service/emulator] [tester/school] [mq]    

                                        state: after starting the dev env `docker-compose up`    
    
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   nameko register subscriber (worker to validate test)
    
                    >>>>>>>>>>>>>>>>>   nameko register publisher (worker to submit test && listen callback)
                                    
                                        event: localmachine run `tester run demo.yml`
                                        
                    <<<<<<<<<<<<<<<<<   codechallenge-submission is dispatch
                    
                                        event: school generate submission token and wait for callback
                
                    >>>>>>>>>>>>>>>>>   codechallenge-validation request to emulator
                    
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   emulator receive code submission from school
    
                                        event: emulator generates the source tree
                                        
                                        event: emulator runs the testsuite
                                        
                                        event: emulator generate reports in json format
                                        
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   emulator response with reports to school
                                        
                                        event: school update the submission token status with the report
                                        
                                        event: school response the ui                                                                                                                                                                                                                                                                  
                                        
                                         
</PRE>


## creating fixtures


 - [HOW_TO_CREATE_FIXTURE.md](https://github.com/2XL/junit-daemon/blob/master/fixture/README.md)




## setup autocomplete[optional]

install autocomplete to enhance tester script autocomplete
```bash
# need root to create: [/etc/bash_completion.d/tester]
└─ $ ▶ sudo ./tester setup

bash_script_where: [/path-to-project/junit-daemon/tester]
bash_autocomplete: [/etc/bash_completion.d/tester]


└─ $ ▶ tester list
demo.yml
request.yml
template.yml
request-junit-5.0.1.yml
exported_challenge.yml


└─ $ ▶ tester run [TAB-KEY] # it will list *.yml files from fixture directory                
demo.yml                 exported_challenge.yml   request-junit-5.0.1.yml  request.yml              template.yml  
```



## test fixtures as submissions

```bash 


└─ $ ▶ docker-compose up 

└─ $ ▶ tester run demo.yml


  
```












## TODO

 - [TODO.md](https://github.com/2XL/junit-daemon/blob/master/TODO.md)