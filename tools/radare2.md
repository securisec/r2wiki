<!-- TITLE: radare2 -->

# radare2

## **Tips**
  - Load a profile and use two terminals (redirect stdin from another terminal)
    - First, find out the the tty of the second terminal using `tty` . Then put that terminal to sleep, i.e. `sleep 999999`
    - Create a new profile file (named with a `.rr` ) and put the following or any other configuration options

          #!/path/to/rarun2
          stdio=/dev/pts/[number]

    - Run `radare2 -e dbg.profile=profile.rr2 -d binary`
  - Set envrionment variable

        #!/path/to/rarun2
        setenv=FOO=BAR

    Run `radare2 -e dbg.profile=profile.rr2 -d binary` 

  - Pass user input via stdin during debugging

        #!/path/to/rarun2
        stdin=aaaa\nbbbb\ncccc....

    Run `radare2 -e dbg.profile=profile.rr2 -d binary` 

  - To attach to a remote debugger, use the `-D debugger_type` . Example `r2 -D gdb gdb://host:port`
  - Use `-B` to set the base address
	  > -B changes the base address, which is the address used by RBin to rebase all the flags , symbols, etc

    > when you want to map a file at a specific address the -B creates the map at address 0 to be in sync with the PA (physical address)
  - Use `-m` to map a binary at the provided address
	  > -m works for bootloaders, raw firmwares and such

- Use `-hh` to find paths to all environment variables being used
- Use `-n` switch to load a binary in raw more. No VADDR
## Help

```text
Usage: r2 [-ACdfLMnNqStuvwzX] [-P patch] [-p prj] [-a arch] [-b bits] [-i file]
       [-s addr] [-B baddr] [-M maddr] [-c cmd] [-e k=v] file|pid|-|--|=
       -- run radare2 without opening any file
       - same as 'r2 malloc://512'
       = read file from stdin (use -i and -c to run cmds)
       -= perform !=! command to run all commands remotely
       -0 print \x00 after init and every command
       -2 close stderr file descriptor (silent warning messages)
       -a [arch] set asm.arch
       -A run 'aaa' command to analyze all referenced code
       -b [bits] set asm.bits
       -B [baddr] set base address for PIE binaries
       -c 'cmd..' execute radare command
       -C file is host:port (alias for -c+=http://%s/cmd/)
       -d debug the executable 'file' or running process 'pid'
       -D [backend] enable debug mode (e cfg.debug=true)
       -e k=v evaluate config var
       -f block size = file size
       -F [binplug] force to use that rbin plugin
       -h, -hh show help message, 
       -hh for long (show environment variables)
       -H ([var]) display variable
       -i [file] run script file
       -I [file] run script file before the file is opened
       -k [OS/kern] set asm.os (linux, macos, w32, netbsd, ...)
       -l [lib] load plugin file
       -L list supported IO plugins
       -m [addr] map file at given address (loadaddr)
       -M do not demangle symbol names
       -n, -nn do not load RBin info (-nn only load bin structures)
       -N do not load user settings and scripts
       -q quiet mode (no prompt) and quit after -i
       -Q quiet mode (no prompt) and quit faster (quickLeak=true)
       -p [prj] use project, list if no arg, load if no file
       -P [file] apply rapatch file and quit
       -r [rarun2] specify rarun2 profile to load (same as -e dbg.profile=X)
       -R [rr2rule] specify custom rarun2 directive
       -s [addr] initial seek
       -S start r2 in sandbox mode
       -t load rabin2 info in thread
       -u set bin.filter=false to get raw sym/sec/cls names
       -v, -V show radare2 version (-V show lib versions)
       -w open file in write mode
       -x open without exec-flag (asm.emu will not work), See io.exec
	   -X same as -e bin.usextr=false (useful for dyldcache)
       -z, -zz do not load strings or load them even in raw
```


## Debuggers supported 
   - `radare2 -L`

  Those that have a **d** in the first column support debugging

  - _rw_ _ **`ar`** Open ar/lib files [ar|lib]://[file//path] (LGPL3)
  - _rw_ _ **`bfdbg`** BrainFuck Debugger (bfdbg://path/to/file) (LGPL3)
  - _rwd_ **`bochs`** Attach to a BOCHS debugger (LGPL3)
  - _r_d_ **`debug`** Native debugger (dbg:///bin/ls dbg://1388 pidof:// waitfor://) (LGPL3) v0.2.0 pancake
  - _rw_ _ **`default`** open local files using def_mmap:// (LGPL3)
  - _rwd_ **`gdb`** Attach to gdbserver, 'qemu -s', gdb://localhost:1234 (LGPL3)
  - _rw_ _ **`gzip`** read/write gzipped files (LGPL3)
  - _rw_ _ **`http`** http get (http://rada.re/) (LGPL3)
  - _rw_ _ **`ihex`** Intel HEX file (ihex://eeproms.hex) (LGPL)
  - _r_ __ **`mach`** mach debug io (unsupported in this platform) (LGPL)
  - _rw_ _ **`malloc`** memory allocation (malloc://1024 hex://cd8090) (LGPL3)
  - _rw_ _ **`mmap`** open file using mmap:// (LGPL3)
  - _rw_ _ **`null`** null-plugin (null://23) (LGPL3)
  - _rw_ _ **`procpid`** /proc/pid/mem io (LGPL3)
  - _rwd_ **`ptrace`** ptrace and /proc/pid/mem (if available) io (LGPL3)
  - _rwd_ **`qnx`** Attach to QNX pdebug instance, qnx://host:1234 (LGPL3)
  - _rw_ _ **`r2k`** kernel access API io (r2k://) (LGPL3)
  - _rw_ _ **`r2pipe`** r2pipe io plugin (MIT)
  - _rw_ _ **`r2web`** r2web io client (r2web://cloud.rada.re/cmd/) (LGPL3)
  - _rw_ _ **`rap`** radare network protocol (rap://:port rap://host:port/file) (LGPL3)
  - _rw_ _ **`rbuf`** RBuffer IO plugin: rbuf:// (LGPL)
  - _rw_ _ **`self`** read memory from myself using 'self://' (LGPL3)
  - _rw_ _ **`shm`** shared memory resources (shm://key) (LGPL3)
  - _rw_ _ **`sparse`** sparse buffer allocation (sparse://1024 sparse://) (LGPL3)
  - _rw_ _ **`tcp`** load files via TCP (listen or connect) (LGPL3)
  - _rwd_ **`windbg`** Attach to a KD debugger (windbg://socket) (LGPL3)
  - _rwd_ **`winedbg`** Wine-dbg io and debug.io plugin for r2 (MIT)
  - _rw_ _ **`zip`** Open zip files [apk|ipa|zip|zipall]://[file//path] (BSD)

## radare2 man page

```text
RADARE2(1)                                   BSD General Commands Manual                                   RADARE2(1)

NAME
     radare2 — Advanced commandline hexadecimal editor, disassembler and debugger

SYNOPSIS
     radare2 [-a arch] [-b bits] [-B baddr] [-c cmd] [-e k=v] [-i file] [-I prefile] [-k kernel] [-m addr]
             [-p project] [-P patch] [-r rarun2] [-R rr2rule] [-s addr] [-0AdDwntLquvVxX] -|--|=|file

DESCRIPTION
     radare2 is a commandline hexadecimal editor.

     "r2" is the alias program name for radare2.

     This manpage is not updated yet. Feel free to contribute.

     The options are:

     --          Open radare2 on an empty file

     -           Equivalent of 'r2 malloc://512'

     -0          Print \x00 after initialization and after every command executed

     -2          Close stderr before starting RCore

     -a arch     force asm.arch (x86, ppc, arm, mips, bf, java, ...)

     -A          run 'aaa' command before prompt or patch to analyze all referenced code. Use -AA to run aaaa

     -b bits     force asm.bits (16, 32, 64)

     -B baddr    Specify the base address to be used when loading a new binary. See 'e?bin.baddr'

     -c cmd      Execute the given command before giving prompt

     -d          Start in debugger mode

     -D dbg.backend
                 Enable debug mode. Set cfg.debug=true

     -e k=v      Set configuration eval variable key=value. For example -e scr.color=false

     -f          Blocksize = file size

     -i file     Run script file. After the file is loaded

     -I file     Run script file. Before the file is loaded

     -k kernel   Select kernel (asm.os) for syscall resolution

     -l plugfile
                 Load given plugin file

     -L          List supported IO plugins.

     -m addr     map file at given address

     -M          Disable demangling

     -n          Do not perform any analysis (r_bin). Just load the raw file

     -nn         Only load the rbin structures (elf, mach0, ...)

     -N          Do not load user settings/projects from ~/.radare2rc, ~/.config/radare2/radare2rc and the scripts
                 inside .../radare2rc.d/ directory.

     -q          Quiet mode (no prompt) and quit after running the commands specified with -i or -c

     -Q          Same as q, but exiting without freeing RCore, this produces leaks at exit time, but saves some pre‐
                 cious ms to run the testsuite in fast mode.

     -p prj      Set project file

     -P file     Apply rapatch file and quit (see doc/rapatch.md for more details)

     -r rarun2   Specify dbg.profile rarun2 profile to use when spawning a program for debugging

     -R rarun2-directive
                 Specify custom rarun2 directives without having to create a rarun2 profile

     -s addr     Start seeking at this address

     -S          Enable sandboxed mode (same as -e cfg.sandbox=true)

     -t          Get binary information using a thread

     -u          Set bin.filter=false to load rbin info without filtering names

     -v          Show version information and exit (Use -qv to get just the version number)

     -V          Show radare2 library versions

     -w          Open in write mode

     -h          Show help message

     -H          Show files and environment help

     -x          Open the file map without executable permissions

     -X          Same as -e bin.usextr=false, do not use extract plugins, useful for dyldcache

SHELL
     Type '?' for help

VISUAL
     To enter visual mode use the 'V' command. Then press '?' for help

DEBUGGER
     In r2 the debugger commands are implemented under the 'd' command. Type 'd?' for help

ENVIRONMENT
      RHOMEDIR     ~/.config/radare2
      RCFILE       ~/.radare2rc (user preferences, batch script)
      MAGICPATH    /usr/lib/radare2/0.10.0-git/magic
      R_DEBUG      if defined, show error messages and crash signal
      VAPIDIR      path to extra vapi directory FILE path to the current working file.

SEE ALSO
     rahash2(1), rafind2(1), rabin2(1), radiff2(1), rasm2(1), rax2(1), ragg2(1), rarun2(1),

AUTHORS
     pancake <pancake@nopcode.org>

                                                     Aug 24, 2017

```



<p hidden>ar bfdbg bochs debug default gdb gzip http ihex mach malloc mmap null procpid ptrace qnx r2k r2pipe r2web rap rbuf self shm sparse tcp windbg winedbg zip</p>