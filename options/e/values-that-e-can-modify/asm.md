<!-- TITLE: asm -->

# asm

- `asm.anal` Analyze code and refs while disassembling (see anal.strings) _Default is false_
- `asm.arch` Set the arch to be used by asm _Default is x86_
- `asm.armimm` Display # for immediates in ARM _Default is 0_
- `asm.asciidot` Enable a char filter for string comments that passes through chars in the range 0x20-0x7e and turns the rest into dots (except some control chars) _Default is false_
- `asm.assembler` Set the plugin name to use when assembling
- `asm.bbline` Show empty line after every basic block _Default is false_
- `asm.bits` Word size in bits at assembler _Default is 64_
- `asm.bytes` Display the bytes of each instruction _Default is true_
- `asm.bytespace` Separate hexadecimal bytes with a whitespace _Default is false_
- `asm.calls` Show callee function related info as comments in disasm _Default is true_
- `asm.capitalize` Use camelcase at disassembly _Default is false_
- `asm.cmtcol` Column to align comments _Default is 71_
- `asm.cmtflgrefs` Show comment flags associated to branch reference _Default is true_
- `asm.cmtfold` Fold comments, toggle with Vz _Default is false_
- `asm.cmtoff` Show offset comment in disasm (true, false, nodup) _Default is nodup_
- `asm.cmtpatch` Show patch comments in disasm _Default is false_
- `asm.cmtrefs` Show flag and comments from refs in disasm _Default is false_
- `asm.cmtright` Show comments at right of disassembly if they fit in screen _Default is true_
- `asm.comments` Show comments in disassembly view _Default is true_
- `asm.cpu` Set the kind of asm.arch cpu _Default is x86_
	> Example: `asm.cpu=cortex` when architecture is ARM.
- `asm.cycles` Show CPU-cycles taken by instruction at disassembly _Default is false_
- `asm.cyclespace` Indent instructions depending on CPU-cycles _Default is false_
- `asm.decode` Use code analysis as a disassembler _Default is false_
- `asm.decoff` Show segmented address in prompt (x86-16) _Default is false_
- `asm.demangle` Show demangled symbols in disasm _Default is true_
- `asm.describe` Show opcode description _Default is false_
- `asm.dwarf` Show dwarf comment at disassembly _Default is false_
- `asm.dwarf.abspath` Show absolute path in asm.dwarf _Default is false_
- `asm.dwarf.file` Show filename of asm.dwarf in pd _Default is true_
- `asm.emu` Run ESIL emulation analysis on disasm _Default is false (cpu emulation)_
  > `asm.emu` This can be used for instruction emulation where the register values are printed after each instruction executes (not debugger)

  > 🚀 Set `e asm.emu =1` to emulate cpu instructions [asciinema](https://asciinema.org/a/mC610KTE8RIgGZUBMO8JhkiyV)

- `asm.emu.pre` Run ESIL emulation starting at the closest flag in pd _Default is false_
	> `asm.emu.pre` this will do the emulation of the instructions before the current offset to get better disasm hints
- `asm.emu.skip` Skip metadata of given types in asm.emu _Default is ds_
- `asm.emu.stack` Create a temporary fake stack when emulating in disasm (asm.emu) _Default is false_
- `asm.emu.str` Show only strings if any in the asm.emu output _Default is false_
  > `asm.emu.str` Handy when analyzing objective c binaries
- `asm.emu.stroff` Always show offset when printing asm.emu strings
- `asm.emu.write` Allow asm.emu to modify memory (WARNING) _Default is false_
- `asm.esil` Show ESIL instead of mnemonic _Default is false_
- `asm.family` Show family name in disasm _Default is false_
- `asm.fcncalls` Show functions calls _Default is true_
- `asm.fcnlines` Show function boundary lines _Default is true_
- `asm.features` Specify supported features by the target CPU
- `asm.filter` Replace numeric values by flags (e.g. 0x4003e0 -> sym.imp.printf) _Default is true_
- `asm.flags` Show flags _Default is true_
- `asm.flagsinbytes` Display flags inside the bytes space _Default is false_
- `asm.flgoff` Show offset in flags _Default is false_
- `asm.functions` Show functions in disassembly _Default is true_
- `asm.hints` Show hints for magic numbers in disasm _Default is false_
- `asm.immstr` Show immediates values as strings _Default is false_
- `asm.immtrim` Remove all offsets and constants from disassembly _Default is false_
- `asm.indent` Indent disassembly based on reflines depth _Default is false_
- `asm.indentspace` How many spaces to indent the code _Default is 2_
- `asm.invhex` Show invalid instructions as hexadecimal numbers _Default is false_
- `asm.jmphints` Show jump hints [numbers] in disasm _Default is true_
- `asm.jmpsub` Always substitute jump, call and branch targets in disassembly _Default is false_
	> `asm.jmpsub` Substitutes targets of jmp, call and branch ops in disassembly based on jump target in RAnalOp structure
- `asm.lbytes` Align disasm bytes to left _Default is true_
- `asm.leahints` Show LEA hints [numbers] in disasm _Default is false_
- `asm.lines` Show ASCII-art lines at disassembly _Default is true_
- `asm.lines.call` Enable call lines _Default is false_
- `asm.lines.ret` Show separator lines after ret _Default is false_
- `asm.linesout` Show out of block lines _Default is true_
- `asm.linesright` Show lines before opcode instead of offset _Default is false_
- `asm.lineswide` Put a space between lines _Default is false_
- `asm.lineswidth` Number of columns for program flow arrows _Default is 7_
- `asm.marks` Show marks before the disassembly _Default is true_
- `asm.maxrefs` Maximum number of xrefs to be displayed as list (use columns above) _Default is 5_
- `asm.midcursor` Cursor in visual disasm mode breaks the instruction _Default is false_
- `asm.middle` Allow disassembling jumps in the middle of an instruction _Default is false_
- `asm.midflags` Realign disassembly if there is a flag in the middle of an instruction _Default is 2_
- `asm.minicols` Only show the instruction in the column disasm _Default is false_
- `asm.minvalsub` Minimum value to substitute in instructions (asm.varsub) _Default is 256_
- `asm.nbytes` Number of bytes for each opcode at disassembly _Default is 6_
- `asm.nodup` Do not show dupped instructions (collapse disasm) _Default is false_
- `asm.noisy` Show comments considered noisy but possibly useful _Default is true_
- `asm.offset` Show offsets at disassembly _Default is true_
- `asm.os` Select operating system (kernel) _Default is linux_
- `asm.parser` Set the asm parser to use _Default is x86.pseudo_
- `asm.payloads` Show payload bytes in disasm _Default is false_
- `asm.pcalign` Only recognize as valid instructions aligned to this value _Default is 0_
- `asm.pseudo` Enable pseudo syntax _Default is false_
- `asm.reloff` Show relative offsets instead of absolute address in disasm _Default is false_
- `asm.reloff.flags` Show relative offsets to flags (not only functions) _Default is false_
- `asm.relsub` Substitute pc relative expressions in disasm _Default is true_
- `asm.section` Show section name before offset _Default is false_
- `asm.section.col` Columns width to show asm.section _Default is 20_
- `asm.section.sub` Show offsets in disasm prefixed with section/map name _Default is false_
- `asm.segoff` Show segmented address in prompt (x86-16) _Default is false_
- `asm.shortcut` Shortcut position (-1, 0, 1) _Default is 1_
- `asm.size` Show size of opcodes in disassembly (pd) _Default is false_
- `asm.slow` Perform slow analysis operations in disasm _Default is true_
- `asm.stackptr` Show stack pointer at disassembly _Default is false_
- `asm.strenc` Assumed string encoding for disasm _Default is guess_
- `asm.strip` Removes garbage instructions from disassembly
- `asm.symbol` Show symbol+delta instead of absolute offset _Default is false_
- `asm.symbol.col` Columns width to show asm.section _Default is 40_
- `asm.syntax` Select assembly syntax _Default is intel_
- `asm.tabs` Use tabs in disassembly _Default is 0_
- `asm.tabsoff` tabulate spaces after the offset _Default is 0_
- `asm.tabsonce` Only tabulate the opcode, not the arguments _Default is false_
- `asm.trace` Show execution traces for each opcode _Default is false_
- `asm.tracespace` Indent disassembly with trace.count information _Default is false_
- `asm.ucase` Use uppercase syntax at disassembly _Default is false_
- `asm.vars` Show local function variables in disassembly _Default is true_
- `asm.varsub` Substitute variables in disassembly _Default is true_
- `asm.varsub_only` Substitute the entire variable expression with the local variable name (e.g. [local10h] instead of [ebp+local10h]) _Default is true_
- `asm.varsum` Show variables summary instead of full list in disasm _Default is false_
- `asm.varxs` Show accesses of local variables _Default is false_
- `asm.xrefs` Show xrefs in disassembly _Default is true_

<p hidden>asm.anal asm.arch asm.armimm asm.asciidot asm.assembler asm.bbline asm.bits asm.bytes asm.bytespace asm.calls asm.capitalize asm.cmtcol asm.cmtflgrefs asm.cmtfold asm.cmtoff asm.cmtpatch asm.cmtrefs asm.cmtright asm.comments asm.cpu asm.cycles asm.cyclespace asm.decode asm.decoff asm.demangle asm.describe asm.dwarf asm.dwarf.abspath asm.dwarf.file asm.emu asm.emuskip asm.emustack asm.emustr asm.emuwrite asm.esil asm.family asm.fcncalls asm.fcnlines asm.features asm.filter asm.flags asm.flagsinbytes asm.flgoff asm.functions asm.hints asm.immstr asm.immtrim asm.indent asm.indentspace asm.invhex asm.jmphints asm.lbytes asm.leahints asm.lines asm.lines.call asm.lines.ret asm.linesout asm.linesright asm.lineswide asm.lineswidth asm.marks asm.maxrefs asm.midcursor asm.middle asm.midflags asm.minicols asm.minvalsub asm.nbytes asm.nodup asm.noisy asm.offset asm.os asm.parser asm.payloads asm.pcalign asm.pseudo asm.reloff asm.reloff.flags asm.relsub asm.section asm.section.col asm.section.sub asm.segoff asm.shortcut asm.size asm.slow asm.stackptr asm.strenc asm.symbol asm.symbol.col asm.syntax asm.tabs asm.tabsoff asm.tabsonce asm.trace asm.tracespace asm.ucase asm.vars asm.varsub asm.varsub_only asm.varsum asm.varxs asm.xrefs asm.strip asm.jmpsub</p>