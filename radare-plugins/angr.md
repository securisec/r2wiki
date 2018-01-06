<!-- TITLE: angr and r2 -->

# pimp (triton)
[github/pimp](https://github.com/kamou/pimp)
# r2angr
[github/r2angr](https://github.com/radare/radare2-extras/tree/master/r2angr)
# r4ge
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
