<!-- TITLE: d -->

#  `d` Debugger commands
## `d` commands

- [ `db[?]` Breakpoints commands](/options/d/db) _debug breakpoint_

- [ `dbt[?]` Display backtrace based on dbg.btdepth and dbg.btalgo](/options/d/dbt) _debug backtrace_

- [ `dc[?]` Continue execution](/options/d/dc) _debug continue_

- [ `dd[?]` File descriptors (!fd in r1)](/options/d/dd) _debug descriptors_

- [ `de[-sc] [rwx] [rm] [e]` Debug with ESIL (see de?)](/options/d/de) _debug esil_

- `dg <file>` Generate a core-file (WIP)
- `dH [handler]` Transplant process to a new handler

- [ `di[?]` Show debugger backend information (See dh)](/options/d/di)

- [ `dk[?]` List, send, get, set, signal handlers of child](/options/d/dk)

- `dL [handler]` List or set debugger handler _debug handler_

- [ `dm[?]` Show memory maps](/options/d/dm) _debug memory maps_

- [ `do[?]` Open process (reload, alias for 'oo')](/options/d/do) _debug open_

- `doo[args]` Reopen in debugger mode with args (alias for 'ood') _debug open args_

- [ `dp[?]` List, attach to process or thread id](/options/d/dp)

- [ `dr[?]` Cpu registers](/options/d/dr) _debug registers_

- [ `ds[?]` Step, over, source line](/options/d/ds) _debug step_

- [ `dt[?]` Display instruction traces (dtr=reset)](/options/d/dt) _debug traces_

- `dw <pid>` Block prompt until pid dies

- [ `dx[?]` Inject and run code on target process (See gs)](/options/d/dx)

## Examples
- [Helpful debug usage examples](/home/misc/usage-examples#debug)

<p hidden>db dbt dc dd de dg dH di dk dL dm do doo dp dr ds dt dw dx</p>