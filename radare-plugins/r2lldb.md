<!-- TITLE: r2lldb -->

# Github README r2lldb

`radare2-(lldb|gdb) integration`

Description
-----------

This repository contains all the necessary scripts required to debug
and manipulate anything running behind an LLDB the LLVM debugger from
an interactive radare2 session.

It has been developed for debugging iOS applications running on non
jailbroken devices. And it has been tested on arm32, arm64, i386
(simulator), and real OSX applications (x86-64).

The `debugserver` required to debug on jailbroken devices can be
obtained by using the `viatools/salvarez/ios-debugserver` repository.

In theory it shuold be possible to use r2lldb on Linux and debug
Android devices running gdbserver, but this hasn't been tested yet.

Features
--------

This is the list of features that r2lldb brings:

* Debug self-signed apps non-jailbroken devices with a low level debugger
* Trace calls to any address in memory
* Show backtrace
* List symbols
* List memory regions allocated
* List ObjC classes (using code injection)
* Inject dynamic libraries
* Step-in/over in r2's Visual mode
* Set breakpoints on objc methods
* Change process environment variables
* Run r2 commands on every traced breakpoint

Local example
-------------

Using r2 as a frontend for local lldb is as easy as this:

	$ r2lldb /bin/ls

Then in another terminal:

	$ r2lldb -R localhost:9999

The same syntax applies to remote connections or crossplatform ones.


Example
-------
Start with `XCode` or `ios-deploy` an lldb session in the target process and type:

	(lldb) script del sys.modules["r2lldb"]  # force module reload
	(lldb) script import r2lldb              # start r2rap server


Another Example
---------------

Target:

	$ r2lldb -l 1234 /bin/ls

	or

	$ while : ; do debugserver *:1234 /bin/ls ; done
	Listening to port 1234 for a connection from *...
	Got a connection, launched process /bin/ls (pid = 82363).

Host: Terminal 1

	$ r2lldb -c :1234

	$ while : ; do lldb -s lldb/local ; done
	Listening for r2rap connections at port 9999

Host: Terminal 2

	$ r2lldb -r ios localhost:9999

	or

	$ r2 -i r2/ios rap://localhost:9999//

r2lldb's help from r2
---------------------

	[0x00000000]> =!?
	Usage: =![cmd] ...       # r2lldb integration
	=!?                      # show r2lldb's help (this one)
	=!help                   # show lldb's help
	=!i                      # target information
	=!is                     # list symbols
	=!dfv                    # show frame variables (arguments + locals)
	=!up,down,list           # lldb's command to list select frames and show source
	=!dks                    # stop debugged process
	=!dm                     # show maps (image list)
	=!dr                     # show registers
	=!dra                    # show all registers
	=!dr*                    # "" "" in r2 commands
	=!dr-*                   # remove all breakpoints
	=!db                     # list breakpoints
	=!db 0x12924             # set breakpoint at address
	=!db objc_msgSend        # set breakpoint on symbol
	=!dbo NSString init:     # set objc breakpoint
	=!dbt                    # show backtrace
	=!ds                     # step
	=!dcue                   # continue until entrypoint
	=!dso                    # step over
	=!dt                     # list all trace points
	=!dt 0x804040 =!dr       # add tracepoint for this address
	=!dc                     # continue
	=!dct                    # continue with tracing
	=!env                    # show process environment
	=!objc                   # list all objc classes
	=!setenv k v             # set variable in target process
	=!dlopen /path/to/lib    # dlopen lib (libr2.so, frida?)

GDB notes
---------

Recently, this project got the ability to use `gdb` as target for r2,
so the project name will probably change to make this clear.

In order to run r2lldb in `ndk-gdb` you may do the following:

	$ prebuilt/darwin-x86_64/bin/gdb
	(gdb) python-interactive
	>>> import sys
	>>> sys.path.append('/path/to/r2lldb')
	>>> sys.path.append('/path/to/r2lldb/r2lldb')
	>>> sys.path.append('/path/to/r2lldb/r2lldb/backend/gdb/')
	>>> sys.path.append('/path/to/radare2-r2pipe/python/')
	>>> import r2lldb

In another terminal:

	$ r2 rap://localhost:9999

Android
-------

To debug Android apps in the target device you will need to find a copy of the `gdbserver` binary. which can be found in Termux if you install the `gdb` package, but also, it can be found inside the NDK under the `prebuilt/` directory.

iOS
---

The `debugserver` is deployed by XCode in the debugger image. If you have a jailbroken device you can just extract this binary from the dmg and copy it via SSH.

--pancake

# github
[r2lldb](https://github.com/nowsecure/r2lldb)

# Misc
[gdb vs lldb cheat sheet](https://kapeli.com/cheat_sheets/LLDB_to_GDB_Command_Map.docset/Contents/Resources/Documents/index)