<!-- TITLE: esil -->

# esil
> Some infor about [ESIL](http://radare.org/get/lacon2k15-esil.pdf) (from 2015)

- `esil.exectrap` trap when executing code in non-executable memory _Default is false_
- `esil.fillstack` Initialize ESIL stack with (random, debrujn, sequence, zeros, ...)
- `esil.gotolimit` Maximum number of gotos per ESIL expression _Default is 0x00001000_
- `esil.iotrap` invalid read or writes produce a trap exception _Default is true_
- `esil.mdev.range` Specify a range of memory to be handled by cmd.esil.mdev
- `esil.nonull` Prevent memory read, memory write at null pointer _Default is false_
- `esil.prestep` Step before esil evaluation in `de` commands _Default is true_
- `esil.romem` Set memory as read-only for ESIL _Default is false_
- `esil.stack.addr` Number of elements that can be pushed on the esilstack _Default is 0x00100000_
- `esil.stack.depth` Number of elements that can be pushed on the esilstack _Default is 32_
- `esil.stack.pattern` Specify fill pattern to initialize the stack (0, w, d, i) _Default is 0_
- `esil.stack.size` Number of elements that can be pushed on the esilstack _Default is 0x000f0000_
- `esil.stats` Statistics from ESIL emulation stored in sdb _Default is false_
- `esil.verbose` Show ESIL verbose level (0, 1, 2) _Default is 0_

<p hidden>esil.exectrap esil.fillstack esil.gotolimit esil.iotrap esil.mdev.range esil.nonull esil.prestep esil.romem esil.stack.addr esil.stack.depth esil.stack.pattern esil.stack.size esil.stats esil.verbose</p>