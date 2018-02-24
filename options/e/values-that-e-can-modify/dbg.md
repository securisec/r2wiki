<!-- TITLE: dbg -->

# dbg

- `dbg.aftersyscall` Stop execution before the syscall is executed (see dcs) _Default is true_
- `dbg.args` Set the args of the program to debug
- `dbg.backend` Select the debugger backend _Default is native_
- `dbg.bep` Break on entrypoint _Default is loader_
- `dbg.bpinmaps` Force breakpoints to be inside a valid map _Default is true_
	- > `dbg.bpinmaps` can be used to place breakpoints / see unmapped memory
- `dbg.bpsize` Size of software breakpoints _Default is 8_
- `dbg.bpsysign` Ignore system breakpoints _Default is false_
- `dbg.btalgo` Select backtrace algorithm _Default is fuzzy_
- `dbg.btdepth` Depth of backtrace _Default is 128_
- `dbg.clone` Stop execution if new thread is created _Default is false_
- `dbg.consbreak` SIGINT handle for attached processes _Default is false_
- `dbg.exe.path` Path to binary being debugged
	- > `dbg.exe.path` Helpful for when debugging a remote binary. May help loading symbols properly. Need to specify the base address with `-B` while loading with r2.
- `dbg.execs` Stop execution if new thread is created _Default is false_
- `dbg.exitkills` Kill process on exit _Default is true_
- `dbg.follow` Follow program counter when pc > core->offset + dbg.follow _Default is 32_
- `dbg.follow.child` Continue tracing the child process on fork. By default the parent process is traced _Default is false_
- `dbg.forks` Stop execution if fork() is done (see dbg.threads) _Default is false_
- `dbg.funcarg` Display arguments to function call in visual mode _Default is false_ [source](https://github.com/radare/radare2/issues/9349#issuecomment-368015838)
	- > To use `dbg.funcarg`, step into a call which in `Vpp` visual mode. [asciinema](https://asciinema.org/a/d6lfoD7s4LSqY0tx1z7nO0IYQ)
- `dbg.gdb.page_size` Page size on gdb target (useful for QEMU) _Default is 0x00001000_
- `dbg.gdb.retries` Number of retries before gdb packet read times out _Default is 10_
- `dbg.hwbp` Set HW or SW breakpoints _Default is 0_
- `dbg.libs` If set stop when loading matching libname
- `dbg.malloc` Choose malloc structure parser _Default is jemalloc_
- `dbg.profile` Path to RRunProfile file
	- > 🚀 Can use dgb.profile to pass multiple args to a debugged binary. [asciinema](https://asciinema.org/a/COJ7JEDbNgESV7XZ7oeQlpjAH)
- `dbg.slow` Show stack and regs in visual mode in a slow but verbose mode _Default is false_ 
	- > Set `e dbg.slow=1` to get a more PEDA like visual debugging. `Vpp`
- `dbg.status` Set cmd.prompt to '.dr*' or '.dr*;drd;sr PC;pi 1;s-' _Default is false_
- `dbg.swstep` Force use of software steps (code analysis+breakpoint) _Default is false_
- `dbg.threads` Stop all threads when debugger breaks (see dbg.forks) _Default is false_
- `dbg.trace` Trace program execution (see asm.trace) _Default is false_
- `dbg.trace.inrange` While tracing, avoid following calls outside specified range _Default is false_
- `dbg.trace.libs` Trace library code too _Default is true_
- `dbg.trace.tag` Trace tag _Default is 0_
- `dbg.unlibs` If set stop when unloading matching libname

<p hidden>dbg.bpinmaps dbg.aftersyscall dbg.args dbg.backend dbg.bep dbg.bpinmaps dbg.bpsize dbg.bpsysign dbg.btalgo dbg.btdepth dbg.clone dbg.consbreak dbg.exe.path dbg.execs dbg.exitkills dbg.follow dbg.follow.child dbg.forks dbg.gdb.page_size dbg.gdb.retries dbg.hwbp dbg.libs dbg.malloc dbg.profile dbg.slow dbg.status dbg.swstep dbg.threads dbg.trace dbg.trace.inrange dbg.trace.libs dbg.trace.tag dbg.unlibs</p>