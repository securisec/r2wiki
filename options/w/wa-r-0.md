<!-- TITLE: wA -->

#  `wA[?] r 0` alter/modify opcode at current seek (see wA?)


```text
Usage: wA[type] [value]
```


- Types 
	- r raw write value
	- v set value (taking care of current address)
	- d destination register
	- 0 1st src register
	- 1 2nd src register
	- Example:wA r 0 # e800000000