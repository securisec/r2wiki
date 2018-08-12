<!-- TITLE: /a -->

# /a jmp find analyzed instructions of this type
```
Usage: /a[stf][?ljq] [instr | op.type | op.family]Search for assembly
```

- `/a instr  `  assemble given instruction and search the bytes
- `/at type  `  Search for instructions of given type
- `/af family`  Search for instruction of specific family
- `/as       `  Search for syscalls (See /at swi and /af priv)
- `/al       `  Same as aoml, list all opcodes
- `/asl      `  Same as asl, list all syscalls
- `/atl      `  List all instruction types
- `/afl      `  List all instruction families