<!-- TITLE: f -->

#  `f` Add flag at current address


```
Usage: f [?] [flagname] # Manage offset-name flags
```


## Tips
  - > To show all the contents of a flag space, use `fs [space_name]; f`
---
- `f` list flags (will only list flags from selected flagspaces)
	- > To create a new flag, use `f flag_name @ offset`
- `f?flagname` check if flag exists or not, See ?? and ?!
- `f. [*[*]]` list local per-function flags (*) as r2 commands
- `f.blah=$$+12` set local function label named 'blah'
- `f*` list flags in r commands
- `f name 12 @ 33` set flag 'name' with length 12 at offset 33
- `f name = 33` alias for 'f name @ 33' or 'f name 1 33'
- `f name 12 33 [cmt]` same as above + optional comment
- `f-.blah@fcn.foo` delete local label from function at current seek (also f.-)
- `f--` delete all flags and flagspaces (deinit)
- `f+name 12 @ 33` like above but creates new one if doesnt exist
- `f-name` remove flag 'name'
- `f-@addr` remove flag at address expression
- `f. fname` list all local labels for the given function
- `f= [glob]` list range bars graphics with flag offsets and sizes
  - Screenshot

    ![](/uploads/small-f/f-equals.png)

- `fa [name] [alias]` alias a flag to evaluate an expression
- `fb [addr]` set base address for new flags
- `fb [addr] [flag*]` move flags matching 'flag' to relative addr

- [ `fc[?][name] [color]` 🚀 set color for given flag](/options/f/fc) [asciinema](https://asciinema.org/a/RQeQkWUPYpKCONJQtLAOuvUAI)

- `fC [name] [cmt]` 🚀 set comment for given flag [asciinema](https://asciinema.org/a/RQeQkWUPYpKCONJQtLAOuvUAI)

- [ `fd addr` return flag+delta](/options/f/fd)

- `fe-` resets the enumerator counter
- `fe [name]` create flag name.#num# enumerated flag. See fe?
	- > 🚀 `fe` can be used to iterate in a loop and create numbered flags. [asciinema](https://asciinema.org/a/CcRKt9q90c12nSooYxWdHhtyg)
- `ff ([glob])` distance in bytes to reach the next flag (see sn/sp)
- `ffs` nothing documented
- `fi [size] | [from] [to]` show flags in current block or range
- `fg` bring visual mode to foreground
	- > `fg` appears to do exactly what `V` does
- `fj` list flags in JSON format
- `fl (@[flag]) [size]` show or set flag length (size)
- `fla [glob]` automatically compute the size of all flags matching glob
- `fm addr` move flag at current offset to new address
- `fn` list flags displaying the real name (demangled)
- `fo` show fortunes
- `fr [old] [[new]]` rename flag (if no new flag current seek one is used)

- [ `fR[?] [f] [t] [m]` relocate all flags matching f&~m 'f'rom, 't'o, 'm'ask](/options/f/fcapr)

- [ `fs[?]+-*` manage flagspaces](/options/f/fs)

- `fS[on]` sort flags by offset or name
- `ft` flag tags [twitter](https://pbs.twimg.com/media/Dc7H-yUWAAAfeg1.jpg:large)
- `fV[*-] [nkey] [offset]` dump/restore visual marks (mK/'K)
- `fx[d]` show hexdump (or disasm) of flag:flagsize
- `fq` list flags in quiet mode

- [ `fz[?][name]` add named flag zone -name to delete. see fz?[name]](/options/f/fz)

<p hidden>f+ f- f= fC fe fe- fg fj fl fla fm fn fo fr fR fs fS fV fx fq fz ff ffs</p>
