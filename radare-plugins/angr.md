<!-- TITLE: angr and r2 -->

# pimp (triton)
[github/pimp](https://github.com/kamou/pimp)
# r2angr
[github/r2angr](https://github.com/radare/radare2-extras/tree/master/r2angr)
# ⭐ r4ge
[github/r4ge](https://github.com/gast04/r4ge)

## Installation
- Clone the repository
- `[sudo] pip install -U r2pipe termcolor IPython angr simuvex`
- Echo the following to the `~/.radare2rc` file. They can be used inside radare2 shell independantly also.
	- To invoke the macros, run them with `.(marcoName [args])
	
		```text
		(r4ge, #!pipe python2.7 /pathToFile/r4ge.py)
		(markMemSymbolic addr bytes name, #!pipe python2.7 /pathToFile/createVariable.py symb $0 $1 $2)
		(addHook addr instructions bytes comment, #!pipe python2.7 /pathToFile/createVariable.py hook $0 $1 $2 $3)
		(addAssert addr assertions comment, #!pipe python2.7 /pathToFile/createVariable.py assert $0 $1 $2)
		(checkStdout content,  #!pipe python2.7 /pathToFile/createVariable.py checkstdout $0)
		(createScript name, #!pipe python2.7 /pathToFile/createScript.py $0)
		(callFunction retval, #!pipe python2.7 /pathToFile/callFunction.py $0)
		```
	- Replace `/pathToFile` as needed

## Command description and usage example
- `(r4ge)` main plugin file, performs static and dynamic analysis

- `(markMemSymbolic addr bytes name)` mark a specific memory region as symbolic (addr: start address, bytes: how many bytes, name: name the variable)

- `(addHook addr instructions bytes comment)` create hooks in r2 and patch function calls or other statements (syntax of the instructions: rax=0x4 or rax=0x4;rbx=0x10)

- `(addAssert addr assertions comment)` create asserts to check register values during exploration (syntax of the instructions: rax==0x3 or rax#=0x3;rax<=0x10) Note: # is used instead of >, cause r2 uses > as pipe operator.

- `(checkStdout content)` it is also possible to search for a specific string in stdout, just call the makro below. this will ignore find flags, but will consider hooks and asserts. (r2 has many special characters so it may not be possible to put arbitrary strings in the makro but you can modify the r2-variable by your own)

- `(createScript name)` create an angr script out of the current r2 session

- `(callFunction retval)` call a function and specifiy the return value (currently in development mode)
