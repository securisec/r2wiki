<!-- TITLE: afl -->

#  `afl[?] [l*] [fcn name]`   list functions (addr, size, bbs, name) (see afll)

- `afl`   list functions
	- > The columns of the `afl` command are *offset/address*, *nbbs*, *size* and *name*
- `afla` Not documented
- `aflc` 🚀 count of functions [asciinema](https://asciinema.org/a/TMvqJRphF2RVI0nNerxzr72pL)
- `aflj` 🚀 list functions in json [asciinema](https://asciinema.org/a/XvEb7StzQ3C1BAAlvn9CDvqLR)
	- > `aflj` can be used to show the size of a function

  > Use `aflj` to get the name of each value in `afl`
- [`afll` list functions in verbose mode](/options/a/af/afll)
	- > 🚀 `afll` will display a table of functions with their address, size, nbbs, edges, min and max bound, range calls, local variables, args xrefs and more. The different colors refer to read, write and execute along with invalid and printable. [asciinema](https://asciinema.org/a/N2QjD5o8X2d1t024LTr9w4wU7)
- `afllj`  list functions in verbose mode (alias to aflj)
- `aflq`   list functions in quiet mode
	- > `aflq` only returns the offsets of all the functions
- `aflqj`   list functions in json quiet mode
- `afls`   print sum of sizes of all functions

<p hidden>afl aflc aflj afll aflq aflqj afls</p>