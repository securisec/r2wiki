<!-- TITLE: @ -->

#  `@` Misc help for '@' (seek), '~' (grep) (see ~??)


```
Usage: [.][#]<cmd>[*] [`cmd`] [@ addr] [~grep] [|syscmd] [>[>]file]
```


- `0` alias for 's 0'
- `0xaddr` alias for 's 0x..'
- `#cmd` if # is a number repeat the command # times
- `/*` start multiline comment
- `*/` end multiline comment
- `.cmd` execute output of command as r2 script
- `.:8080` wait for commands on port 8080
- `.!rabin2 -re $FILE` run command output as r2 script
- `*` output of command in r2 script format (CC*)
- `j` output of command in JSON format (pdj)
- `~?` count number of lines (like wc -l)
- `~??` show internal grep help
- `~..` internal less
- `~{}` json indent
- `~{}..` json indent and less
- `~word` grep for lines matching word
- `~!word` grep for lines NOT matching word
- `~word[2]` grep 3rd column of lines matching word
- `~word:3[0]` grep 1st column from the 4th line matching word
- `@ 0x1024` temporary seek to this address (sym.main+3)
- `@ [addr]!blocksize` temporary set a new blocksize
- `@a:arch[:bits]` temporary set arch and bits
- `@b:bits` temporary set asm.bits
- `@e:k=v,k=v` temporary change eval vars
- `@r:reg` tmp seek to reg value (f.ex pd@r:PC)
- `@i:nth.op` temporary seek to the Nth relative instruction
- `@f:file` temporary replace block with file contents
- `@o:fd` temporary switch to another fd
- `@s:string` same as above but from a string
- `@x:909192` from hex pairs string
- `@..from to` temporary set from and to for commands supporting ranges temporary partial address seek (see s..)
- `@@=1 2 3` run the previous command at offsets 1, 2 and 3
- `@@ hit*` run the command on every flag matching 'hit*'
- `@@?[ktfb..]` show help for the iterator operator
- `@@@ [type]` run a command on every [type] (see @@@? for help)
- `>file` pipe output of command to file
- `>>file` append to file
- `H>file` pipe output of command to file in HTML
  - > Example:`pdf H>somefile.html`
- `H>>file` append to file with the output of command in HTML
- ``pdi~push:0[0] replace output of command inside the line
- `|cmd` pipe output to command (pd|less) (.dr*)