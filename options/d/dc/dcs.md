<!-- TITLE: dcs -->

#  `dcs[?] <num>` Continue until syscall


```
Usage: dcs Continue until syscall
```


- `dcs` Continue until next syscall
   - > _Example `dcs strcmp` to continue till strcmp is called_ 
- `dcs [str]` Continue until next call to the 'str' syscall
- `dcs*` Trace all syscalls, a la strace

<p hidden>dcs dcs*</p>