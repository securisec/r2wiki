<!-- TITLE: wao -->

#  **`wao[?] op`** modify opcode (change conditional of jump. nop, etc)


```text
Usage: wao [op]performs a modification on current opcode
```


> NOTE: those operations are only implemented for x86 and arm atm

- **`wao nop`** nop current opcode
- **`wao jz`** make current opcode conditional (zero)
- **`wao jnz`** make current opcode conditional (not zero)
- **`wao ret1`** make the current opcode return 1
- **`wao ret0`** make the current opcode return 0
- **`wao retn`** make the current opcode return -1
- **`wao un-cjmp`** remove conditional operation to branch
- **`wao trap`** make the current opcode a trap
- **`wao recj`** 🚀 swap conditional branch. Old name _swap-cjmp_ Invert conditional jump [asciinema](https://asciinema.org/a/Oiht2V7aKAcRbRYfMa7eejvVk)

<p hidden>wao</p>