<!-- TITLE: ae -->

#  `ae[?] [expr]`   analyze opcode eval expression (see ao)


```
Usage: ae[idesr?] [arg]ESIL code emulation
```


[Breakdown of ESIL](/options/a/ae/breakdown_esil)

- `ae [expr]`   evaluate ESIL expression
- `ae?`   show this help
- `ae??`   show ESIL help
[ `ae[aA][f] [count]`   analyse esil accesses (regs, mem..)](/options/a/ae/aea)
[ `aec[?]`   continue until ^C](/options/a/ae/aec)
- `aef [addr]`   emulate function
- `aei`   initialize ESIL VM state (aei- to deinitialize)
- `aeim [addr] [size] [name]`   initialize ESIL VM stack (aeim- remove)
- `aeip`   initialize ESIL program counter to curseek
- `aek [query]`   perform sdb query on ESIL .info
- `aek-`   resets the ESIL .info sdb instance
[ `aep[?] [addr]`   manage esil pin hooks](/options/a/ae/aep)
- `aepc [addr]`   change esil PC to this address
- `aer [..]`   handle ESIL registers like 'ar' or 'dr' does
[ `aets[?]`   ESIL Trace session](/options/a/ae/aets)
- `aes`   perform emulated debugger step
- `aesp [X] [N]`   evaluate N instr from offset X
- `aesb`   step back
- `aeso`   step over
- `aesu [addr]`   step until given address
- `aesue [esil]`   step until esil expression match
- `aetr[esil]`   Convert an ESIL Expression to REIL
- `aex [hex]`   evaluate opcode expression

<p hidden>ae ae? ae?? aea aec aef aei aeim aeip aek aek- aep aepc aer aets aes aesp aesb aeso aesu aesue aetr aex</p>