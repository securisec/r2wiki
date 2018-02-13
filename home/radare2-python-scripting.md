<!-- TITLE: Radare 2 Python Scripting -->

# Radare2 Python scripting
## r2pipe
- [Sample scripts could be found here](https://github.com/radare/radare2-r2pipe/tree/master/python/examples)
-  > Python: r2pipe `pip install r2pipe` 

## Basic usage

- To run a python script inside the r2 shell, do not pass a file path. The file can then be called using `.` or `#!pipe /path/to/script.py`
```python
r = r2pipe.open() # no file path
```
	
- Load a binary
```python
import r2pipe
r = r2pipe.open('binary')
```
				

- Disable stderr messages
```python
r = r2pipe.open('binary', flags=['-2']) # pass any options from radare2 as a list in the flags parameter. -2 signifies disable stderr
```

- Run multiple commands (effeciently)
```python
r.cmd('doo; db main; dc') # multiple commands can be passed using a semicolon. In the example; doo (open in debug mode), db main (set breakpoint in main, dc (continue (will hit breakpoint))
```

- Run a command (any command that one runs in the r2 shell can be passed to the cmd method)
```python
import r2pipe
r = r2pipe.open('binary')
print r.cmd('pdf') # disassamble funtion 
```

- Run a command multiple times
```python
r.cmd('3dc') # the 3 represents how many times dc will run. Can be any value
```

## Json output
- Most commands in r2pipe supports json output by including a `j` at the end of the command
```python
import r2pipe
r = r2pipe.open('binary')
json_out = r.cmd('iij') # get import table as json
```

- Instead of using python `json` module to parse the json data, use `cmdj` instead which does the parsing of json objects for you
```python
json = r.cmdj('iij') # parse json output as json objects
```

## Working with registers
- Get values of all registers
```python
r.cmd('drj') # dumps values of all registers in json format
```

- Get value of single register
```python
r.cmd('dr eax') # gets the value of the eax register as a hex string
```

## Open a binary in write mode
- To open a file in write mode, pass the `-w` switch to the flags

```python
r = r2pipe.open('binary', flags=['-w', '-d']
# In this example, we are opening the binary in write and debug mode
```


## User input via stdin (debugging mode)
- Method 1
```python
import r2pipe
r = r2pipe.open(
filename='', flags=['-d', 'rarun2', 'program=binary', 'stdin="AAA"..."any rarun2 key/value pairs"'])
r.cmd('doo') # initially you are debuggign rarun2
```

- Method 2
```python
import r2pipe
with open('profile.rr2', 'w+') as f:
		f.write('#!/path/to/rarun2\nstdin="AAA"')
r = r2pipe.open('binary', flags=['-e', 'dbg.profile=profile.rr2'])
# This method is untested. Use method 1 or 3
```

- Method 3
```python
import r2pipe
r = r2pipe.open('binary')
r.cmd('e dbg.profile=profile.rr2')
# Contents of profile.rr2
# #!/path/to/rarun2
# program=binary
# stdin="AAA"
```
## User input as args (debugging mode)
```python
r.cmd('doo arg') # could be any number of args
```

## Other ways of user input with debugging
```python
r.cmd('dor arg1=some_arg ...')
```
- > `dor` will take any keypair that can be passed via rarun2

## radare2-ctypes
- > pip install radare2-ctypes [radare2 ctypes bindings](https://pypi.python.org/pypi/radare2-ctypes)

```python
from r2.r_core import *
r = RCore()
r.cmd0("?V")
r.cons.flush() 
```


## Blogs

  [Scripting r2 with pipes - pancake - Medium](https://medium.com/@trufae/scripting-r2-with-pipes-47a7e14c50aa)
	
## Videos
[video](https://www.youtube.com/watch?v=y69uIxU0eI8){.youtube}
