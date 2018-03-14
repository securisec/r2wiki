<!-- TITLE: cmd -->

# cmd

- `cmd.bp` Run when a breakpoint is hit
- `cmd.cprompt` Column visual prompt commands
- `cmd.depth` Maximum command depth _Default is 10_
- `cmd.esil.intr` Command to run when an esil interrupt happens
- `cmd.esil.ioer` Command to run when esil fails to IO (invalid read/write)
- `cmd.esil.mdev` Command to run when memory device address is accessed
- `cmd.esil.todo` Command to run when the esil instruction contains TODO
- `cmd.esil.trap` Command to run when an esil trap happens
- `cmd.fcn.delete` Run when a function is deleted
- `cmd.fcn.new` Run when new function is analyzed
- `cmd.fcn.rename` Run when a function is renamed
- `cmd.gprompt` Graph visual prompt commands
- `cmd.graph` Command executed by 'agv' command to view graphs _Default is agf_
- `cmd.hit` Run when a search hit is found
  - > _Run a command/action when a search hit is found_
- `cmd.hitinfo` Show info when a tracepoint/breakpoint is hit _Default is 1_
- `cmd.log` Every time a new T log is added run this command
- `cmd.open` Run when file is opened
- `cmd.pdc` Select pseudo-decompiler command to run after pdc
- `cmd.prompt` Prompt commands
- `cmd.repeat` Empty command an alias for '..' (repeat last command) _Default is false_
- `cmd.stack` Command to display the stack in visual debug mode
	- > 🚀 Use a macro to change to an alternate view of the stack `(changeStackView , e cmd.stack = pxr 40@r:SP, e dbg.slow=false)` [asciinema](https://asciinema.org/a/GaXGDXx0qgmsSGMlxuwnXOCNp) _From @NistelbergerK_
- `cmd.times` Run when a command is repeated (number prefix)
- `cmd.visual` Replace current print mode
- `cmd.vprompt` Visual prompt commands
- `cmd.xterm` xterm command to spawn with V@ _Default is xterm -bg black -fg gray -e_

<p hidden>cmd.bp cmd.cprompt cmd.depth cmd.esil.intr cmd.esil.ioer cmd.esil.mdev cmd.esil.todo cmd.esil.trap cmd.fcn.delete cmd.fcn.new cmd.fcn.rename cmd.gprompt cmd.graph cmd.hit cmd.hitinfo cmd.log cmd.open cmd.prompt cmd.repeat cmd.stack cmd.times cmd.visual cmd.vprompt cmd.xterm</p>