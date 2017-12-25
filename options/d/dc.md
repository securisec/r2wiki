<!-- TITLE: dc -->

#  **`dc[?]`** Continue execution


```text
Usage: dc Execution continuation commands
```


- **`dc`** Continue execution of all children
- **`dc <pid>`** Continue execution of pid
- **`dc[-pid]`** Stop execution of pid
- **`dca [sym] [sym].`** Continue at every hit on any given symbol
- **`dcb`** Continue back until breakpoint
- **`dcc`** Continue until call (use step into)
- **`dccu`** Continue until unknown call (call reg)
- **`dcf`** Continue until fork (TODO)
- **`dck <signal> <pid>`** Continue sending signal to process
- **`dco <num>`** Step over <num> instructions
- **`dcp`** Continue until program code (mapped io section)
- **`dcr`** Continue until ret (uses step over)

- [ **`dcs[?] <num>`** Continue until syscall](/options/d/dc/dcs)

- **`dct <len>`** Traptrace from curseek to len, no argument to list

- [ **`dcu[?] [..end|addr] ([end])`** Continue until address (or range)](/options/d/dc/dcu) _debug continue until_

<p hidden>dc dca dcb dcc dccu dcf dck dco dcp dcr dcs dct dcu</p>