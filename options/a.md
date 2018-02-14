<!-- TITLE: a -->

#  `a` Analysis commands


```
Usage: a[abdefFghoprxstc] [...]
```


## Tips
  - Use `afn` to rename function. Use `dr` in visual mode
  - To see cross references for strings, use `axt @@ str.*` . The `@@` is a for i in x operator in radare2.
---

- [ `aa[?]` analyze all (fcns + bbs) (aa0 to avoid sub renaming)](/options/a/aa)
- [ `ab [hexpairs]` analyze bytes](/options/a/ab)
- `ac [cycles]` analyze which op could be executed in [cycles]
- [ `ad[?]` analyze data trampoline (wip)](/options/a/ad)
- `ad [from] [to]` analyze data pointers to (from-to)
- [ `ae[?] [expr]` analyze opcode eval expression (see ao)](/options/a/ae)
- [ `af[?]` analyze Functions](/options/a/af)
- `aF` same as above, but using anal.depth=1
- [ `ag[?] [options]` output Graphviz code](/options/a/ag)
- [ `ah[?]` analysis hints (force opcode size, ...)](/options/a/ah)
- `ai [addr]` address information (show perms, stack, heap, ...)
- `an [name] [@addr]` show/rename/create whatever flag/function is used at addr
- [ `ao[?] [len]` analyze Opcodes (or emulate it)](/options/a/ao)
- `aO` Analyze N instructions in M bytes
- `ap` find prelude for current offset
- [ `ar[?]` like 'dr' but for the esil vm. (registers)](/options/a/ar)
- [ `as[?] [num]` analyze syscall using dbg.reg](/options/a/as)
- `av[?] [.]` show vtables
- [ `ax[?]` manage refs/xrefs (see also afx?)](/options/a/ax)

<p hidden>aa ab ac ad ae af aF ag ah ai an ao aO ap ar as av ax</p>