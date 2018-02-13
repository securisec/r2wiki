<!-- TITLE: dbt -->

#  `dbt[?]` Display backtrace based on dbg.btdepth and dbg.btalgo


```text
Usage: dbt # Backtrace commands
```


- `dbt` Display backtrace based on dbg.btdepth and dbg.btalgo
- `dbt*` Display backtrace in flags
- `dbt=` Display backtrace in one line (see dbt=s and dbt=b for sp or bp)
- `dbtj` Display backtrace in JSON
- `dbta` Display ascii-art representation of the stack backtrace
![dbta](/uploads/small-d/dbta.png) {:height="50%" width="50%"}
- `dbte <addr>` Enable Breakpoint Trace
- `dbtd <addr>` Disable Breakpoint Trace
- `dbts <addr>` Swap Breakpoint Trace

<p hidden>dbt dbt* dbt= dbtj dbta dbte dbtd dbts</p>
