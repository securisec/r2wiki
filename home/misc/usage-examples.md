<!-- TITLE: Usage Examples taken from the r2 git-->
# Usage examples
## Android

```text
r2 on android
=============
Install NDK in archlinux x86-64
 - Enable multilib repo in pacman.conf
 - pacman -S lib32-glibc lib32-zlib

To build r2 for android you need to install the NDK:

  http://developer.android.com/tools/sdk/ndk/index.html

Edit ~/.r2androidrc to setup the paths to your ndk

  sys/android-shell.sh
  ./configure --with-compiler=android --with-ostype=android --without-ssl --prefix=/data/radare2 --without-pic --with-nonpic --without-gmp
  make -j 4

To compile for android-x86

  export NDK_ARCH=x86

To package:

  mkdir 
  make install DESTDIR=/usr

Build farm

  See sys/android-shell.sh and sys/android-build.sh

  sys/android-shell.sh sys/android-build.sh arm-static


Environment:

   NDK_ARCH=arm|x86
   STATIC_BUILD=0|1
```

## avr

```text
AVR (arduino, atmega128, ..)
============================

Install JTAG serial driver:

	http://www.wch.cn/download/CH341SER_MAC_ZIP.html 

Install SDK from Arduino:

	https://www.arduino.cc/en/Main/Software
	echo 'PATH="/Applications/Arduino.app//Contents/Java/hardware/tools/avr/bin/:$PATH"' >> ~/.profile

Install avarice, the gdbserver <-> jtag:

	r2pm -i avarice

Run the proxy:

	r2pm -r avarice --jtag /dev/tty.wch* --mkI :4242

Using GDB:

	(avr-gdb) target remote :4242

In another terminal now run:

	r2 -a avr -d gdb://localhost:4242

NOTE: Right now the avr debugger is pretty broken, the memory and register reads result in in correct data.

```

## brainfuck

```text
Brainfuck support for r2
========================

Plugins for brainfuck:
  - asm.bf - brainfuck assembler and disassembler
  - debug.bf - debugger using bfvm
  - anal.bf - code analysis for brainfuck
  - bp.bf - breakpoints support (experimental)

To debug a brainfuck program:

$ r2 -D bf bfdbg:///tmp/bf

> dc    # continue
> x@scr # show screen buffer contents

The debugger creates virtual sections for code, data, screen and input.

TODO 
----
- add support for comments, ignore invalid instructions as nops
- enhance io and debugger plugins to generate sections and set arch opts

Hello World
===========
>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]
>++++++++[<++++>-] <.>+++++++++++[<++++++++>-]<-.--------.+++
.------.--------.[-]>++++++++[<++++>- ]<+.[-]++++++++++.

$ cat << EOF
>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-] <.>+++++++++++[<++++++++>-]<-.--------.+++.------.--------.[-]>++++++++[<++++>- ]<+.[-]++++++++++.
EOF
```

## Debug

```text
 Conditional breakpoints
=========================
conditional breakpoints are implemented in the following way:
- when a breakpoint is hit, the condition is run as a normal command
- if the command returns a value different from zero, execution continue,
- otherwise, execution is stopped at the breakpoint

 Examples of conditional breakpoints
======================================
1.) ignore breakpoint at address 0x4000ce for five times:
	f times=5
	(dec_times,f times=`?vi times-1`,?= times)
	db 0x4000ce
	dbC 0x4000ce .(dec_times)
	dc
2.) execute until rax==0x31c0 at address 0x4000ce
	e cmd.hitinfo=0
	(break_rax,f reg_rax=`dr rax`,f test=`?vi reg_rax-0x31c0`,?= test)
	db 0x4000ce
	dbC 0x4000ce .(break_rax)
	dc
3.) perform a register tracing dump at address 0x4000ce
	e cmd.hitinfo=0
	(trace_rax,dr rax,?= 1)
	db 0x4000ce
	dbC 0x4000ce .(trace_rax)
	dc > trace.txt
```

## esil


```text
ESIL
====

# source https://github.com/radare/radare2/wiki/ESIL

ESIL stands for 'Evaluable Strings Intermedate Language'. It aims to describe a Forth-like representation for every opcode. Those representations can be evaluated in order to emulate code. Each element of an esil expression is separated by a comma. The VM can be described as this:
---
   while ((word=haveCommand())) {
     if (word.isKeyword()) {
       esilCommands[word](esil);
     } else {
       esil.push (evaluateToNumber(word));
     }
     nextCommand();
   }
---
The esil commands are operations that pop values from the stack, performs some calculations and pushes the result in the stack (if any). They aim to cover all common operations done by CPUs, permitting to do binary operations, memory peeks and pokes, spawning a syscall, etc.

#### Use ESIL
---
[0x00000000]> e asm.esil = true
---

Syntax
======
An opcode is translated into a comma separated list of ESIL expressions.
---
xor eax, eax    ->    0,eax,=,1,zf,=
---
Memory access is defined by brackets.
---
mov eax, [0x80480]   ->   0x80480,[],eax,=
---
Default size is the destination of the operation. In this case 8bits, aka 1 byte.
---
movb $0, 0x80480     ->   0,0x80480,=[1]
---
Conditionals are expressed with the '?' char at the beginning of the expression. This checks if the rest of the expression is 0 or not and skips the next expression if doesn't matches. % is the prefix for internal vars.
---
cmp eax, 123  ->   123,eax,==,%z,zf,=
jz eax        ->   zf,?{,eax,eip,=,}
---
So.. if you want to run more than one expression under a conditional, you'll have to write it 
---
zf,?{,eip,esp,=[],eax,eip,=,%r,esp,-=,}
---

The whitespace, newlines and other chars are ignored in esil, so the first thing to do is:
---
esil = r_str_replace (esil, " ", "", true);
---
Syscalls are specially handled by '$' at the beginning of the expression. After that char you have an optional numeric value that specifies the number of syscall. The emulator must handle those expressions and 'simulate' the syscalls. (r_esil_syscall)

Order of arguments
==================
As discussed on irc, current implementation works like this:

---
a,b,-      b - a
a,b,/=     b /= a
---
This approach is more readable, but it's less stack-friendly

Special instructions
====================
NOPs are represented as empty strings. Unknown or invalid instructions

Syscalls are implemented with the '0x80,$' command. It delegates the execution of the esil vm into a callback that implements the syscall for a specific kernel.

Traps are implemented with the -<trap>,<code>,$$- command. They are used to throw exceptions like invalid instructions, division by zero, memory read error, etc.

Quick analysis
==============
Here's a list of some quick checks to retrieve information from an esil string. Relevant information will be probably found in the first expression of the list.
---
indexOf('[')       ->    have memory references
indexOf("=[")      ->    write in memory
indexOf("pc,=")    ->    modifies program counter (branch, jump, call)
indexOf("sp,=")    ->    modifies the stack (what if we found sp+= or sp-=?)
indexOf("=")       ->    retrieve src and dst
indexOf(":")       ->    unknown esil, raw opcode ahead
indexOf("%")       ->    accesses internal esil vm flags
indexOf("$")       ->    syscall
indexOf("$$")      ->    can trap
indexOf('++')      ->    has iterator
indexOf('--')      ->    count to zero
indexOf("?{")      ->    conditional
indexOf("LOOP")    ->    is a loop (rep?)
equalsTo("")       ->    empty string, means: nop (wrong, if we append pc+=x)
---

Common operations:
 * Check dstreg
 * Check srcreg
 * Get destinaion
 * Is jump
 * Is conditional
 * Evulate
 * Is syscall

CPU Flags
=========
CPU flags are usually defined as 1 bit registers in the RReg profile. and sometimes under the 'flg' register type.

ESIL Flags
==========
ESIL VM have an internal state flags that can are read only and can be used to export those values to the underlaying CPU flags. This is because the ESIL vm defines all the flag changes, while the CPUs only update the flags under certain conditions or specific instructions.

Those internal flags are prefixed by the '%' character.

---
z - zero flag, only set if the result of an operation is 0
b - borrow, this requires to specify from which bit (example: %b4 - checks if borrow from bit 4)
c - carry, same like above (example: %c7 - checks if carry from bit 7)
p - parity
r - regsize ( asm.bits/8 )
---

Variables
=========
1. No predefined bitness (should be easy to extend them to 128,256 and 512bits, e.g. for MMX, SSE, AVX, Neon)
2. Infinite number (for SSA-form compatibility)
3. Register names have no specific syntax. They are just strings
4. Numbers can be specified in any base supported by RNum (dec, hex, oct, binary ...)
5. Each ESIL backend should have an associated RReg profile to describe the esil register specs

Bitarrays
=========
What to do with them? What about bit arithmetics if use variables instead of registers?

Arithmetics
===========
1. ADD ("+")
2. MUL ("*")
3. SUB ("-")
4. DIV ("/")
5. MOD ("%")


Bit arithmetics
===============
1. AND  "&"
2. OR   "|"
3. XOR  "^"
4. SHL  "<<"
5. SHR  ">>"
6. ROL  "<<<"
7. ROR  ">>>"
8. NEG  "!"

Floating point
==============

_TODO_

The x86 REP prefix in ESIL
==========================
ESIL specifies that the parsing control-flow commands are in uppercase. Bear in mind that some archs have uppercase register names. The register profile should take care to not reuse any of the following:
---
3,SKIP   - skip N instructions. used to make relative forward GOTOs
3,GOTO   - goto instruction 3
LOOP     - alias for 0,GOTO
BREAK    - stop evaluating the expression
STACK    - dump stack contents to screen
CLEAR    - clear stack
---


Usage example:

rep cmpsb
---------
cx,!,?{,BREAK,},esi,[1],edi,[1],==,?{,BREAK,},esi,++,edi,++,cx,--,LOOP


Unimplemented/unhandled instructions
====================================
Those are expressed with the 'TODO' command. which acts as a 'BREAK', but displaying a warning message describing which instruction is not implemented and will not be emulated.

For example:
---
fmulp ST(1), ST(0)      =>      TODO,fmulp ST(1),ST(0)
---

Disassembly example:
====================
---
[0x1000010f8]> e asm.esil=true
[0x1000010f8]> pd $r @ entry0
   ;      [0] va=0x1000010f8 pa=0x000010f8 sz=13299 vsz=13299 rwx=-r-x 0.__text
            ;-- section.0.__text:
            0x1000010f8    55           8,rsp,-=,rbp,rsp,=[8]
            0x1000010f9    4889e5       rsp,rbp,=
            0x1000010fc    4883c768     104,rdi,+=
            0x100001100    4883c668     104,rsi,+=
            0x100001104    5d           rsp,[8],rbp,=,8,rsp,+=                                          ┌─< 0x100001105    e950350000   0x465a,rip,= ;[1]
        │   0x10000110a    55           8,rsp,-=,rbp,rsp,=[8]
        │   0x10000110b    4889e5       rsp,rbp,=                                                       │   0x10000110e    488d4668     rsi,104,+,rax,=
        │   0x100001112    488d7768     rdi,104,+,rsi,=
        │   0x100001116    4889c7       rax,rdi,=
        │   0x100001119    5d           rsp,[8],rbp,=,8,rsp,+=                                         ┌──< 0x10000111a    e93b350000   0x465a,rip,= ;[1]
       ││   0x10000111f    55           8,rsp,-=,rbp,rsp,=[8]
       ││   0x100001120    4889e5       rsp,rbp,=
       ││   0x100001123    488b4f60     rdi,96,+,[8],rcx,=
       ││   0x100001127    4c8b4130     rcx,48,+,[8],r8,=                                              ││   0x10000112b    488b5660     rsi,96,+,[8],rdx,=
       ││   0x10000112f    b801000000   1,eax,= ;  0x00000001
       ││   0x100001134    4c394230     rdx,48,+,[8],r8,==,cz,?=
      ┌───< 0x100001138    7f1a         sf,of,!,^,zf,!,&,?{,0x1154,rip,=,} ;[2]
     ┌────< 0x10000113a    7d07         of,!,sf,^,?{,0x1143,rip,} ;[3]
     ││││   0x10000113c    b8ffffffff   0xffffffff,eax,= ;  0xffffffff                              ┌─────< 0x100001141    eb11         0x1154,rip,= ;[2]
    │└────> 0x100001143    488b4938     rcx,56,+,[8],rcx,=
    │ │││   0x100001147    48394a38     rdx,56,+,[8],rcx,==,cz,?=
---

Radare anal ESIL code example
==============================

As an example implementation of ESIL analysis for the AVR family of microcontrollers there is
a -avr_op- function in -/libr/anal/p/anal_avr.c- which contains information on how the 
instructions are expressed in ESIL and other opcode information such as cycle counts per instruction:

static int avr_op(RAnal *anal, RAnalOp *op, ut64 addr, const ut8 *buf, int len) {
	  short ofst;
		  int d, r, k;
			(...)

Variables d, r and k refer to "destination", "register" and "(k)onstant", respectively. They
are used later on by ESIL string formatting function like for instance:

    r_strbuf_setf (&op->esil, "0x%x,r%d,=", k, d);

Which in this case corresponds to the LDI (LoaD with immediate) instruction in AVR. As an example,
the above ESIL string template will translate into the following when reversing in radare:

│           0x00000080      30e0           0x0,r19,=                   ; LDI Rd,K. load immediate

Or in non-ESIL format:

│           0x00000080      30e0           ldi r19, 0x00               ; LDI Rd,K. load immediate


Looking at other architectures which already have mature ESIL support such as x86 can help 
in understanding the syntax and conventions of radare's ESIL.


Introspection
=============
To ease esil parsing we should have a way to express introspection expressions to extract the data we want. For example. We want to get the target address of a jmp.

The parser for the esil expressions should be implemented in an API to make it possible to extract information by analyzing the expressions easily.

---
>  ao~esil,opcode
opcode: jmp 0x10000465a
esil: 0x10000465a,rip,=
---
We need a way to retrieve the numeric value of 'rip'. This is a very simple example, but there will be more complex, like conditional ones and we need expressions to get:

- opcode type
- destination of jump
- condition depends on
- all regs modified (write)
- all regs accessed (read)

API HOOKS
=========

It is important for emulation to be able to setup hooks in the parser, so we can extend the parser to implement the analysis without having to write the parser again and again. This is, every time an operation is going to be executed we call a user hook which can be used to determine if rip is changing or if the instruction updates the stack.
Later, at this level we can split that callback into several ones to have an event based analysis api that may be extended in js like this:
esil.on('regset', function(){..
esil.on('syscall', function(){esil.regset('rip'

we have already them. see hook_flag_read() hook_execute() hook_mem_read() ...

return true if you want to override the action taken for a callback. for example. avoid mem reads in a region or mem writes to make all memory read only.

return false or 0 if you want to trace esil expression parsing. aka emulation
..

Other operations that require bindings to external functionalities to work. In this case r_ref and r_io. This must be defined when initializing the esil vm.

* Io Get/Set
    Out ax, 44
    44,ax,:ou
* Selectors (cs,ds,gs...)
   Mov eax, ds:[ebp+8]
   Ebp,8,+,:ds,eax,=
```

## FLIRT

```text
FLIRT
=====
At the  moment of  writing r2  supports  loading  and finding  FLIRT
patterns, those files can be generated with the FLIRT tools from IDA.
R2 doesn't  yet supports creating  those files.  But it supports its
own signature format  which can be used  to generate signatures  and
find them.

This document will focus on FLIRT, not the native r2 'Zignatures'.

You need the flair tools/ida utilities. Those tools are closed source
and privative, so you should not distribute them. It is probable that
it is  not possible  to redistribute the  .pat or the .sig files.  It
doesn't  seems to  have watermarks.  However it's  a bit unclear  what
licence the file generated should have.  Mentioning the files should
be free of copyrighted material  (the original libs bytes). That said,
there's a paragraph in the flirt paper:

	https://www.hex-rays.com/products/ida/tech/flirt/in_depth.shtml


Create the .pat file
--------------------

	cd flair/bin/linux
	./pelf -p64 /usr/lib/x86_64-linux-gnu/libc.a libc.pat

Create the .sig file (possible collisions):
--------------------

	./sigmake -n <libname> libc.pat libc.sig

There's little chance libc.sig will  be compatible across systems and
libc versions. If libc.exc exists, you need to resolve some functions
conflicts.  Prepend a '+' on the lines  you're sure you  want to keep
(see end of flair/sigmake.txt).  Then redo the  sigmake command.  The
.sig is now ready to be used with r2.

Using it with r2:
-----------------

    $ r2 -c 'zF libc.sig' staticbin

PROFIT.

refs:
    flair/sigmake.txt
    flair/pat.txt

```

## gdb

```text
Connecting r2 with gdb
======================

Running gdbserver
-----------------
        $ gdbserver :2345 /bin/ls
        (gdb) target remote localhost:2345

Connecting from r2
------------------
        $ r2 -D gdb gdb://127.0.0.1:2345


Supported implementations
=========================
r2 have support for connecting to remote GDB instances:

                x86-32   x86-64   arm    arm64   sh
    winedbg       x        x       -      -      -
    qemu          x        x       ?      x      -
    gdbserver     x        x       ?      ?      ?

    x = supported
    ? = untested
    - = not supported

Supported Commands
------------------
- read/write memory

Writing or reading memory is implemented through the m/M packet.

- read registers

Reading registers is currently implemented through the <g> packet of the gdb protocol.
It returns the whole register profile at once. 

- write registers

There are two ways of writing registers. The first one is through the P packet.
It works like this: `P<register_index>=<register_value>`
The second one is the G packet, that writes the whole register Profile at once.
The implementation first tries to use the newer P packet and if it receives a $00# packet (that says not implemented), it tries to write through the G packet.

- stepping (but this is still the softstep mode and for an unknown reason it sill does not call th gdb_write_register function)

Supported Packets:
- g : Reads the whole register Profile at once
- G : Writes the whole register Profile at once
- m : Reads memory 
- M : Writes memory
- vCont,v : continues execution of the binary
- P : Write one register

TODO
----
- Implement GDBserver to allow other apps use r2 debugger 
- Fix that usese the gdb internal stepping version
- Fix softstep, that it finally recoils correct (it just have to reset the eip/rip)
- Add Breakpoints (should be an easy add of the function, because its already implemented in the gdb lib)

```

## IDA

```text
IDA
======

You can find conversion scripts to work between radare2 and IDA files (IDC, IDB...) in the repo:

* https://github.com/radare/radare2ida
```

## Macros

```text
 Examples of Macros
--------------------
NOTE: in radare2, do not add a space between the "," and the next
      command otherwise you are in for pain...

1.) Hello, world
(hello,?e Hello World)
.(hello)

2.) Looping inside a macro
(loop_macro,f cnt=3,loop:,?e hello `?vi cnt`,f cnt=`?vi cnt-1`,?= cnt,?!(),.loop:)
.(loop_macro)

Backtrace implementation for x86-64:
------------------------------------

(backtrace,
aa
f prev @ rsp
f base@ rbp
loop:
f next @ `pq 1 @base~[1]`,
f cont @ `pq 1 @base+8~[1]`,
?= next
??()
?= next-0xffffffffffffffff
??()
?= cont-0xffffffffffffffff
??()
?e StackFrame at `?v next` with size `?vi base-prev`
x base-prev@base+16
?e Code: `?v cont`
pdf @ cont
f prev@base
f base@next
.loop:
)
.(backtrace)
```


## pdb

```text
PDB usage
=========

- To get information about functions, structures, unions, enumerates etc:
----
rabin2 -P some_pdb_file
For example:
rabin2 -P Project1.pdb
...
TEST_STRUCT: size 0x8
	0x0: a type:(member) long
	0x4: b type:(member) long
TEST_ENUM: size 0x0
	0x10: eENUM1 type:enumerate eENUM1
	0x20: eENUM2 type:enumerate eENUM2
	0x21: eENUM_MAX type:enumerate eENUM_MAX
TEST_UNION: size 0x4
	0x0: union_var_1 type:(member) long
	0x0: union_var_2 type:(member) long
TEST_STRUCT: size 0x8
	0x0: struct_var_1 type:(member) long
	0x4: struct_var_2 type:(member) long
{"gvars":[0x00001000  0  .textbss  __enc$textbss$begin
0x00011000  0  .textbss  __enc$textbss$end
0x000192c8  0  .idata  __imp__printf
0x000192c0  0  .idata  __imp__system
0x000113e0  2  .text  ?test_func@@YAHHH@Z
...
----

- To display all mentioned above information in json format:
----
rabin2 -Pj some_pdb_file
----

- To export information about types, functions:
----
rabin2 -Pr some_pdb_file
For example:
rabin2 -P Project1.pdb
...
pf TEST_STRUCT ii a b
"td enum TEST_ENUM eENUM1=00000010,eENUM2=00000020,eENUM_MAX=00000021 };"
pf TEST_UNION ii union_var_1 union_var_2
pf TEST_STRUCT ii struct_var_1 struct_var_2
f pdb.__enc_textbss_begin = 0x1000 # 0 .textbss
f pdb.__enc_textbss_end = 0x11000 # 0 .textbss
f pdb.__imp__printf = 0x192c8 # 0 .idata
f pdb.__imp__system = 0x192c0 # 0 .idata
f pdb._test_func__YAHHH_Z = 0x113e0 # 2 .text
...
Check out this post for more information about pf: http://radare.today/types/
----

- To download PDB file for some binary (.exe, .dll):
----
rabin2 -PP path_to_binary
For example:
rabin2 -PP ~/Downloads/libs/user32.dll
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current Dload  Upload   Total   Spent    Left  Speed
100  336k  100  336k    0     0  34388      0  0:00:10  0:00:10 --:--:-- 38385
Extracting cabinet: /home/inisider/Downloads/libs/user32.pd_
extracting /home/inisider/Downloads/libs/user32.pdb
All done, no errors.
----
The following dependencies are required for PDB downloader:
* curl
* cabextract (non-Windows only, optional)
```


## RAP Remote Access Protocol

```text
RAP protocol
============

RAP stands for the Remote Access Protocol of Radare2, it is compatible with radare1
and it simply defines a communication between a client and a server to simulate IO
operations.

There are two different implementations, one in C and another in Python.

Usage example
-------------

Start in one terminal the following command to wait for incoming connections:

	r2 rap://:9999

In another machine or terminal connect it:

	r2 rap://localhost:9999//bin/ls

As you see, the path of the remote file to load must be specified, and this handled
by the open() packet.

Known Bugs
----------

* Read/Write operations ignore the filedescriptor completely because it is supposed to be handled by the IO layer and it is redundant, but it introduces a bug that breaks support for multiple files.
* This can be fixed with a new packet type RAP_SETFD.
* Read lengths should be only 2 bytes, there's no sense in read > 64K of memory in a shot.
* Seek does not returns anything
* System vs Cmd - the first should have a return value as well as string result
* Filedescriptors are assumed to be 32bit


Operations
----------

The protocol is designed to be bidirectional, but right now, only one way is supported.
The client sends a byte specifying the operation and the server will reply the same byte
masked with the RMT_REPLY value (0x80 | op)

	RAP_OPEN   = 1
	RAP_READ   = 2
	RAP_WRITE  = 3
	RAP_SEEK   = 4
	RAP_CLOSE  = 5
	RAP_SYSTEM = 6
	RAP_CMD    = 7
	RAP_REPLY  = 0x80

This is how are constructed the packets:

	RAP_OPEN
		struct packed RapOpen {
			ut8 op = 1;
			ut8 rw = 0; // 0 = read-only, 1 = read-write
			ut8 len = 15; // length of filename
		}
		>> 01 RW LN [....]
		<< 81 FD=(.. .. .. ..)

	RAP_READ
		>> 02 LN=(.. .. .. ..)
		<< 82 LN=(.. .. .. ..) [..LN..]

	RAP_WRITE
		>> 03 LN=(.. .. .. ..) [..LN..]
		<< 83 LN=(.. .. .. ..)

	RAP_SEEK
		>> 04 FLAG=(..) OFFSET=(.. 8 bytes ..)
		<< 84

	RAP_CLOSE
		>> 05 FD=(4 bytes) 
		<< 85 RET=(4 bytes)

	RAP_SYSTEM
		>> 06 LEN=(4 bytes) STR[LEN bytes]
		<< 86 LN=(.. .. .. ..) STR[ LEN bytes]

	RAP_CMD_
		>> 07 LEN=(4 bytes) STR[LEN bytes]
		<< 87 LN=(.. .. .. ..) STR[ LEN bytes]


Examples
--------

Python:

	See radare2-bindings/python/remote.py and test-rap-*.py

C:

	Server: libr/socket/rap_server.c
	Client: libr/io/p/io_rap.c
```

## Strings

```text
Loading strings from binaries
=============================

TODO: explain bin.minstr

Config vars
-----------
bin.strings  =  [true]  - load strings from file
bin.rawstr   =  [false] - load strings from unknown rbin

Program args
------------
rabin2 -z   # list strings
rabin2 -zz  # list strings from raw binary (unknown rbin type)

Examples
--------

r2 -e bin.rawstr=true
r2 -z   # do not load strings (same as bin.strings=false)
r2 -zz  # load strings even if unknown bin (same as bin.rawstr=true)
r2 -n   # do not load symbols or anything
r2 -e bin.strings=false # load symbols but not strings
if (bin.strings) {
  if RBin.format(isKnown) {
    loadStrings()
  } else {
    if (bin.rawstr)
      loadStrings()
  }
}

```

## Types
[Types](https://github.com/radare/radare2/blob/master/doc/types.md)

## windbg

```text
WinDBG
======

The WinDBG support for r2 allows you to attach to VM running Windows
using a named socket file (will support more IOs in the future) to
debug a windows box using the KD interface over serial port.

Bear in mind that WinDBG support is still work-in-progress, and this is
just an initial implementation which will get better in time.

It is also possible to use the remote GDB interface to connect and
debug Windows kernels without depending on Windows capabilities.

------8<--------------8<------------------8<------------------------

Enable WinDBG support on Windows Vista and higher like this:

    bcdedit /debug on
    bcdedit /dbgsettings serial debugport:1 baudrate:115200

Or like this for Windows XP:
    Open boot.ini and add /debug /debugport=COM1 /baudrate=115200:

    [boot loader]
    timeout=30
    default=multi(0)disk(0)rdisk(0)partition(1)\WINDOWS
    [operating systems]
    multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Debugging with Cable" /fastdetect /debug /debugport=COM1 /baudrate=57600


Configure the VirtualBox Machine like this:

    Preferences -> Serial Ports -> Port 1

    [V] Enable Serial Port
    Port Number: [_COM1_______[v]]
    Port Mode:   [_Host_Pipe__[v]]
                 [v] Create Pipe
    Port/File Path: [_/tmp/windbg.pipe____]

Or just spawn the VM with qemu like this:

    $ qemu-system-x86_64 -chardev socket,id=serial0,\
           path=/tmp/windbg.pipe,nowait,server \
           -serial chardev:serial0 -hda Windows7-VM.vdi


Radare2 will use the 'windbg' io plugin to connect to a socket file
created by virtualbox or qemu. Also, the 'windbg' debugger plugin and
we should specify the x86-32 too. (32 and 64 bit debugging is supported)

    $ r2 -a x86 -b 32 -D windbg windbg:///tmp/windbg.pipe

On Windows you should run the following line:

    $ radare2 -D windbg windbg://\\.\pipe\com_1

At this point, we will get stuck here:

    [0x828997b8]> pd 20
           ;-- eip:
           0x828997b8    cc           int3
           0x828997b9    c20400       ret 4
           0x828997bc    cc           int3
           0x828997bd    90           nop
           0x828997be    c3           ret
           0x828997bf    90           nop

In order to skip that trap we will need to change eip and run 'dc' twice:

    dr eip=eip+1
    dc
    dr eip=eip+1
    dc

Now the Windows VM will be interactive again. We will need to kill r2 and
attach again to get back to control the kernel.

In addition, the `dp` command can be used to list all processes, and
`dpa` or `dp=` to attach to the process. This will display the base
address of the process in the physical memory layout.
```

