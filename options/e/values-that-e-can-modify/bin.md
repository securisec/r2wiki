<!-- TITLE: bin -->

# bin

- `bin.b64str` Try to debase64 the strings _Default is false_
- `bin.baddr` Base address of the binary _Default is 4194304_
	> `bin.baddr` can be used to set the base address. 
- `bin.classes` Load classes from rbin on startup _Default is true_
- `bin.dbginfo` Load debug information at startup if available _Default is true_
- `bin.debase64` Try to debase64 all strings _Default is false_
- `bin.demangle` Import demangled symbols from RBin _Default is true_
- `bin.demanglecmd` run xcrun swift-demangle and similar if available (SLOW) _Default is false_
- `bin.filter` Filter symbol names to fix dupped names _Default is true_
- `bin.force` Force that rbin plugin
- `bin.laddr` Base address for loading library ('*.so') _Default is 0_
- `bin.lang` Language for bin.demangle _Default is c_
- `bin.libs` Try to load libraries after loading main binary _Default is false_
- `bin.maxstr` Maximum string length for r_bin _Default is 0_
- `bin.maxstrbuf` Maximum size of range to load strings from _Default is 0x00a00000_
- `bin.minstr` Minimum string length for r_bin _Default is 0_
- `bin.prefix` Prefix all symbols/sections/relocs with a specific string
- `bin.rawstr` Load strings from raw binaries _Default is false_
- `bin.relocs` Load relocs information at startup if available _Default is true_
- `bin.strfilter` Filter strings
- `bin.strings` Load strings from rbin on startup _Default is true_
- `bin.strpurge` Try to purge false positive strings _Default is false_
- `bin.verbose` Show RBin warnings when loading binaries _Default is true_

<p hidden>bin.b64str bin.baddr bin.classes bin.dbginfo bin.debase64 bin.demangle bin.demanglecmd bin.filter bin.force bin.laddr bin.lang bin.libs bin.maxstr bin.maxstrbuf bin.minstr bin.prefix bin.rawstr bin.relocs bin.strfilter bin.strings bin.strpurge bin.verbose</p>