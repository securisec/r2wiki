<!-- TITLE: dc -->

#  `dc[?]` Continue execution


```
Usage: dc Execution continuation commands
```


- `dc` Continue execution of all children
	> `dc < /path/to/multiline` to insert multiple inputs
- `dc <pid>` Continue execution of pid
- `dc[-pid]` Stop execution of pid
- `dca [sym] [sym].` Continue at every hit on any given symbol
- `dcb` Continue back until breakpoint _debug continue breakpoint_
	> `dcb` Similar to `dsb` but instead of setting back, it will continue back till breakpoint
- `dcc` Continue until call (use step into) _debug continue call_
- `dccu` Continue until unknown call (call reg)
- `dcf` Continue until fork (TODO) _debug continue fork_
- `dck <signal> <pid>` Continue sending signal to process
- `dco <num>` Step over <num> instructions _debug step over_
- `dcp` Continue until program code (mapped io section) _debug continue program code_
- `dcr` Continue until ret (uses step over) _debug continue ret_

- [ `dcs[?] <num>` Continue until syscall](/options/d/dc/dcs) _debug continue syscall_

- `dct <len>` Traptrace from curseek to len, no argument to list

- [ `dcu[?] [..end|addr] ([end])` Continue until address (or range)](/options/d/dc/dcu) _debug continue until_

<p hidden>dc dca dcb dcc dccu dcf dck dco dcp dcr dcs dct dcu</p>