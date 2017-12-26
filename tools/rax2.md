<!-- TITLE: rax2 -->

# rax2

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

