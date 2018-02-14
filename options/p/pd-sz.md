<!-- TITLE: pd -->

#  `pd[?] [sz] [a] [b]` disassemble N opcodes (pd) or N bytes (pD)


```
Usage: p[dD][ajbrfils] [sz] [arch] [bits] # Print Disassembly
```


> NOTE: len parameter can be negative 

> NOTE: Pressing ENTER on empty command will repeat last pd command and also seek to end of disassembled range. 

- `pd N` 🚀 disassemble N instructions [asciinema](https://asciinema.org/a/2nKEu7kSlVqBjOK4wP5z5zEsX)
- `pd -N` 🚀 disassemble N instructions backward [asciinema](https://asciinema.org/a/vd7otYJkQOz4O4L2A4mNgKp3t)
- `pD N` 🚀 disassemble N bytes [asciinema](https://asciinema.org/a/YHknEz9gYIfXzXceGwQ5ngEga)
- `pda` 🚀 disassemble all possible opcodes (byte per byte) [asciinema](https://asciinema.org/a/J7bNbCAvuLyWUgX34l6L5zIFZ)
- `pdb` 🚀 disassemble basic block [asciinema](https://asciinema.org/a/7aehL6ebprYJHHD7USmR4LLLO)
- `pdbj` disassemble basic block json output
- `pdc` 🚀 pseudo disassembler output in C-like syntax [asciinema](https://asciinema.org/a/B5GTvDyOpRPn488Da6mkGcBgC)
- `pdC` show comments found in N instructions 
- `pdf` 🚀 disassemble function asciinema[](https://asciinema.org/a/uDMKJWZBg0M9Fq14nQBh3VJnQ)
- `pdfs[j]`  - disassemble function (summary+cjmp), json)
- `pdi` 🚀 like 'pi', with offset and bytes [asciinema](https://asciinema.org/a/MGEEXMOfi74Sm3wf5X34PPaPk)
- `pdj` disassemble to json
- `pdk` disassemble all methods of a class 
- `pdl` 🚀 show instruction sizes [asciinema](https://asciinema.org/a/VqcVh8H731bmhBoLNwv21zqDF)
- `pdr` 🚀 recursive disassemble across the function graph [asciinema](https://asciinema.org/a/qbatqGNhB5Zmvr1VzmsEB7TRo)
- `pdR` 🚀 recursive disassemble block size bytes without analyzing functions [asciinema](https://asciinema.org/a/gpiEMqW1aUsLnPprBeCjcMBlS)
	> `pdR` command that doesnt requires previous analaysis and just follow non-conditional jumps
- `pds[?]` 🚀 disassemble summary (strings, calls, jumps, refs) (see pdsf and pdfs) [asciinema](https://asciinema.org/a/pUcz5MwdofZbJrxzUIrZekH5z)
  > `pds` _Can be used as either inside function, or assigned an offset `pds @offset[func_name]`_

- `pdsf`  🚀 sumarize N bytes or function (pdfs) [asciinema](https://asciinema.org/a/sT6SJdYI4VqxqqTVcowF21hdk)
- `pdt` disassemble the debugger traces (see atd)

<p hidden>pd pD pda pdb pdc pdC pdf pdi pdj pdk pdl pdr pdR pds pdt</p>
