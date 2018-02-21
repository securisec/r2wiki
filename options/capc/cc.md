<!-- TITLE: CC -->

#  `CC[?] [-] [comment-text] [@addr]` add/remove comment


```
Usage: CC[-+!*au] [base64:..|str] @ addr
```


- `CC` list all comments in human friendly form 
	> 🚀 Use `CC` to insert comments [asciinema](https://asciinema.org/a/Re42NaTrEYUuu5RseVhA8a7Qp)
- `CC*` list all comments in r2 commands
- `CC.` show comment at current offset
- `CC, [file]` show or set comment file
- `CC [text]` append comment at current address
- `CCf` list comments in function
- `CC+ [text]` append comment at current address
	- 🚀 `CC+` may be used to add multiline comments using r2pipe [asciinema](https://asciinema.org/a/wArUQELJApjnDF77pz3MbuZGz)
- `CC!` 🚀 edit comment using cfg.editor (vim, ..) [asciinema](https://asciinema.org/a/vTZQP8lnl6qEw9dZKLvOC7EHV)
- `CC- @ cmt_addr` remove comment at given address
- `CCu good boy @ addr` add good boy comment at given address
- `CCu base64:AA== @ addr` add comment in base64

<p hidden>CC CC* CC. CCf CC+ CC! CC- CCu</p>