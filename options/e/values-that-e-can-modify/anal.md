<!-- TITLE: anal -->

# anal

- `anal.a2f` Use the new WIP analysis algorithm (core/p/a2f), anal.depth ignored atm _Default is false_
- `anal.afterjmp` Continue analysis after jmp/ujmp _Default is true_
- `anal.arch` Select the architecture to use _Default is x86_
- `anal.armthumb` aae computes arm/thumb changes (lot of false positives ahead) _Default is false_
- `anal.autoname` Automatically set a name for the functions, may result in some false positives _Default is true_
- `anal.bb.align` Possible space between basic blocks _Default is 0x10_
- `anal.bb.maxsize` Maximum basic block size _Default is 1024_
- `anal.bb.split` Use the experimental basic block split for JMPs _Default is true_
- `anal.brokenrefs` Follow function references as well if function analysis was failed _Default is false_
- `anal.calls` Make basic af analysis walk into calls _Default is false_
- `anal.cjmpref` Create references for conditional jumps _Default is false_
- `anal.cpp.abi` Select C++ ABI (Compiler) _Default is itanium_
- `anal.cpu` Specify the anal.cpu to use _Default is x86_
- `anal.datarefs` Follow data references for code coverage _Default is false_
- `anal.depth` Max depth at code analysis _Default is 16_
- `anal.eobjmp` jmp is end of block mode (option) _Default is false_
- `anal.esil` Use the new ESIL code analysis _Default is false_
- `anal.fcnprefix` Prefix new function names with this _Default is fcn_
- `anal.from` Lower limit on the address range for analysis _Default is 0xffffffffffffffff_
- `anal.gp` Set the value of the GP register (MIPS) _Default is 0_
- `anal.gp2` Set anal.gp before emulating each instruction (workaround) _Default is false_
- `anal.hasnext` Continue analysis after each function _Default is false_
  - > `anal.hasnext` _Forces to find a function, after the end of a function._
- `anal.hpskip` Skip `mov reg, reg` and `lea reg, [reg] at the beginning of functions _Default is false_
-  `anal.in` Specify search boundaries for analysis _Default is io.maps_
- `anal.jmpabove` Jump above function pointer _Default is true_
- `anal.jmpref` Create references for unconditional jumps _Default is true_
- `anal.jmptbl` Analyze jump tables in switch statements _Default is false_
  - > `anal.jmptbl` _Helps in analyzing jump tables. Creates a new flags called switch and jmptbl_
  - > `anal.jmptbl` _Set value to true before analysis to analyze jump tables._ [asciinema](https://asciinema.org/a/OPQxOl3OGIb63m2au6KvHXuVZ)
- `anal.limits` Restrict analysis to address range [anal.from _Default is false_
- `anal.maxreflines` Maximum number of reflines to be analyzed and displayed in asm.lines with pd _Default is 0_
- `anal.noncode` Analyze data as code _Default is false_
- `anal.nopskip` Skip nops at the beginning of functions _Default is true_
- `anal.prelude` Specify an hexpair to find preludes in code
- `anal.ptrdepth` Maximum number of nested pointers to follow in analysis _Default is 3_
- `anal.pushret` Analyze push+ret as jmp _Default is false_
- `anal.recont` End block after splitting a basic block instead of error _Default is false_
- `anal.refstr` Search string references in data references _Default is false_
- `anal.rnr` (Recursive no return checks (EXPERIMENTAL)) _Default is false_
- `anal.sleep` Sleep N usecs every so often during analysis. Avoid 100% CPU usage _Default is 0_
- `anal.split` Split functions into basic blocks in analysis _Default is true_
- `anal.strings` Identify and register strings during analysis (aar only) _Default is false_
  - > `anal.strings` _Disables bin.strings option. Only gets strings that are referenced by code_
- `anal.timeout` Stop analyzing after a couple of seconds _Default is 0_
- `anal.to` Upper limit on the address range for analysis Default is 0xffffffffffffffff
- `anal.vars` Analyze local variables and arguments _Default is true_
- `anal.vinfun` Search values in functions (aav) (false by default to only find on non-code) _Default is true_
- `anal.vinfunrange` Search values outside function ranges (requires anal.vinfun=false) _Default is false_


<p hidden>anal.a2f anal.afterjmp anal.arch anal.armthumb anal.autoname anal.bb.align anal.bb.maxsize anal.bb.split anal.brokenrefs anal.calls anal.cjmpref anal.cpu anal.datarefs anal.depth anal.eobjmp anal.esil anal.fcnprefix anal.from anal.gp anal.hasnext anal.hpskip Skip mov reg, reg and  anal.jmpabove anal.jmpref anal.jmptbl anal.limits anal.maxreflines anal.noncode anal.nopskip anal.prelude anal.ptrdepth anal.pushret anal.recont anal.refstr anal.sleep anal.split anal.strings anal.timeout anal.to anal.vars anal.vinfun anal.vinfunrange jump table</p>