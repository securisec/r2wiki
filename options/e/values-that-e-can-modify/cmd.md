<!-- TITLE: cmd -->

# cmd

- **`cmd.bp`** Run when a breakpoint is hit
- **`cmd.cprompt`** Column visual prompt commands
- **`cmd.depth`** Maximum command depth _Default is 10_
- **`cmd.esil.intr`** Command to run when an esil interrupt happens
- **`cmd.esil.ioer`** Command to run when esil fails to IO (invalid read/write)
- **`cmd.esil.mdev`** Command to run when memory device address is accessed
- **`cmd.esil.todo`** Command to run when the esil instruction contains TODO
- **`cmd.esil.trap`** Command to run when an esil trap happens
- **`cmd.fcn.delete`** Run when a function is deleted
- **`cmd.fcn.new`** Run when new function is analyzed
- **`cmd.fcn.rename`** Run when a function is renamed
- **`cmd.gprompt`** Graph visual prompt commands
- **`cmd.graph`** Command executed by 'agv' command to view graphs _Default is agf_
- **`cmd.hit`** Run when a search hit is found
  > _Run a command/action when a search hit is found_
- **`cmd.hitinfo`** Show info when a tracepoint/breakpoint is hit _Default is 1_
- **`cmd.log`** Every time a new T log is added run this command
- **`cmd.open`** Run when file is opened
- **`cmd.prompt`** Prompt commands
- **`cmd.repeat`** Empty command an alias for '..' (repeat last command) _Default is false_
- **`cmd.stack`** Command to display the stack in visual debug mode
- **`cmd.times`** Run when a command is repeated (number prefix)
- **`cmd.visual`** Replace current print mode
- **`cmd.vprompt`** Visual prompt commands
- **`cmd.xterm`** xterm command to spawn with V@ _Default is xterm -bg black -fg gray -e_