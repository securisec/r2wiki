#  **`/c jmp [esp]`** search for asm code matching the given string

- **`/c instr`** search for instruction 'instr'
- **`/ce esil`** search for esil expressions matching substring
- **`/ca instr`** search for instruction 'instr' (in all offsets)
- **`/c/ instr`** search for instruction that matches regexp 'instr'
- **`/c/a instr`** search for every byte instruction that matches regexp 'instr'
- **`/c instr1;instr2`** search for instruction 'instr1' followed by 'instr2'
- **`/c/ instr1;instr2`** search for regex instruction 'instr1' followed by regex 'instr2'
- **`/cj instr`** json output
- **`/c/j instr`** regex search with json output
- **`/c* instr`** r2 command output

<p hidden>/ce /ca /c/ /c/a /cj /c/j /c*</p>