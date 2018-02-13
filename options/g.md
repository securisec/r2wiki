<!-- TITLE: g -->

#  `g` Generate shellcodes with r_egg


```text
Usage: g[wcilper] [arg]Go compile shellcodes
```


- `g foo.r` Compile r_egg source file
- `gw` Compile and write
- `gc cmd=/bin/ls` Set config option for shellcodes and encoders
- `gc` List all config options
- `gl[?]` List plugins (shellcodes, encoders)
- `gs name args` Compile syscall name(args)
- `gi [type]` Compile shellcode. like ragg2 -i (see gl or ragg2 -L)
- `gp padding` Define padding for command
- `ge xor` Specify an encoder
- `gr` Reset r_egg
- `EVAL VARS:` asm.arch, asm.bits, asm.os

<p hidden>gw gc gl gs gi gp ge gr</p>