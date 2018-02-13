<!-- TITLE: Code samples -->
# Code samples
# Bruteforce
## My version of the solver for Unknown from TUCTF 2017 (this is just a placeholder for now)

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
	
# Automation
- > Place holder
# Helper scripts
## Find args and addresses in stack
[r2args](https://github.com/gast04/r2args)