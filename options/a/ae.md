<!-- TITLE: ae -->

#  `ae[?] [expr]`   analyze opcode eval expression (see ao)


```text
Usage: ae[idesr?] [arg]ESIL code emulation
```


[Breakdown of ESIL](/options/a/ae/breakdown_esil)

- `ae [expr]`   evaluate ESIL expression
- `ae?`   show this help
- `ae??`   show ESIL help

[ `ae[aA][f] [count]`   analyse esil accesses (regs, mem..)](./ae-aA-f-count-analyse-esil-accesses-regs-mem-fb12b2c6-0b22-4894-b279-006868d18f31.md)

[ `aec[?]`   continue until ^C](./aec-continue-until-C-b869f7ef-ef9c-47c0-a848-2b95fb267a78.md)

- `aef [addr]`   emulate function
- `aei`   initialize ESIL VM state (aei- to deinitialize)
- `aeim [addr] [size] [name]`   initialize ESIL VM stack (aeim- remove)
- `aeip`   initialize ESIL program counter to curseek
- `aek [query]`   perform sdb query on [ESIL.info](http://esil.info)
- `aek-`   resets the ESIL.info sdb instance

[ `aep[?] [addr]`   manage esil pin hooks](./aep-addr-manage-esil-pin-hooks-660fc309-f990-499a-912e-a374f04bf9f2.md)

- `aepc [addr]`   change esil PC to this address
- `aer [..]`   handle ESIL registers like 'ar' or 'dr' does

[ `aets[?]`   ESIL Trace session](./aets-ESIL-Trace-session-ba8fedcb-9540-4831-a85a-b64e9e698242.md)

- `aes`   perform emulated debugger step
- `aesp [X] [N]`   evaluate N instr from offset X
- `aesb`   step back
- `aeso`   step over
- `aesu [addr]`   step until given address
- `aesue [esil]`   step until esil expression match
- `aetr[esil]`   Convert an ESIL Expression to REIL
- `aex [hex]`   evaluate opcode expression