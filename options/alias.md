<!-- TITLE: $ Alias -->
#  `$` Alias


```
Usage: $alias[=cmd] [args...]Alias commands
```

- `$` list all defined aliases
	- > 🚀 `$` can be used as variables. [asciinema](https://asciinema.org/a/9XsUEQySaKiNp3WJFeC2AdfoF)
- `$*` same as above, but using r2 commands
	- > Use `$*` to see values of all user defined variables or aliases. 
- `$dis='af;pdf'` create command - analyze to show function <p hidden>$dis</p>
- `$test=#!pipe node /tmp/test.js create command - rlangpipe script`
- `$dis=` undefine alias
- `$dis` execute the previously defined alias
- `$dis?` show commands aliased by 'analyze'
	- > Example `$somevar?` will show the value assigned to somevar variable

- `$$          `  here (current virtual seek)
- `$$$         `  current non-temporary virtual seek
- `$?          `  last comparison value
- `$alias=value`  alias commands (simple macros)
- `$b          `  block size
- `$B          `  base address (aligned lowest map address)
- `$f          `  jump fail address (e.g. jz 0x10 => next instruction)
- `$fl         `  flag length (size) at current address (fla; pD $l @ entry0)
- `$F          `  current function size
- `$FB         `  begin of function
- `$Fb         `  address of the current basic block
- `$Fs         `  size of the current basic block
- `$FE         `  end of function
- `$FS         `  function size
- `$Fj         `  function jump destination
- `$Ff         `  function false destination
- `$FI         `  function instructions
- `$c,$r       `  get width and height of terminal
- `$Cn         `  get nth call of function
- `$Dn         `  get nth data reference in function
- `$D          `  current debug map base address ?v $D @ rsp
- `$DD         `  current debug map size
- `$e          `  1 if end of block, else 0
- `$j          `  jump address (e.g. jmp 0x10, jz 0x10 => 0x10)
- `$Ja         `  get nth jump of function
- `$Xn         `  get nth xref of function
- `$l          `  opcode length
- `$m          `  opcode memory reference (e.g. mov eax,[0x10] => 0x10)
- `$M          `  map address (lowest map address)
- `$MM         `  map size (lowest map address)
- `$o          `  here (current disk io offset)
- `$p          `  getpid()
- `$P          `  pid of children (only in debug)
- `$s          `  file size
- `$S          `  section offset
- `$SS         `  section size
- `$v          `  opcode immediate value (e.g. lui a0,0x8010 => 0x8010)
- `$w          `  get word size, 4 if asm.bits=32, 8 if 64, ...
- `${ev}       `  get value of eval config variable
- `$r          `  get console height
- `$r{reg}     `  get value of named register
- `$k{kv}      `  get value of an sdb query value
- `$s{flag}    `  get size of flag
- `RNum        `  $variables usable in math expressions