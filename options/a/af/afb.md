<!-- TITLE: afb -->

#  `afb[?] [addr]`   List basic blocks of given function

- `.afbr-`   Set breakpoint on every return address of the function
- `.afbr-*`   Remove breakpoint on every return address of the function
- `afb [addr]`   list basic blocks of function
- `afb. [addr]`   show info of current basic block
- `afb+ fcn_at bbat bbsz [jump] [fail] ([type] ([diff]))`   add basic block by hand
- `afbr`   Show addresses of instructions which leave the function
	> `afbr` can be used to find the address where a function exits or returns
- `afbi`   print current basic block information
- `afbj`   show basic blocks information in json
- `afbe bbfrom bbto`   add basic-block edge for switch-cases
- `afB [bits]`   define asm.bits for the given function

<p hidden>afbr afb afb+ .afbr afbi afbj afbe afB</p>