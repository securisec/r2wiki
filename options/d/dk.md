<!-- TITLE: dk -->

#  **`dk[?]`** List, send, get, set, signal handlers of child


```text
Usage: dk Signal commands
```


- **`dk`** List all signal handlers of child process
- **`dk <signal>`** Send KILL signal to child
- **`dk <signal>=1`** Set signal handler for <signal> in child
- **`dk?<signal>`** Name/signum resolver

- [ **`dko[?] <signal>`** Reset skip or cont options for given signal](/options/d/dk/dko)

- **`dko <signal> [|skip|cont]`** On signal SKIP handler or CONT into
- **`dkj`** List all signal handlers in JSON

<p hidden>dk dk? dko dkj</p>