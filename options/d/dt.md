<!-- TITLE: dt -->

#  **`dt[?]`** Display instruction traces (dtr=reset)


```text
Usage: dt Trace commands
```


- **`dt`** List all traces
- **`dt [addr]`** Show trace info at address
  > _To count instructions, use `e asm.trace=1 / e dbg.trace=1` followed by`dt`_
- **`dt%`** TODO
- **`dt*`** List all traced opcode offsets
- **`dt+ [addr] [times]`** Add trace for address N times
- **`dt-`** Reset traces (instruction/calls)
- **`dtD`** Show dwarf trace (at*|rsc dwarf-traces $FILE)
- **`dta 0x804020 ...`** Only trace given addresses

- [ **`dtc[?][addr]|([from] [to] [addr])`** Trace call/ret](/options/d/dt/dtc)

- **`dtd`** List all traced disassembled

- [ **`dte[?]`** Show esil trace logs](/options/d/dt/dte)

- **`dtg`** Graph call/ret trace
- **`dtg*`** Graph in agn/age commands. use .dtg*;aggi for visual
- **`dtgi`** Interactive debug trace
- **`dtr`** Show traces as range commands (ar+)

- [ **`dts[?]`** Trace sessions](/options/d/dt/dts)

- **`dtt [tag]`** Select trace tag (no arg unsets)