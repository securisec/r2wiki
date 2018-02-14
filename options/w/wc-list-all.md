<!-- TITLE: wc -->

#  `wc` list all write changes


```
Usage: wc[ir+-*?] # NOTE: Uses io.cache=true
```


- `wc` list all write changes
- `wc- [from] [to]` remove write op at curseek or given addr
- `wc+ [addr]` commit change from cache to io
- `wc*` "" in radare commands
- `wcr` reset all write changes in cache
- `wci` commit write cache
- `wcp [fd]` list all cached write-operations on p-layer for specified fd or current fd
- `wcp* [fd]` list all cached write-operations on p-layer in radare commands
- `wcpi [fd]` commit and invalidate pcache for specified fd or current fd

<p hidden>wc wc+ wc* wcr wci wcp wcp* wcpi</p>