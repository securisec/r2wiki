<!-- TITLE: . -->

#  `.` Define macro or load r2, cparse or rlang file
##
Usage: .[r2cmd] | [file] | [!command] | [(macro)] # define macro or load r2, cparse or rlang file
> When prefixed with a `.` and postfixed with a `*`, then the output of the command is interpreted as r2 commands and executed. Example: `.idp*`
- `.` repeat last command backward
- `. foo.r2` Run the commands found in foo.r2. Works with .py files also. 
	- > In case of a .py file, it will run and interpret commands set using `r2pipe`

- `.r2cmd` interpret the output of the command as r2 commands
- `.. [file]` run the output of the execution of a script as r2 commands
- `...` repeat last command forward (same as \n)
- `.:8080` listen for commands on given tcp port
- `.—` terminate tcp server for remote commands
- `. foo.r2` interpret r2 script
- `.-` open cfg.editor and interpret tmp file
- `.!rabin -ri $FILE` interpret output of command
- `.(foo 1 2 3)` run macro 'foo' with args 1, 2, 3. Find more info in [ `(` Macros](./macros)
- `./ ELF` interpret output of command /m ELF as r. commands

<p hidden>.r2cmd .!rabin</p>