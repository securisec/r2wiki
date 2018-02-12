R2WIKI
@@ Run A For Loop
DISCARD
SAVE CHANGES
|||||

<!-- TITLE: @@ Run A For Loop -->
#  `@@` Run a for loop
​
Repeat a command over a list of offsets
​
## Tips
  - Example: `wx 90 @@ /x80` . This will replace all hex 80 with hex 90
  - Use `@@` as a replacement for a for i in x loop (iterator). Example: `axt @@ str.*` will look for xref of all strings and return thier offsets.
---
- `x @@ sym.*` run 'x' over all flags matching 'sym.' in current flagspace
- `x @@dbt[abs]` run 'x' command on every backtrace address, bp or sp
- `x @@.file` run 'x' over the offsets specified in the file (one offset per line)
- `x @@=off1 off2 ..` manual list of offsets
  - > 🚀 `x@@=` Run query over multiple offsets [asciinema](https://asciinema.org/a/sxTpCSQUL1vkT9ByRRo5B03RT)
- `x @@/x 9090` temporary set cmd.hit to run a command on each search result
  - > ⭐ `@@/` Can be used to search and replace something. Usage in this case is `w mystring_replace @@/ mystring_to_search`
- `x @@k sdbquery` run 'x' on all offsets returned by that sdbquery
- `x @@t` run 'x' on all threads (see dp)
- `x @@b` run 'x' on all basic blocks of current function (see afb)
- `x @@i` run 'x' on all instructions of the current function (see pdr)
- `x @@f` run 'x' on all functions (see aflq)
- `x @@f:write` run 'x' on all functions matching write in the name
- `x @@s:from to step` run 'x' on all offsets from, to incrementing by step
- `x @@c:cmd` the same as @@=`` without the backticks
- `x @@=pdf~call[0]` run 'x' at every call offset of the current function
  - > 🚀⭐ `@@=` can be used to loop over the output of a command and run another command against it. [asciinema](https://asciinema.org/a/1Qj5SAUKbwA7lEzxsYCx6BKaL)
​
​
<p hidden>search and replace</p>
Powered by Wiki.js.
Home
Return to top