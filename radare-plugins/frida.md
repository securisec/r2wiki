<!-- TITLE: r2frida -->
# r2frida
> [nowsecure/r2frida](https://github.com/nowsecure/r2frida) {.is-info}

## Tips
- > Use the following syntax to trace. Example: `\dtf write iZi` (this was tested against node. Write is the symbol being hooked) {.is-info}
- > `af` Analyze function while using r2frida. [asciinema](https://asciinema.org/a/rDfyFskNxvnguJCQu6AiehUd0)

## Load a binary
### Attach to a running process
#### On the host
- r2 frida://Twitter
- r2 frida://\<pid\>

#### On the device
- r2 frida://\<device_id\>Twitter
- r2 frida://\<device_id\>\<pid\>

### Spawn a process
#### On the host
- r2 frida:///bin/ls
- r2 "frida:///bin/ls -la" _supply arguments_

#### On a device
- r2 frida://\<device_id\>//your.package.name

## Frida commands
> The commands here can be found using `\?` or `=!` when a binary is loaded using frida.

- **`\?`** Show this help
- **`\?V`** Show target Frida version
- **`\/[j] <string|hexpairs>`** Search hex/string pattern in memory ranges (see search.in=?)
	> The regions to be searched can be modied using `e search.in=?`
- **`\/w[j] string`** Search wide string
- **`\/v[1248][j] value`** Search for a value honoring `e cfg.bigendian` of given width
- **`\i`** Show target information
- **`\ii[*]`** List imports
- **`\il`** List libraries
- **`\is[*] <lib>`** List exports/entrypoints of lib
- **`\isa[*] (<lib>) <sym>`** Show address of symbol
- **`\ic <class>`** List Objective-C classes or methods of \<class\>
	> `\ic` _helps you analyze classes and methods._ [asciinema](https://asciinema.org/a/3H4xbEeaBAbgqHX1YvaTk34Tb)
- **`\ip <protocol>`** List Objective-C protocols or methods of \<protocol\>
- **`\fd[*j] <address>`** Inverse symbol resolution
- **`\dd[-][fd] ([newfd])`** List, dup2 or close filedescriptors
- **`\dm[.|j|*]`** Show memory regions
- **`\dma <size>`** Allocate \<size\> bytes on the heap, address is returned
- **`\dmas <string>`** Allocate a string inited with \<string\> on the heap
- **`\dmad <addr> <size>`** Allocate \<size\> bytes on the heap, copy contents from \<addr\>
- **`\dmal`** List live heap allocations created with dma[s]
- **`\dma- (<addr>...)`** Kill the allocations at <addr> (or all of them without param)
- **`\dmp <addr> <size> <perms>`** Change page at \<address\> with \<size\>, protection \<perms\> (rwx)
- **`\dp`** Show current pid
- **`\dpt`** Show threads
- **`\dr`** Show thread registers (see dpt)
- **`\env [k[=v]]`** Get/set environment variable
- **`\dl libname`** Dlopen a library
- **`\dl2 libname [main]`** Inject library using Frida's >= 8.2 new API
- **`\dt <addr> ..`** Trace list of addresses
- **`\dt-`** Clear all tracing
- **`\dtr <addr> (<regs>...)`** Trace register values
- **`\dtf <addr> [fmt]`** Trace address with format (^ixzO) (see dtf?)
      
	```text
		Usage: dtf [format] || dtf [addr] [fmt]
			 ^ = trace onEnter instead of onExit
			 + = show backtrace on trace
			 x = show hexadecimal argument
			 i = show decimal argument
			 z = show pointer to string
			 O = show pointer to ObjC object
	```

- **`\dtSf[*j] [sym|addr]`** Trace address or symbol using the stalker (Frida >= 10.3.13)
- **`\dtS[*j] seconds`** Trace all threads for given seconds using the stalker
- **`\di[0,1,-1] [addr]`** Intercept and replace return value of address
- **`\dx [hexpairs]`** Inject code and execute it (TODO)
- **`\dxc [sym|addr] [args..]`** Call the target symbol with given args
- **`\e[?] [a[=b]]`** List/get/set config evaluable vars

	
	```text
	Usage: e [var[=value]]Evaluable vars
		patch.code      = true
		search.in       = perm:r--
		search.quiet    = false
		stalker.event   = compile
		stalker.timeout = 300
		stalker.in      = raw
	```

- **`\. script`** Run script
- **`\<space> code..`** Evaluate Cycript code
- **`\eval code..`** Evaluate Javascript code in agent side
- **`\dc`** Continue

## Resources, writeups etc
[Spearing data in mobile memory: Building a better R2Frida memory search](https://www.nowsecure.com/blog/2017/03/14/spearing-data-mobile-memory-building-better-r2frida-memory-search/)

## Videos
[r2con2017 - r2frida /by @mrmacete](https://www.youtube.com/watch?list=PLjIhlLNy_Y9Oe-nfcPEpaki0_En5dhQ5S&time_continue=15&v=URyd4bcV-Ik){.youtube}
