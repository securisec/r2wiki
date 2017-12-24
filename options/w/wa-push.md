<!-- TITLE: wa -->

#  **`wa[?] push ebp`** write opcode, separated by ';' (use '"' around the command)

- **`wa nop`** write nopcode using asm.arch and asm.bits
- **`wa* mov eax, 33`** show 'wx' op with hexpair bytes of assembled opcode
- **`"wa nop;nop"`** assemble more than one instruction (note the quotes)
- **`waffoo.asm`** assemble file and write bytes
- **`wao?`** show help for assembler operation on current opcode (hack)

<p hidden>wa wa* wao</p>