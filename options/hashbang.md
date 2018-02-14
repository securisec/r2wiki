<!-- TITLE: # -->

#  `#` Hashbang to run an rlang script


```
Usage #!interpreter [<args>] [<file] [<<eof]
```


- `#` comment - do nothing
- `#!` list all available interpreters
- `#!python` run python commandline
- `#!python foo.py` run foo.py python script (same as '. foo.py')
- `#!python arg0 a1 <<q` set arg0 and arg1 and read until 'q'