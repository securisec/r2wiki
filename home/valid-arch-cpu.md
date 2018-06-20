<!-- TITLE: Valid Arch Cpu -->

# Valid architecture and cpu
## rasm2 -L (list of valid architectures and bits)
  - > A list of valid architectures can also be obtained using `e asm.arch=?` 
	
	
  ```
_dAe  8 16       6502        LGPL3   6502/NES/C64/Tamagotchi/T-1000 CPU
_dAe  8          8051        PD      8051 Intel CPU
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
_dAe  32         hexagon     LGPL3   Qualcomm Hexagon (QDSP6) V6
_d__  32         hppa        GPL3    HP PA-RISC
_dAe             i4004       LGPL3   Intel 4004 microprocessor
_dA_  8          i8080       BSD     Intel 8080 CPU
adA_  32         java        Apache  Java bytecode
_d__  32         lanai       GPL3    LANAI
_d__  8          lh5801      LGPL3   SHARP LH5801 disassembler
_d__  32         lm32        BSD     disassembly plugin for Lattice Micro 32 ISA
_dA_  16 32      m68k        BSD     Capstone M68K disassembler
_dA_  32         malbolge    LGPL3   Malbolge Ternary VM
_d__  16         mcs96       LGPL3   condrets car
adAe  16 32 64   mips        BSD     Capstone MIPS disassembler
adAe  32 64      mips.gnu    GPL3    MIPS CPU
_dA_  16         msp430      LGPL3   msp430 disassembly plugin
_dA_  32         nios2       GPL3    NIOS II Embedded Processor
_dAe  8          pic         LGPL3   PIC disassembler
_dAe  32 64      ppc         BSD     Capstone PowerPC disassembler
_dA_  32 64      ppc.gnu     GPL3    PowerPC
_d__  32         propeller   LGPL3   propeller disassembly plugin
_dA_  32 64      riscv       GPL     RISC-V
_dAe  32         rsp         LGPL3   Reality Signal Processor
_dAe  32         sh          GPL3    SuperH-4 CPU
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
adA_  32         wasm        MIT     WebAssembly (by cgvwzq) v0.1.0
_dA_  32         ws          LGPL3   Whitespace esotheric VM
a___  16 32 64   x86.as      LGPL3   Intel X86 GNU Assembler
_dAe  16 32 64   x86         BSD     Capstone X86 disassembler
a___  16 32 64   x86.nasm    LGPL3   X86 nasm assembler
a___  16 32 64   x86.nz      LGPL3   x86 handmade assembler
_dA_  16         xap         PD      XAP4 RISC (CSR)
_dA_  32         xcore       BSD     Capstone XCore disassembler
_dAe  32         xtensa      GPL3    XTensa CPU
adA_  8          z80         GPL     Zilog Z80
```

# CPU types
## arm
- v8
- cortex

## avr
- ATmega8
- ATmega1280
- ATmega1281
- ATmega168
- ATmega2560
- ATmega2561
- ATmega328p
- ATmega32u4
- ATmega48
- ATmega640
- ATmega88
- ATxmega128a4u

## cris
- v10
- v32
- v10+v32

## m68k

- 68000
- 68010
- 68020
- 68030
- 68040
- 68060

## mc6809
- `r2pm -i mc6809`
- `r2 -a mc6809`

## mips
- mips32/64
- micro
- r6
- v3
- v2

## ppc
- ppc
- vle
- ps

## sparc
- v9

## tms320
- c54x
- c55x
- c55x+
- c64x






<p hidden>6502/NES/C64/Tamagotchi/T-1000 CPU 8051 Intel CPU Argonaut RISC Core as ARM Assembler (use ARM_AS environment) Capstone ARM disassembler Acorn RISC Machine CPU WineDBG's ARM disassembler AVR Atmel Brainfuck (by pancake, nibble) v4.0.0 Chip8 disassembler cr16 disassembly plugin Axis Communications 32-bit embedded processor AndroidVM Dalvik Mojang's DCPU-16 EFI Bytecode GameBoy(TM) (z80-like) H8/300 disassembly plugin Qualcomm DSPv5 HP PA-RISC Intel 4004 microprocessor Intel 8080 CPU Java bytecode LANAI SHARP LH5801 disassembler disassembly plugin for Lattice Micro 32 ISA Capstone M68K disassembler Malbolge Ternary VM condrets car Capstone MIPS disassembler MIPS CPU msp430 disassembly plugin NIOS II Embedded Processor pic18c disassembler Capstone PowerPC disassembler PowerPC propeller disassembly plugin RISC-V Reality Signal Processor SuperH-4 CPU SuperNES CPU Capstone SPARC disassembler Scalable Processor Architecture spc700, snes' sound-chip SystemZ CPU disassembler TMS320 DSP family (c54x,c55x,c55x+,c64x) Siemens TriCore CPU v810 disassembly plugin v850 disassembly plugin VAX WebAssembly (by cgvwzq) v0.1.0 Whitespace esotheric VM Intel X86 GNU Assembler Capstone X86 disassembler X86 nasm assembler x86 handmade assembler udis86 x86-16,32,64 XAP4 RISC (CSR) Capstone XCore disassembler XTensa CPU Zilog Z80 mc6809</p>
