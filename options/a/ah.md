<!-- TITLE: ah -->

#  `ah[?]`   analysis hints (force opcode size, ...)


```text
Usage: ah[lba-]Analysis Hints
```


## Tips
  - `ah` is helpful during ARM analysis

---
- `ah?` show this help
- `ah? offset` show hint of given offset
- `ah` list hints in human-readable format
- `ah.` list hints in human-readable format from current offset
- `ah-` remove all hints
- `ah- offset [size]` remove hints at given offset
- `ah* offset` list hints in radare commands format
- `aha ppc 51` set arch for a range of N bytes
- `ahb 16 @ $$` force 16 bit for current instruction
	> Use `ahb` to define 16, 32 bit functions. Helpful with arm.
- `ahc 0x804804` override call/jump address
- `ahe 3,eax,+=` set vm analysis string
- `ahf 0x804840` override fallback address for call
- `ahh 0x804840` highlight this adrress offset in disasm

- [ `ahi[?] 10` define numeric base for immediates (1, 8, 10, 16, s)](/options/a/ah/ahi)

- `ahj` list hints in JSON
- `aho foo a0,33` replace opcode string
- `ahp addr` set pointer hint
- `ahs 4` set opcode size=4
- `ahS jz` set asm.syntax=jz for this opcode

<p hidden>ah? ah ah. ah- ah* aha ahb ahc ahe ahf ahh ahi ahj aho ahp ahs ahS</p>