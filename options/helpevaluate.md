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
- **`?b [num]`** 🚀 show binary value of number [asciinema](https://asciinema.org/a/4lauRRlFZHiJmpAQUv1FlxDfC)
- **`?b64[-] [str]`** 🚀 encode/decode in base64 [asciinema](https://asciinema.org/a/xV77ADJ1jf2w43Lr9RS9fIy76)
- **`?btw num|(expr) num|(expr) num|(expr)`** returns boolean value of a <= b <= c
- **`?B [elem]`** show range boundaries like 'e?search.in
- **`?d[.] opcode`** 🚀 describe opcode for asm.arch [asciinema](https://asciinema.org/a/F5bPaITylZ1qGTtIh8slo8xr1)
	> Use: `?d[.] [opcode]`    to get the description of the opcode
- **`?e[nbgc] string`** echo string (nonl, gotoxy, column, bars)
- **`?E string`** ** ** clippy messages.
- **`?f [num] [str]`** map each bit of the number as flag string index
- **`?F`** flush cons output
- **`?h [str]`** calculate hash for given string
- **`?i`** ** ** can be used to pass stdin input
- **`?i[ynmkp] arg`** prompt for number or Yes,No,Msg,Key,Path and store in $$?
- **`?ik`** press any key input dialog
- **`?im message`** 🚀 show message centered in screen [asciinema](https://asciinema.org/a/vmSYaPY9RJfssBpN8o6JS2F6K)
- **`?in prompt`** noyes input prompt
- **`?iy prompt`** yesno input prompt
- **`?l str`** returns the length of string
- **`?o num`** 🚀 get octal value [asciinema](https://asciinema.org/a/DqczvLnEep64MSqLffoMpgYqz)
- **`?O [id]`** List mnemonics for current asm.arch / asm.bits
	> Usage: `?O[jd] [arg]` .. list all mnemonics for asm.arch (d = describe, j=json)
- **`?p vaddr`** get physical address for given virtual address
- **`?P paddr`** get virtual address for given physical one
- **`?r [from] [to]`** 🚀 generate random number between from-to [asciinema](https://asciinema.org/a/KDsEFp4p723UZa166Qmw0gu2S)
- **`?s from to step`** sequence of numbers from to by steps
- **`?S addr`** return section name of given address
- **`?t cmd`** 🚀 returns the time to run a command [asciinema](https://asciinema.org/a/GJhqTgd9OiWEXA0RcmzWHrCH2)
- **`?T`** show loading times
- **`?u num`** get value in human units (KB, MB, GB, TB)
- **`?v eip-0x804800`** show hex value of math expr
- [**`?vi rsp-rbp`** show decimal value of math expr](/options/helpevaluate/vi)
- [**`?V`** show library version of r_core](/options/helpevaluate/cap-v)
- **`?w addr`** 🚀 show what's in this address (like pxr/pxq does) [asciinema](https://asciinema.org/a/012GFhmRtgZ4dVe0SJRbVUFxH)
- **`?x str`** 🚀 returns the hexpair of number or string [asciinema](https://asciinema.org/a/deh7r6WHZ4AOoH8hhfgODrzDR)
- **`?x+num`** like ?v, but in hexpairs honoring cfg.bigendian
- **`?x-hexst`** convert hexpair into raw string with newline
- **`?X num|expr`** 🚀 returns the hexadecimal value numeric expr [asciinema](https://asciinema.org/a/IeIKCOC5IcXi47D4TTAU6DCVt)
- **`?y [str]`** show contents of yank buffer, or set with string