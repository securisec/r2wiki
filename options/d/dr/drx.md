<!-- TITLE: drx -->

#  `drx[?]` Show all debug registers


```
Usage: drx Hardware breakpoints commands
Usage: drx n [address] [length] [rwx]
```


- `drx` List all (x86?) hardware breakpoints
- `drx <number> <address> <length> <perms>` Modify hardware breakpoint. \<perms\> could be r, w, x
	- > Example: `drx 1 [offset] x`
- `drx-<number>` Clear hardware breakpoint

<p hidden>drx</p>