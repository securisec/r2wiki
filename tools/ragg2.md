<!-- TITLE: Ragg 2 -->

# ragg2

## Help

      Usage: ragg2 [-FOLsrxhvz] [-a arch] [-b bits] [-k os] [-o file] [-I path]
       [-i sc] [-e enc] [-B hex] [-c k=v] [-C file] [-p pad] [-q off]
       [-q off] [-dDw off:hex] file|f.asm|-
       -a [arch] select architecture (x86, mips, arm)
       -b [bits] register size (32, 64, ..)
       -B [hexpairs] append some hexpair bytes
       -c [k=v] set configuration options
       -C [file] append contents of file
       -d [off:dword] patch dword (4 bytes) at given offset
       -D [off:qword] patch qword (8 bytes) at given offset
       -e [encoder] use specific encoder. see -L
       -f [format] output format (raw, c, pe, elf, mach0, python, javascript)
       -F output native format (osx=mach0, linux=elf, ..)
       -h show this help
       -i [shellcode] include shellcode plugin, uses options. see -L
       -I [path] add include path
       -k [os] operating system's kernel (linux,bsd,osx,w32)
       -L list all plugins (shellcodes and encoders)
       -n [dword] append 32bit number (4 bytes)
       -N [dword] append 64bit number (8 bytes)
       -o [file] output file
       -O use default output file (filename without extension or a.out)
       -p [padding] add padding after compilation (padding=n10s32)
       ntas : begin nop, trap, 'a', sequence
       NTAS : same as above, but at the end
       -P [size] prepend debruijn pattern
       -q [fragment] debruijn pattern offset
       -r show raw bytes instead of hexpairs
       -s show assembler
       -v show version
       -w [off:hex] patch hexpairs at given offset
       -x execute
       -z output in C string syntax

[Payloads in C · The Official Radare Blog](http://radare.today/posts/payloads-in-c/)