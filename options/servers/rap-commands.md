<!-- TITLE: rap Commands -->

# rap commands:

- `=` list all open connections
- `=<[fd] cmd` send output of local command to remote fd
- `=[fd] cmd` exec cmd at remote 'fd' (last open is default one)
- `=! cmd` run command via r_io_system
- `=+ [proto://]host` add host (default=rap://, tcp://, udp://)
- `=-[fd]` remove all hosts or host 'fd'
- `==[fd]` open remote session with host 'fd', 'q' to quit
- `=!=` disable remote cmd mode
- `!=!` enable remote cmd mode

<p hidden>!=!</p>