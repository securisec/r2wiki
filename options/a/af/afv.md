<!-- TITLE: afv -->

#  `afv[bsra]?`   manipulate args, registers and variables in 
- [ `afvr[?]`   manipulate register based arguments](/options/a/af/afv/afvr)
-	[ `afvb[?]`   manipulate bp based arguments/locals](/options/a/af/afv/afvb)
-	[ `afvs[?]`   manipulate sp based arguments/locals](/options/a/af/afv/afvs)
- `afvR [varname]`   list addresses where vars are accessed
- `afvW [varname]`   list addresses where vars are accessed
	> 🚀 `afvW` can be used to show all addresses where local variables are accessed or used. [asciinema](https://asciinema.org/a/SHszmEf7H6iqliyML3ElNznEQ)
- `afva`   analyze function arguments/locals
- [ `afvd [name]` output r2 command for displaying the value of args/locals in the debugger](/options/a/af/afv/afvd)
	> 🚀 ⭐ `afvd` shows how the local variables are being set up. [asciinema](https://asciinema.org/a/2udrCGW9OCrhsaKAdIUfQHbvT)

  > 🚀 `afvd somevarname` will return the r2 command. Prefixing a `.` will run that command directly. Example `.afvd somevarname`[asciinema](https://asciinema.org/a/BXT3vqvqOmBTnwsOs8H6DyEdj)
- `afvn [old_name] [new_name]`   rename argument/local
	> Use `afvn` to rename local variables and arguments
- `afvt [name] [new_type]`   change type for given argument/local
- `afv-([name])`   remove all or given var

<p hidden>afvr afvb afvs afvR afvW afva afvd afvn afvt afv variable</p>