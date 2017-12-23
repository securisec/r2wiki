<!-- TITLE: af -->

#  `af[?]`   analyze Functions

- `af ([name]) ([addr])`   analyze functions (start at addr or $$)

- `afr ([name]) ([addr])`   analyze functions recursively

- `af+ addr name [type] [diff]`   hand craft a function (requires afb+)

- `af- [addr]`   clean all function analysis data (or function at addr)
- `afb+ fcnA bbA sz [j] [f] ([t]( [d]))`   add bb to function @ fcnaddr
[ `afb[?] [addr]`   List basic blocks of given function](/options/a/af/afb)
- `afB [bits]`   set current function as thumb (change asm.bits)
[ `afC[lc] ([addr])@[addr]`   calculate the Cycles (afC) or Cyclomatic Complexity (afCc)](/options/a/af/afC)
[ `afc[?] type @[addr]`   set calling convention for function](./afc-type-addr-set-calling-convention-for-function-de18fce7-8ce3-4612-8357-7f86bb0d2506.md)

- `aff`   re-adjust function boundaries to fit

- `afF[1|0|]`   fold/unfold/toggle
[ `afi [addr|fcn.name]`   show function(s) information (verbose afl)](./afi-addr-fcn-name-show-function-s-information-verbose-afl-dea687f3-901c-42b1-a7ab-e08aba895c93.md)
[ `afl[?] [l*] [fcn name]`   list functions (addr, size, bbs, name) (see afll)](./afl-l-fcn-name-list-functions-addr-size-bbs-name-see-afll-39bb9543-9de0-4ea4-b847-059965b93268.md)

- `afo [fcn.name]`   show address for the function named like this

- `afm name`   merge two functions


- `afM name`   print functions map
[ `afn[?] name [addr]`   rename name for function at address (change flag too)](./afn-name-addr-rename-name-for-function-at-address-change-flag-too-a378ab1c-eb3d-4763-aaaa-e2a706bbed3e.md)

- `afna`   suggest automatic name for current offset
- `afs [addr] [fcnsign]`   get/set function signature at current address
- `afS[stack_size]`   set stack frame size for function at current address
- `afu [addr]`   resize and analyze function from current address until addr
[ `aft[?]`   type matching, type propagation](./aft-type-matching-type-propagation-300ded28-0008-4c98-9e60-afb50f80bee1.md)
[ `afv[bsra]?`   manipulate args, registers and variables in](./afv-bsra-manipulate-args-registers-and-variables-in-ec2e1b96-8f41-4fe1-8d9d-7a124cec6133.md)
[ `afx[cCd-] src dst`   add/remove code/Call/data/string reference](./afx-cCd-src-dst-add-remove-code-Call-data-string-reference-b61b2a06-a498-42e7-a0c2-ccd14afe7940.md)