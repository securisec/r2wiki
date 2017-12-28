<!-- TITLE: Code samples -->
# Code samples
## Bruteforce
### My version of the solver for Unknown from TUCTF 2017 (this is just a placeholder for now)

	```python
	# -*- coding: utf-8 -*-
	import r2pipe
	import sys

	additional_chars = ''
	chrs = additional_chars + '{}_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

	flag = list('-' * 56)
	addr = 0x401c82
	r = r2pipe.open('/vagrant/tuctf/reversing/unknown', flags=['-2'])
	r.cmd('aaa')
	for x in range(0, len(flag)):
			for i, c in enumerate(chrs):
					flag[x] = c
					r.cmd('doo %s' % ''.join(flag))
					r.cmd('db %s' % addr)
					r.cmd('%sdc' % str(x + 1))
					eax = int(r.cmd('dr rax'), 16)
					sys.stdout.write('\r' + ''.join(flag))
					sys.stdout.flush()
					if eax == 0:
							break
	```
	
## Automation
### Set a breakpoint in every call inside a function
	
```python
# make sure the binary is being debugged
import r2pipe

r = r2pipe.open()
r.cmd('aa')
json = r.cmdj('pdfj @ $$')

for i in json['ops']:
		if i['type'] == 'call':
				r.cmd('db @ %s' %hex(i['offset']))
```
> To invoke, simply call the function with `#!pipe python /path/to/script.py dpe` (dpe will automatically get the binaries path)

## Lazy scripts
### Copy the output of any r2 command. Invoke with `. ./script.py`
```python
# To use, simply make an alias and pass the desired command as an argument
import r2pipe
from pyperclip import copy
from sys import argv
import re

r = r2pipe.open()
data = r.cmd(argv[1])
print data
ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
data = ansi_escape.sub('', data)
copy(data)
print 'Copied'
```