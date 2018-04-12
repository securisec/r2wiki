<!-- TITLE: aa -->

#  `aa[?]` analyze all (fcns + bbs) (aa0 to avoid sub renaming)

- `aa` alias for 'af@@ sym.\*;af@entry0;afva'
	- > `aa` analyze all public symbols. The aa command analyzes all flags starting with sym. (symbols/function names) and entry0 (i.e. \_start, the program’s entry point)
- `aa*` analyze all flags starting with sym. (af @@ sym.*)
- `aaa[?]` autoname functions after aa (see afna)
- `aab` aab across io.sections.text
  - > `aab` Looks for executable sections and looks for calls. when it finds a call, it looks for the destination of the call. Splits up basic blocks, and tries to remove all the false positives
- `aac [len]` analyze function calls (af @@ \`pi len~call[1]\` ) _Identify functions by following calls_
	- > `aac` analyze all call destinations as functions
- `aac* [len]` flag function calls without performing a complete analysis
- `aad [len]` analyze data references to code
- `aae [len] ([addr])` analyze references with ESIL (optionally to address) _Emulate code to identify new pointer references_
  - > `aae` Analyzes executable sections but using emulation. Useful for calls that are using registers instead of hardcoded destinations
- `aaf`                 analyze all functions (e anal.hasnext=1;afr @@c:isq)
- `aaE` run aef on all functions (same as aef @@f)
- `aai[j]` show info of all analysis parameters
- `aan` autoname functions that either start with fcn.* or sym.func.*
- `aap` find and analyze function preludes
[ `aar[?] [len]` analyze len bytes of instructions for references](/options/a/aa/aar)
- `aas [len]` analyze symbols (af @@= \`isq~[0]\` )
	- > `aas` Use binary header information to find public functions 
- `aat [len]` analyze all consecutive functions in section. _Assume functions are consecutive_
- `aaT [len]` analyze code after trap-sleds
- `aau [len]` list mem areas (larger than len bytes) not covered by functions
- `aav [sat]` find values referencing a specific section or map
  - > `aav` Looks for values in the text section that are pointing to the text section. Shows hardcoded pointers in program memory.

<p hidden>aa aa* aaa aab aac aac* aad aae aaE aai aan aap aar aas aat aaT aau aav aaf</p>