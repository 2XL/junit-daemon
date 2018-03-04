

# Description of a list of pipeline inline command:

    check jinja api and adapt to it
    - the django project root inner docker instance will be:
      * /opt/app
    - base feature
      * given a submission
      * walk trough the pipeline and apply all the commands
    - example:


## Example submission

    definitions
    %%rules
    user code
    %%end_rule
    
    %%rules
    user code
    %%end_rule
## Commands use case and composed use case:

 - [ ] `$CREATE`
 
```bash
# create or replace file with value
%%CREATE%%file_path.file_name.extension%%
value
```
 - [ ] `$UPDATE`

```bash
# update source from existing file, lookup for a key :: use case: update part of file
%%UPDATE%%file_path.file_name.extension%%jinja.key
value 
``` 

 - [ ] `$PUT`

```bash
# append source to existing file or create new 
%%PUT%%file_path.file_name.extension%%
value 
```

 - [ ] `$DROP`
 
```bash
# drop file or section of a file
%%DROP%%file_path.file_name.extension%%jinja.key
%%DROP%%file_path.file_name.extension 
``` 




# TODO: hello world django test 

```javascript
data={
    'code_challenge_task': self.codechallenge_java_task_fixture.pk,
    'submission': '{"files":[ { "source":"variable.py", "content":"' + code_challenge_64 + '"}]}'
}
```