<!-- TITLE: rasm2 -->

# rasm2

## **Tips**
  - The `a` or the `d` in `rasm2 -L` signifies assember, disassembler or both
## Help

      Usage: rasm2 [-ACdDehLBvw] [-a arch] [-b bits] [-o addr] [-s syntax]
       [-f file] [-F fil:ter] [-i skip] [-l len] 'code'|hex|-
       -a [arch] Set architecture to assemble/disassemble (see -L)
       -A Show Analysis information from given hexpairs
       -b [bits] Set cpu register size (8, 16, 32, 64) (RASM2_BITS)
       -B Binary input/output (-l is mandatory for binary input)
       -c [cpu] Select specific CPU (depends on arch)
       -C Output in C format
       -d, -D Disassemble from hexpair bytes (-D show hexpairs)
       -e Use big endian instead of little endian
       -E Display ESIL expression (same input as in -d)
       -f [file] Read data from file
       -F [in:out] Specify input and/or output filters (att2intel, x86.pseudo, ...)
       -h, -hh Show this help, -hh for long
       -i [len] ignore/skip N bytes of the input buffer
       -j output in json format
       -k [kernel] Select operating system (linux, windows, darwin, ..)
       -l [len] Input/Output length
       -L List Asm plugins: (a=asm, d=disasm, A=analyze, e=ESIL)
       -o [offset] Set start address for code (default 0)
       -O [file] Output file name (rasm2 -Bf a.asm -O a)
       -p Run SPP over input for assembly
       -q quiet mode
       -r output in radare commands
       -s [syntax] Select syntax (intel, att)
       -v Show version information
       -w What's this instruction for? describe opcode
       If '-l' value is greater than output length, output is padded with nops
       If the last argument is '-' reads from stdin

## rasm2 -L (list of valid architectures)
  > A list of valid architectures can also be obtained using `e asm.arch=?` {.is-info}
	
	
  ```text
_dAe  8 16       6502        LGPL3   6502/NES/C64/Tamagotchi/T-1000 CPU
_dA_  8          8051        PD      8051 Intel CPU
_dA_  16 32      arc         GPL3    Argonaut RISC Core
a___  16 32 64   arm.as      LGPL3   as ARM Assembler (use ARM_AS environment)
adAe  16 32 64   arm         BSD     Capstone ARM disassembler
_dA_  16 32 64   arm.gnu     GPL3    Acorn RISC Machine CPU
_d__  16 32      arm.winedbg LGPL2   WineDBG's ARM disassembler
adAe  8 16       avr         GPL     AVR Atmel
adAe  16 32 64   bf          LGPL3   Brainfuck (by pancake, nibble) v4.0.0
_dA_  32         chip8       LGPL3   Chip8 disassembler
_dA_  16         cr16        LGPL3   cr16 disassembly plugin
_dA_  32         cris        GPL3    Axis Communications 32-bit embedded processor
adA_  32 64      dalvik      LGPL3   AndroidVM Dalvik
ad__  16         dcpu16      PD      Mojang's DCPU-16
_dA_  32 64      ebc         LGPL3   EFI Bytecode
adAe  16         gb          LGPL3   GameBoy(TM) (z80-like)
_dAe  16         h8300       LGPL3   H8/300 disassembly plugin
_d__  32         hexagon     GPL3    Qualcomm DSPv5
_d__  32         hppa        GPL3    HP PA-RISC
_dAe             i4004       LGPL3   Intel 4004 microprocessor
_dA_  8          i8080       BSD     Intel 8080 CPU
adA_  32         java        Apache  Java bytecode
_d__  32         lanai       GPL3    LANAI
_d__  8          lh5801      LGPL3   SHARP LH5801 disassembler
_d__  32         lm32        BSD     disassembly plugin for Lattice Micro 32 ISA
_d__  16 32      m68k        BSD     Capstone M68K disassembler
_dA_  32         malbolge    LGPL3   Malbolge Ternary VM
_d__  16         mcs96       LGPL3   condrets car
adAe  16 32 64   mips        BSD     Capstone MIPS disassembler
adAe  32 64      mips.gnu    GPL3    MIPS CPU
_dA_  16         msp430      LGPL3   msp430 disassembly plugin
_dA_  32         nios2       GPL3    NIOS II Embedded Processor
_dAe  8          pic18c      LGPL3   pic18c disassembler
_dAe  32 64      ppc         BSD     Capstone PowerPC disassembler
_dA_  32 64      ppc.gnu     GPL3    PowerPC
_d__  32         propeller   LGPL3   propeller disassembly plugin
_dA_  32 64      riscv       GPL     RISC-V
_dAe  32         rsp         LGPL3   Reality Signal Processor
_dA_  32         sh          GPL3    SuperH-4 CPU
_dA_  8 16       snes        LGPL3   SuperNES CPU
_dAe  32 64      sparc       BSD     Capstone SPARC disassembler
_dA_  32 64      sparc.gnu   GPL3    Scalable Processor Architecture
_d__  16         spc700      LGPL3   spc700, snes' sound-chip
_d__  32         sysz        BSD     SystemZ CPU disassembler
_dA_  32         tms320      LGPLv3  TMS320 DSP family (c54x,c55x,c55x+,c64x)
_d__  32         tricore     GPL3    Siemens TriCore CPU
_dAe  32         v810        LGPL3   v810 disassembly plugin
_dAe  32         v850        LGPL3   v850 disassembly plugin
_dAe  8 32       vax         GPL     VAX
ad__  32         wasm        MIT     WebAssembly (by cgvwzq) v0.1.0
_dA_  32         ws          LGPL3   Whitespace esotheric VM
a___  16 32 64   x86.as      LGPL3   Intel X86 GNU Assembler
_dAe  16 32 64   x86         BSD     Capstone X86 disassembler
a___  16 32 64   x86.nasm    LGPL3   X86 nasm assembler
a___  16 32 64   x86.nz      LGPL3   x86 handmade assembler
_dAe  16 32 64   x86.udis    BSD     udis86 x86-16,32,64
_dA_  16         xap         PD      XAP4 RISC (CSR)
_dA_  32         xcore       BSD     Capstone XCore disassembler
_dAe  32         xtensa      GPL3    XTensa CPU
adA_  8          z80         GPL     Zilog Z80
```

## rasm2 man page

```text
RASM2(1)                                     BSD General Commands Manual                                     RASM2(1)

NAME
     rasm2 — radare2 assembler and disassembler tool

SYNOPSIS
     rasm2 [-ABdDeEfCLvwrq] [-a arch] [-b bits] [-c cpu] [-F in:out] [-o offset] [-O ofile] [-s syntax] [-i int]
           [-l int] [ARG]

DESCRIPTION
     This tool uses r_asm to assemble and disassemble files or hexpair strings. It supports a large list of architec‐
     tures which can be listed using the -L flag.

     -a arch     Set architecture plugin

     -A          Show analysis information of given hexpair string

     -b bits     Set architecture bits

     -B          Binary input/output (-l is mandatory for binary input)

     -c cpu      Select specific CPU (depends on -a arch)

     -C          Output in C format

     -d          Disassemble hexpair bytes. rasm2 -d 9090

     -D          Disassemble showing hexpair and opcode

     -e          Use big endian (or swap endianness if used more than once)

     -E          Output disassembled instructions in ESIL format.

     -f          Read data from file instead of ARG.

     -F in:out   Specify input and/or output filters (att2intel, x86.pseudo, ...)

     -h          Show usage help message.

     -hh         Show long help message including supported assembler directives

     -l int      Input/Output length

     -i int      Ignore/skip N bytes from the beginning of the input buffer

     -L          List supported asm plugins

     -o offset   Offset of the opcode to assemble (default is 0)

     -O ofile    output to file, for example 'rasm2 -BF a a.asm'

     -r          Show output in r2 script

     -s syntax   Select syntax output (intel, att)

     -w          Describe opcode (whats op)

     -q          Quiet output (handy for -L, -v, ...)

different than filename
     -.intel_syntax
                 Use intel syntax rather than att:w

     -.att_syntax
                 Use ATT syntax rather than flu :w dentify the region fof aslerrger

     -string     dentify the region fof aslerrger

     -.ascii

     -.align

     -.arm

     -.thumb

     -.arch

     -.bits

     -.fill

     -.kernel

     -.os

     -.hex

     -.int16

     -.short

     -.int32

     -.int64

     -.glob

     -.equ

     -.org

     -.text

     -.data

EXAMPLES
     Assemble opcode:

       $ rasm2 -a x86 -b 32 'mov eax, 33'

     Disassemble opcode:

       $ rasm2 -d 90

SEE ALSO
     radare2(1), rafind2(1), rahash2(1), rabin2(1), radiff2(1), ragg2(1), rarun2(1), rax2(1),

AUTHORS
     pancake <pancake@nopcode.org>

                                                     Sep 30, 2014

```




<p hidden>6502/NES/C64/Tamagotchi/T-1000 CPU 8051 Intel CPU Argonaut RISC Core as ARM Assembler (use ARM_AS environment) Capstone ARM disassembler Acorn RISC Machine CPU WineDBG's ARM disassembler AVR Atmel Brainfuck (by pancake, nibble) v4.0.0 Chip8 disassembler cr16 disassembly plugin Axis Communications 32-bit embedded processor AndroidVM Dalvik Mojang's DCPU-16 EFI Bytecode GameBoy(TM) (z80-like) H8/300 disassembly plugin Qualcomm DSPv5 HP PA-RISC Intel 4004 microprocessor Intel 8080 CPU Java bytecode LANAI SHARP LH5801 disassembler disassembly plugin for Lattice Micro 32 ISA Capstone M68K disassembler Malbolge Ternary VM condrets car Capstone MIPS disassembler MIPS CPU msp430 disassembly plugin NIOS II Embedded Processor pic18c disassembler Capstone PowerPC disassembler PowerPC propeller disassembly plugin RISC-V Reality Signal Processor SuperH-4 CPU SuperNES CPU Capstone SPARC disassembler Scalable Processor Architecture spc700, snes' sound-chip SystemZ CPU disassembler TMS320 DSP family (c54x,c55x,c55x+,c64x) Siemens TriCore CPU v810 disassembly plugin v850 disassembly plugin VAX WebAssembly (by cgvwzq) v0.1.0 Whitespace esotheric VM Intel X86 GNU Assembler Capstone X86 disassembler X86 nasm assembler x86 handmade assembler udis86 x86-16,32,64 XAP4 RISC (CSR) Capstone XCore disassembler XTensa CPU Zilog Z80</p>