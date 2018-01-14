<!-- TITLE: afl -->

#  `afl[?] [l*] [fcn name]`   list functions (addr, size, bbs, name) (see afll)

- `afl`   list functions
- `aflc`   count of functions
- `aflj`   list functions in json
	> `aflj` can be used to show the size of a function
- `afll` list functions in verbose mode
	> 🚀 `afll` will display a table of functions with their address, size, nbbs, edges, min and max bound, range calls, local variables, args xrefs and more. The different colors refer to read, write and execute along with invalid and printable. [asciinema](https://asciinema.org/a/N2QjD5o8X2d1t024LTr9w4wU7)
- `aflq`   list functions in quiet mode
- `aflqj`   list functions in json quiet mode
- `afls`   print sum of sizes of all functions

<p hidden>afl aflc aflj afll aflq aflqj afls</p>