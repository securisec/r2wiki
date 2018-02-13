<!-- TITLE: dp -->

#  `dp[?]` List, attach to process or thread id


```text
Usage: dp # Process commands
```


- `dp` List current pid and children
- `dp <pid>` List children of pid
- `dp*` List all attachable pids
- `dp- <pid>` Detach select pid
- `dp=<pid>` Select pid
- `dpa <pid>` Attach and select pid
- `dpc` Select forked pid (see dbg.forks)
- `dpc*` Display forked pid (see dbg.forks)
- `dpe` Show path to executable. Show file path
- `dpf` Attach to pid like file fd // HACK
- `dpk <pid> [<signal>]` Send signal to process (default 0)
- `dpn` Create new process (fork)
- `dptn` Create new thread (clone)
- `dpt` List threads of current pid
- `dpt <pid>` List threads of process
- `dpt=<thread>` Attach to thread

<p hidden>dp dp* dp- dp= dpa dpc dpc* dpe dpf dpk dpn dptn dpt dpt=</p>