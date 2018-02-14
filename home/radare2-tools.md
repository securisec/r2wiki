<!-- TITLE: radare2 tools -->
# Radare2 tools

## Command line tools

  [r2agent](/tools/r2agent)

  [r2pm (radare2 package manager)](/tools/r2pm)

  [rabin2](/tools/rabin2)

  [radare2](/tools/radare2)

  [radiff2](/tools/radiff2)

  [rafind2](/tools/rafind2)

  [ragg2](/tools/ragg2)

  [rahash2](/tools/rahash2)

  [rarun2](/tools/rarun2)

  [rasm2](/tools/rasm2)

  [rax2](/tools/rax2)

---

## Valid architectures 
   [radare](http://rada.re/r/arch.html)
   - `rasm2 -L`

      
```
			_dAe 8 16 6502 LGPL3 6502/NES/C64/Tamagotchi/T-1000 CPU
      _dA_ 8 8051 PD 8051 Intel CPU
      _dA_ 16 32 arc GPL3 Argonaut RISC Core
      a___ 16 32 64 arm.as LGPL3 as ARM Assembler (use ARM_AS environment)
      adAe 16 32 64 arm BSD Capstone ARM disassembler
      _dA_ 16 32 64 arm.gnu GPL3 Acorn RISC Machine CPU
      _d__ 16 32 arm.winedbg LGPL2 WineDBG's ARM disassembler
      adAe 8 16 avr GPL AVR Atmel
      adAe 16 32 64 bf LGPL3 Brainfuck (by pancake, nibble) v4.0.0
      _dA_ 16 cr16 LGPL3 cr16 disassembly plugin
      _dA_ 32 cris GPL3 Axis Communications 32-bit embedded processor
      adA_ 32 64 dalvik LGPL3 AndroidVM Dalvik
      ad__ 16 dcpu16 PD Mojang's DCPU-16
      _dA_ 32 64 ebc LGPL3 EFI Bytecode
      adAe 16 gb LGPL3 GameBoy(TM) (z80-like)
      _dAe 16 h8300 LGPL3 H8/300 disassembly plugin
      _d__ 32 hexagon GPL3 Qualcomm DSPv5
      _d__ 32 hppa GPL3 HP PA-RISC
      _dAe i4004 LGPL3 Intel 4004 microprocessor
      _dA_ 8 i8080 BSD Intel 8080 CPU
      adA_ 32 java Apache Java bytecode
      _d__ 32 lanai GPL3 LANAI
      _d__ 8 lh5801 LGPL3 SHARP LH5801 disassembler
      _d__ 32 lm32 BSD disassembly plugin for Lattice Micro 32 ISA
      _d__ 16 32 m68k BSD Capstone M68K disassembler
      _dA_ 32 malbolge LGPL3 Malbolge Ternary VM
      _d__ 16 mcs96 LGPL3 condrets car
      adAe 16 32 64 mips BSD Capstone MIPS disassembler
      adAe 32 64 mips.gnu GPL3 MIPS CPU
      _dA_ 16 msp430 LGPL3 msp430 disassembly plugin
      _dA_ 32 nios2 GPL3 NIOS II Embedded Processor
      _dAe 8 pic18c LGPL3 pic18c disassembler
      _dAe 32 64 ppc BSD Capstone PowerPC disassembler
      _dA_ 32 64 ppc.gnu GPL3 PowerPC
      _dA_ 32 64 riscv GPL RISC-V
      _dAe 32 rsp LGPL3 Reality Signal Processor
      _dA_ 32 sh GPL3 SuperH-4 CPU
      _dA_ 8 16 snes LGPL3 SuperNES CPU
      _dAe 32 64 sparc BSD Capstone SPARC disassembler
      _dA_ 32 64 sparc.gnu GPL3 Scalable Processor Architecture
      _d__ 16 spc700 LGPL3 spc700, snes' sound-chip
      _d__ 32 sysz BSD SystemZ CPU disassembler
      _dA_ 32 tms320 LGPLv3 TMS320 DSP family (c54x,c55x,c55x+,c64x)
      _d__ 32 tricore GPL3 Siemens TriCore CPU
      _dAe 32 v810 LGPL3 v810 disassembly plugin
      _dAe 32 v850 LGPL3 v850 disassembly plugin
      _dAe 8 32 vax GPL VAX
      ad__ 32 wasm MIT WebAssembly (by cgvwzq) v0.1.0
      _dA_ 32 ws LGPL3 Whitespace esotheric VM
      a___ 16 32 64 x86.as LGPL3 Intel X86 GNU Assembler
      _dAe 16 32 64 x86 BSD Capstone X86 disassembler
      a___ 16 32 64 x86.nasm LGPL3 X86 nasm assembler
      a___ 16 32 64 x86.nz LGPL3 x86 handmade assembler
      _dAe 16 32 64 x86.udis BSD udis86 x86-16,32,64
      _dA_ 16 xap PD XAP4 RISC (CSR)
      _dA_ 32 xcore BSD Capstone XCore disassembler
      _dAe 32 xtensa GPL3 XTensa CPU
      adA_ 8 z80 GPL Zilog Z80
      _d__ 32 propeller LGPL3 propeller disassembly plugin
```


## Valid file formats supported 
   - `rabin2 -L`

  [radare](http://rada.re/r/fileformat.html)

      bin any Dummy format r_bin plugin (LGPL3) 
      bin art Android Runtime (LGPL3) 
      bin avr ATmel AVR MCUs (LGPL3) 
      bin bf brainfuck (LGPL3) 
      bin bflt bFLT format r_bin plugin (LGPL3) 
      bin bios BIOS bin plugin (LGPL) 
      bin bootimg Android Boot Image (LGPL3) 
      bin cgc CGC format r_bin plugin (LGPL3) 
      bin coff COFF format r_bin plugin (LGPL3) 
      bin dex dex format bin plugin (LGPL3) 
      bin dol Nintendo Dolphin binary format (BSD) 
      bin dyldcache dyldcache bin plugin (LGPL3) 
      bin elf ELF format r2 plugin (LGPL3) 
      bin elf64 elf64 bin plugin (LGPL3) 
      bin fs filesystem bin plugin (LGPL3) 1.0 pancake
      bin java java bin plugin (LGPL3) 
      bin mach0 mach0 bin plugin (LGPL3) 
      bin mach064 mach064 bin plugin (LGPL3) 
      bin mbn MBN/SBL bootloader things (LGPL3) 
      bin mdmp Minidump format r_bin plugin (LGPL3) 
      bin menuet Menuet/KolibriOS bin plugin (LGPL3) 
      bin mz MZ bin plugin (MIT) 
      bin nes NES (LGPL3) 
      bin nin3ds Nintendo 3DS FIRM format r_bin plugin (LGPL3) 
      bin ninds Nintendo DS format r_bin plugin (LGPL3) 
      bin ningb Gameboy format r_bin plugin (LGPL3) 
      bin ningba Game Boy Advance format r_bin plugin (LGPL3) 
      bin nro Nintendo Switch NRO0 binaries (MIT) 
      bin nso Nintendo Switch NSO0 binaries (MIT) 
      bin omf omf bin plugin (LGPL3) 
      bin p9 Plan9 bin plugin (LGPL3) 
      bin pe PE bin plugin (LGPL3) 
      bin pe64 PE64 (PE32+) bin plugin (LGPL3) 
      bin pebble Pebble Watch App (LGPL) 
      bin psxexe Sony PlayStation 1 Executable (LGPL3) 
      bin sfc Super NES / Super Famicom ROM file (LGPL3) 
      bin smd SEGA Genesis/Megadrive (LGPL3) 
      bin sms SEGA MasterSystem/GameGear (LGPL3) 
      bin spc700 SNES-SPC700 Sound File Data (LGPL3) 
      bin te TE bin plugin (LGPL3) 
      bin vsf VICE Snapshot File (LGPL3) 
      bin wasm WebAssembly bin plugin (MIT) 
      bin xbe Microsoft Xbox xbe format r_bin plugin (LGPL3) 
      bin zimg zimg format bin plugin (LGPL3) 
      xtr fatmach0 fat mach0 bin extractor plugin (LGPL3)
      xtr xtr_dyldcache dyld cache bin extractor plugin (LGPL3)

## Valid IO plugins 
   - (can be extended) 
   - `radare2 -L`

      
```
      rw_ ar Open ar/lib files [ar|lib]://[file//path] (LGPL3)
      rw_ bfdbg BrainFuck Debugger (bfdbg://path/to/file) (LGPL3)
      rwd bochs Attach to a BOCHS debugger (LGPL3)
      r_d debug Native debugger (dbg:///bin/ls dbg://1388 pidof:// waitfor://) (LGPL3) v0.2.0 pancake
      rw_ default open local files using def_mmap:// (LGPL3)
      rwd gdb Attach to gdbserver, 'qemu -s', gdb://localhost:1234 (LGPL3)
      rw_ gzip read/write gzipped files (LGPL3)
      rw_ http http get (http://rada.re/) (LGPL3)
      rw_ ihex Intel HEX file (ihex://eeproms.hex) (LGPL)
      r__ mach mach debug io (unsupported in this platform) (LGPL)
      rw_ malloc memory allocation (malloc://1024 hex://cd8090) (LGPL3)
      rw_ mmap open file using mmap:// (LGPL3)
      rw_ null null-plugin (null://23) (LGPL3)
      rw_ procpid /proc/pid/mem io (LGPL3)
      rwd ptrace ptrace and /proc/pid/mem (if available) io (LGPL3)
      rwd qnx Attach to QNX pdebug instance, qnx://host:1234 (LGPL3)
      rw_ r2k kernel access API io (r2k://) (LGPL3)
      rw_ r2pipe r2pipe io plugin (MIT)
      rw_ r2web r2web io client (r2web://cloud.rada.re/cmd/) (LGPL3)
      rw_ rap radare network protocol (rap://:port rap://host:port/file) (LGPL3)
      rw_ rbuf RBuffer IO plugin: rbuf:// (LGPL)
      rw_ self read memory from myself using 'self://' (LGPL3)
      rw_ shm shared memory resources (shm://key) (LGPL3)
      rw_ sparse sparse buffer allocation (sparse://1024 sparse://) (LGPL3)
      rw_ tcp load files via TCP (listen or connect) (LGPL3)
      rwd windbg Attach to a KD debugger (windbg://socket) (LGPL3)
      rwd winedbg Wine-dbg io and debug.io plugin for r2 (MIT)
      rw_ zip Open zip files [apk|ipa|zip|zipall]://[file//path] (BSD)
```


## Available algorithems 
   - `rahash2 -L` , sorted

      
```
      Available Hashes: 
       adler32
       crc15can
       crc16
       crc16citt
       crc16hdlc
       crc16usb
       crc24
       crc32
       crc32c
       crc32ecma267
       crc8smbus
       entropy
       hamdist
       luhn
       md4
       md5
       mod255
       parity
       pcprint
       sha1
       sha256
       sha384
       sha512
       xor
       xorpair
       xxhash
      
      Available Encoders/Decoders: 
       base64
       base91
       punycode
      
      Available Crypto Algos: 
       aes-cbc
       aes-ecb
       blowfish
       cps2
       des-ecb
       rc2
       rc4
       rc6
       rol
       ror
       rot
       serpent-ecb
       xor
```
