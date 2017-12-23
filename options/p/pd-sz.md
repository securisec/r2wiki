<!-- TITLE: pd -->

#  **`pd[?] [sz] [a] [b]`** disassemble N opcodes (pd) or N bytes (pD)


```text
Usage: p[dD][ajbrfils] [sz] [arch] [bits] # Print Disassembly
```


> NOTE: len parameter can be negative {.is-info}

> NOTE: Pressing ENTER on empty command will repeat last pd command and also seek to end of disassembled range. {.is-info}

- **`pd N`** disassemble N instructions
- **`pd -N`** disassemble N instructions backward
- **`pD N`** disassemble N bytes
- **`pda`** disassemble all possible opcodes (byte per byte)
- **`pdb`** disassemble basic block
- **`pdc`** pseudo disassembler output in C-like syntax
- **`pdC`** show comments found in N instructions
- **`pdf`** disassemble function
- **`pdi`** like 'pi', with offset and bytes
- **`pdj`** disassemble to json
- **`pdk`** disassemble all methods of a class
- **`pdl`** show instruction sizes
- **`pdr`** recursive disassemble across the function graph
- **`pdR`** recursive disassemble block size bytes without analyzing functions
- **`pds[?]`** disassemble summary (strings, calls, jumps, refs) (see pdsf and pdfs)
  > _Can be used as either inside function, or assigned an offset `pds @offset[func_name]`_
- **`pdt`** disassemble the debugger traces (see atd)

<p hidden>pd pD pda pdb pdc pdC pdf pdi pdj pdk pdl pdr pdR pds pdt</p>