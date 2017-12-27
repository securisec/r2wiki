<!-- TITLE: afv -->

#  `afv[bsra]?`   manipulate args, registers and variables in 
- [ `afvr[?]`   manipulate register based arguments](/options/a/af/afv/afvr)
-	[ `afvb[?]`   manipulate bp based arguments/locals](/options/a/af/afv/afvb)
-	[ `afvs[?]`   manipulate sp based arguments/locals](/options/a/af/afv/afvs)
- `afvR [varname]`   list addresses where vars are accessed
- `afvW [varname]`   list addresses where vars are accessed
- `afva`   analyze function arguments/locals
- [ `afvd`  show local variables during debugging](/options/a/af/afv/afvd)
	> 🚀 ‼️ `afvd` shows how the local variables are being set up. [asciinema](https://asciinema.org/a/2udrCGW9OCrhsaKAdIUfQHbvT)
- `afvn [old_name] [new_name]`   rename argument/local
- `afvt [name] [new_type]`   change type for given argument/local
- `afv-([name])`   remove all or given var

<p hidden>afvr afvb afvs afvR afvW afva afvd afvn afvt afv</p>