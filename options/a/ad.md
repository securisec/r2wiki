<!-- TITLE: ad -->
#  `ad[?]`   analyze data trampoline (wip)


```text
Usage: ad[kt] [...]
```


- `ad [N] [D]`   analyze N data words at D depth
- `ad4 [N] [D]`   analyze N data words at D depth (asm.bits=32)
- `ad8 [N] [D]`   analyze N data words at D depth (asm.bits=64)
- `adf`   analyze data in function (use like .adf @@=`afl~[0]`
- `adfg`   analyze data in function gaps
- `adt`   analyze data trampolines (wip)
- `adk`   analyze data kind (code, text, data, invalid, ...)

<p hidden>ad ad4 ad8 adf adfg adt adk</p>