<!-- TITLE: af -->

#  `af[?]`   analyze Functions

- `af ([name]) ([addr])`   analyze functions (start at addr or $$)

- `afr ([name]) ([addr])`   analyze functions recursively

- `af+ addr name [type] [diff]`   hand craft a function (requires afb+)

- `af- [addr]`   clean all function analysis data (or function at addr)
- `afb+ fcnA bbA sz [j] [f] ([t]( [d]))`   add bb to function @ fcnaddr
- [ `afb[?] [addr]`   List basic blocks of given function](/options/a/af/afb)
- `afB [bits]`   set current function as thumb (change asm.bits)
- [ `afC[lc] ([addr])@[addr]`   calculate the Cycles (afC) or Cyclomatic Complexity (afCc)](/options/a/af/afC)
- [ `afc[?] type @[addr]`   set calling convention for function](/options/a/af/af_small_c)
- `afd [addr]` show function + delta for given offset
- `aff`   re-adjust function boundaries to fit

- `afF[1|0|]`   fold/unfold/toggle
- [ `afi [addr|fcn.name]`   show function(s) information (verbose afl)](/options/a/af/afi)
	> 🚀 `afi[j]` Get various information about a function including size, call-convention, call references local variables, args etc Example [asciinema](https://asciinema.org/a/p3P1PWA5PvLb0LADUXiXIbr9S)
- [ `afl[?] [l*] [fcn name]`   list functions (addr, size, bbs, name) (see afll)](/options/a/af/afl)

- `afo [fcn.name]`   show address for the function named like this

- `afm name`   merge two functions


- `afM name`   print functions map
- [ `afn[?] name [addr]`   rename name for function at address (change flag too)](/options/a/af/afn)

- `afna`   suggest automatic name for current offset
- `afs [addr] [fcnsign]`   get/set function signature at current address
- `afS[stack_size]`   set stack frame size for function at current address
- `afu [addr]`   resize and analyze function from current address until addr
	> `afu` can be used to define both the start and end of a function when manually defining a function
- [ `aft[?]`   type matching, type propagation](/options/a/af/aft)
- [ `afv[bsra]?`   manipulate args, registers and variables in](/options/a/af/afv)
- [ `afx[cCd-] src dst`   add/remove code/Call/data/string reference](/options/a/af/afx)

<p hidden>af afr af+ af- afb+ afB afC afc aff afF afi afl afo afm afM afn afna afs afS afu aft afv afx</p>