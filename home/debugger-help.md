<!-- TITLE: Debugger help -->
# Debugger help
## gdbserver
### gdbserver commands from r2 shell
- `=g port file [args]`   listen on 'port' debugging 'file' using gdbserver
- `=g! port file [args]` same as above, but debug protocol messages (like gdbserver --remote-debug)
- [Additional details regarding gdb and gdbserver can be found here](/home/misc/usage-examples#gdb)

### Directly using gdbserver steps
- Set up and attach gdbserver to a process/binary. Example: `gdbserver localhost:8000 /bin/ls`
- 🚀 Connect to gdbserver using r2. `radare2 -d gdb://localhost:8000` [asciinema](https://asciinema.org/a/V1olGhQv9rhYWdkYxOzDGBntu)
- Use radare2 commands normally
	- > Note that gdbserver implemented this way will die once the r2 session exits

### gdbserver subhelp

```text
Usage: =!cmd args
 =!pid             - show targeted pid
 =!pkt s           - send packet 's'
 =!monitor cmd     - hex-encode monitor command and pass to target interpreter
 =!detach [pid]    - detach from remote/detach specific pid
 =!inv.reg         - invalidate reg cache
 =!pktsz           - get max packet size used
 =!pktsz bytes     - set max. packet size as 'bytes' bytes
 =!exec_file [pid] - get file which was executed for current/specified pid
```

### gdbserver monitor commands `=!monitor help`

## windbg

  [Remote WinDbg · Radare2 Book](https://radare.gitbooks.io/radare2book/content/debugger/windbg.html)
	[windbg usage example](/home/misc/usage-examples#windbg)