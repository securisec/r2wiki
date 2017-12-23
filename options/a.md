<!-- TITLE: a -->

#  **`a`** Analysis commands


```text
Usage: a[abdefFghoprxstc] [...]
```


## **Tips**
  - Use `afn` to rename function. Use `dr` in visual mode
  - To see cross references for strings, use `axt @@ str.*` . The `@@` is a for i in x operator in radare2.
---

- [ **`aa[?]`** analyze all (fcns + bbs) (aa0 to avoid sub renaming)](/options/a/aa)
- [ `ab [hexpairs]` analyze bytes](/options/a/ab)
- `ac [cycles]` analyze which op could be executed in [cycles]
- [ `ad[?]` analyze data trampoline (wip)](/options/a/ad)
- `ad [from] [to]` analyze data pointers to (from-to)
- [ `ae[?] [expr]` analyze opcode eval expression (see ao)](/options/a/ae)
- [ `af[?]` analyze Functions](/options/a/af)
- `aF` same as above, but using anal.depth=1
- [ `ag[?] [options]` output Graphviz code](/options/a/ag-options-output-Graphviz-code-eb8c5d2c-e606-4ac0-80c2-b1885bc324bf.md)
- [ `ah[?]` analysis hints (force opcode size, ...)](/options/a/ah-analysis-hints-force-opcode-size-57ef1086-626c-4baa-ace6-3e9382036b20.md)
- `ai [addr]` address information (show perms, stack, heap, ...)
- `an [name] [@addr]` show/rename/create whatever flag/function is used at addr
- [ `ao[?] [len]` analyze Opcodes (or emulate it)](/options/a/ao-len-analyze-Opcodes-or-emulate-it-2304893a-4fdb-455d-afff-86d76cd1b333.md)
- `aO` Analyze N instructions in M bytes
- `ap` find prelude for current offset
- [ `ar[?]` like 'dr' but for the esil vm. (registers)](/options/a/ar-like-dr-but-for-the-esil-vm-registers-1c46e6b7-e3a1-4a03-85de-226381a184c1.md)
- [ `as[?] [num]` analyze syscall using dbg.reg](/options/a/as-num-analyze-syscall-using-dbg-reg-02716739-a129-45c7-922f-8e7f64f09e3f.md)
- `av[?] [.]` show vtables
- [ `ax[?]` manage refs/xrefs (see also afx?)](/options/a/ax-manage-refs-xrefs-see-also-afx-edce23b5-3963-4ca3-aee9-a1842dd96b3f.md)