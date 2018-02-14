<!-- TITLE: dr -->

#  `dr[?]` Cpu registers


```
Usage: dr Registers commands
```


- `dr` Show 'gpr' registers
- `dr <register>=<val>` Set register value
- `dr8[1|2|4|8] [type]` Display hexdump of gpr arena (WIP)
- `dr=` 🚀 Show registers in columns [asciinema](https://asciinema.org/a/3pB3XIR48Lyz5XF9XTgbWTmWz)
- `dr?<register>` Show value of given register
- `drb[1|2|4|8] [type]` Display hexdump of gpr arena (WIP)
- `drc [name]` Related to conditional flag registers
- `drC` Show register profile comments
- `drd`  Show only different registers
  > 🚀 `drd` _This can be used to show differences between old and new register values_ [asciinema](https://asciinema.org/a/A0Ki2qX9DKajCU0tD5QA8N2P9)
- `drf` Show fpu registers (80 bit long double)
- `drl[j]` List all register names
- `drm` Show multimedia packed registers
- `drm mmx0 0 32 = 12` Set the first 32 bit word of the mmx reg to 12
- `drn <pc>` Get regname for pc,sp,bp,a0-3,zf,cf,of,sg
- `dro` Show previous (old) values of registers
- `drp` Display current register profile

- [ `drp[?] <file>` Load register metadata file](/options/d/dr/drp)

- `drpi` Display current internal representation of the register profile
- `drps` Fake register profile size
- `drpj` Show the current register profile (JSON)
- `drr` 🚀 Show registers references (telescoping) [asciinema](https://asciinema.org/a/s1bOy1oWQrKMMtPNIJ44Pr0UO)
  - Screenshot

    ![](/uploads/small-d/drr.png)

- [ `drs[?]` Stack register states](/options/d/dr/drs)

- `drt 16` 🚀 Show 16 bit registers [asciinema](https://asciinema.org/a/JBBPfzyiUsK34yLus1aIPK4Rk)
- `drt 32` 🚀 Show 32 bit registers [asciinema](https://asciinema.org/a/JBBPfzyiUsK34yLus1aIPK4Rk)
- `drt 80` Show 80 bit registers (long double)
- `drt all` 🚀 Show all registers [asciinema](https://asciinema.org/a/JBBPfzyiUsK34yLus1aIPK4Rk)
- `drt flg` Show flag registers

- [ `drt[?]` Show all register types](/options/d/dr/drt)

- `drw <hexnum>` Set contents of the register arena

- [ `drx[?]` Show all debug registers](/options/d/dr/drx)

- `drx idx addr len rwx` Modify hardware breakpoint
- `drx-number` Clear hardware breakpoint
- `.dr*` Include common register values in flags
- `.dr-` Unflag all registers

<p hidden>dr dr8 dr= dr? drb drc drC drd drf drl drm drn dro drpdrpi drps drpj drr drs drt drw drX drx .dr</p>
