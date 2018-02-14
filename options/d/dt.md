<!-- TITLE: dt -->

#  `dt[?]` Display instruction traces (dtr=reset)


```
Usage: dt Trace commands
```

> To enable tracing, set `e asm.trace=1; e dbg.trace=1` 

- `dt` List all traces
- `dt [addr]` Show trace info at address
  > 🚀 _To count instructions, use `e asm.trace=1 / e dbg.trace=1` followed by`dt`_ [asciinema](https://asciinema.org/a/AAxcyuprERjhJwutaOR0fdGun)
- `dt%` TODO
- `dt*` List all traced opcode offsets
- `dt+ [addr] [times]` Add trace for address N times
- `dt-` Reset traces (instruction/calls)
- `dtD` Show dwarf trace (at*|rsc dwarf-traces $FILE)
- `dta 0x804020 ...` Only trace given addresses

- [ `dtc[?][addr]|([from] [to] [addr])` Trace call/ret](/options/d/dt/dtc)

- `dtd` List all traced disassembled
	> Show disasm of each instruction traced 

- [ `dte[?]` Show esil trace logs](/options/d/dt/dte)

- `dtg` Graph call/ret trace
- `dtg*` Graph in agn/age commands. use .dtg*;aggi for visual
- `dtgi` Interactive debug trace
- `dtr` Show traces as range commands (ar+)

- [ `dts[?]` Trace sessions](/options/d/dt/dts)

- `dtt [tag]` Select trace tag (no arg unsets)

- Screenshot
	![](/uploads/small-d/tracing-visual-mode.png)
	> `dt` The numbers in the red box indicates the order of the trace count as each instruction is stepped into, and the green box indicates how many times that instruction has run

<p hidden>dt dt% dt* dt+ dt- dtD dta dtc dtd dte dtg dtg* dtgi dtr dts dtt</p>
