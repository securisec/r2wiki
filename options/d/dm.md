<!-- TITLE: dm -->

#  `dm[?]` Show memory maps


```text
Usage: dm # Memory maps commands
```


- `dm` List memory maps of target process
  - Screenshot

    ![]("/uploads/small-d/dm.png) 

- `dm address size` Allocate <size> bytes at <address> (anywhere if address is -1) in child process
- `dm=` List memory maps of target process (ascii-art bars)
- `dm.` Show map name of current address
- `dm*` List memmaps in radare commands
- `dm- address` Deallocate memory map of <address>
- `dmd[a] [file]` Dump current (all) debug map region to a file (from-to.dmp) (see Sd)

- [ `dmh[?]` Show map of heap](/options/d/dm/dmh)

- [ `dmi [addr|libname] [symname]` List symbols of target lib](/options/d/dm/dmi)

- `dmi* [addr|libname] [symname]` List symbols of target lib in radare commands
- `dmi.` List closest symbol to the current address
- `dmiv` Show address of given symbol for given lib
- `dmj` List memmaps in JSON format
- `dml <file>` Load contents of file into the current map region (see Sl)
- `dmm[?][j*]` List modules (libraries, binaries loaded in memory)

- [ `dmp[?] <address> <size> <perms>` Change page at \<address\> with \<size\>, protection \<perms\> (rwx)](/options/d/dm/dmp)

- [ `dms[?] <id> <mapaddr>` Take memory snapshot](/options/d/dm/dms)

- `dms- <id> <mapaddr>` Restore memory snapshot
- `dmS [addr|libname] [sectname]` List sections of target lib
- `dmS* [addr|libname] [sectname]` List sections of target lib in radare commands

<p hidden>dm dm. dm* dm- dmd dmh dmi dmi. dmiv dmj dml dmm dmp dms dms- dmS dmS*</p>
