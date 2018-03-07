
Clean the repo

```
make clean
```

Fill src and tests folder with you source files then run
```
└─ $ ▶ inv export -h
Usage: inv[oke] [--core-opts] export [--options] [other tasks here ...]

Docstring:
  Generate fixture yml from src and tests

  :param ctx:
  :param source_home: (default:'src')
  :param test_home: (default:'tests')
  :param fixture_home: (default:'fixture')
  :param fixture_name: (default:'exported_challenge.yml')
  :param is_correct: (default:False)
  :return:

Options:
  --, --is-correct
  -f STRING, --fixture-home=STRING
  -i STRING, --fixture-name=STRING
  -s STRING, --source-home=STRING
  -t STRING, --test-home=STRING


$ inv export -- # generate fixture is_correct=true
$ inv export # generate fixture is_correct=false  

```