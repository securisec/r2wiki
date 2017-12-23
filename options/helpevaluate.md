<!-- TITLE: ? Help / Evalulate -->

#  **`?`** Help or evaluate math expression


```text
Usage: ?[?[?]] expression
```


## **Tips**
  - Use `?i` to give stdin input

---
- **`? eip-0x804800`** show hex and dec result for this math expr

- [ **`?:`** list core cmd plugins](evaluate/core_plugins)

- **`[cmd]?*`** Recursive help for the given cmd
- **`?! [cmd]`** run cmd if $? == 0
- **`?$`** show value all the variables ($)
- **`?+ [cmd]`** run cmd if $? > 0
- **`?- [cmd]`** run cmd if $? < 0
- **`?= eip-0x804800`** hex and dec result for this math expr
- **`?? [cmd]`** run cmd if $? != 0
- **`??`** show value of operation
- **`?_ hudfile`** load hud menu with given file
- **`?b [num]`** show binary value of number
- **`?b64[-] [str]`** encode/decode in base64
- **`?btw num|(expr) num|(expr) num|(expr)`** returns boolean value of a <= b <= c
- **`?B [elem]`** show range boundaries like 'e?search.in
- **`?d[.] opcode`** describe opcode for asm.arch
- **`?e[nbgc] string`** echo string (nonl, gotoxy, column, bars)
- **`?E string`** ** ** clippy messages.
- **`?f [num] [str]`** map each bit of the number as flag string index
- **`?F`** flush cons output
- **`?h [str]`** calculate hash for given string
- **`?i`** ** ** can be used to pass stdin input
- **`?i[ynmkp] arg`** prompt for number or Yes,No,Msg,Key,Path and store in $$?
- **`?ik`** press any key input dialog
- **`?im message`** show message centered in screen
- **`?in prompt`** noyes input prompt
- **`?iy prompt`** yesno input prompt
- **`?l str`** returns the length of string
- **`?o num`** get octal value
- **`?O [id]`** List mnemonics for current asm.arch / asm.bits
- **`?p vaddr`** get physical address for given virtual address
- **`?P paddr`** get virtual address for given physical one
- **`?r [from] [to]`** generate random number between from-to
- **`?s from to step`** sequence of numbers from to by steps
- **`?S addr`** return section name of given address
- **`?t cmd`** returns the time to run a command
- **`?T`** show loading times
- **`?u num`** get value in human units (KB, MB, GB, TB)
- **`?v eip-0x804800`** show hex value of math expr
- **`?vi rsp-rbp`** show decimal value of math expr
- **`?V`** show library version of r_core
- **`?w addr`** show what's in this address (like pxr/pxq does)
- **`?x str`** returns the hexpair of number or string
- **`?x+num`** like ?v, but in hexpairs honoring cfg.bigendian
- **`?x-hexst`** convert hexpair into raw string with newline
- **`?X num|expr`** returns the hexadecimal value numeric expr
- **`?y [str]`** show contents of yank buffer, or set with string