<!-- TITLE: w -->

#  `w` Multiple write operations


```
Usage: w[x] [str] [<file] [<<EOF] [@addr]
```


- `w[1248][+-][n]` increment/decrement byte,word..
- `w foobar` write string 'foobar'
- `w0 [len]` write 'len' bytes with value 0x00
- `w6[de] base64/hex` write base64 [d]ecoded or [e]ncoded string

- [ `wa[?] push ebp` write opcode, separated by ';' (use '"' around the command)](/options/w/wa-push)
	- > Assemble opcodes with the `a` and `A` keys in visual mode, which are bindings to the `wa` and `wA` commands

- `waf file` assemble file and write bytes

- [ `wao[?] op` modify opcode (change conditional of jump. nop, etc)](/options/w/wao-op)

- [ `wA[?] r 0` alter/modify opcode at current seek (see wA?)](/options/w/wa-r-0)

- `wb 010203` fill current block with cyclic hexpairs
- `wB[-]0xVALUE` set or unset bits with given value

- [ `wc` list all write changes](/options/w/wc-list-all)

- `wc[?][ir*?]` write cache undo/commit/reset/list (io.cache)
- `wd [off] [n]` duplicate N bytes from offset at current seek (memcpy) (see y?)

- [ `we[?] [nNsxX] [arg]` extend write operations (insert instead of replace)](/options/w/we-nnsxx)
- `wf [start_position] [bytes] @ [offset]` Write from start position, the number of bytes at offset [Twitter](https://twitter.com/radareorg/status/971320354760216578)
- `wff -|file` write contents of file at current offset
- `wfs [from_address] [bytes] [@] [offset]` Swap from address N bytes to offset [Twitter](https://twitter.com/radareorg/status/971322252200378368)
- `wh r2` whereis/which shell command
- `wm f0ff` set binary mask hexpair to be used as cyclic write mask

- [ `wo[?] hex` write in block with operation. 'wo?' fmi](/options/w/wo-hex-write)

- [ `wp[?] -|file` apply radare patch file. See wp? fmi](/options/w/wp-file)

- `wr 10` write 10 random bytes
- `ws pstring` write 1 byte for length and then the string

- [ `wt[f][?] file [sz]` write to file (from current seek, blocksize or sz bytes)](/options/w/wt-f-file)

- `wts host:port [sz]` send data to remote host:port via tcp://
- `ww foobar` write wide string 'f\x00o\x00o\x00b\x00a\x00r\x00'

- [ `wx[?][fs] 9090` write two intel nops (from wxfile or wxseek)](/options/w/wx-fs)

- [ `wv[?] eip+34` write 32-64 bit value](/options/w/wv-eip)

- `wz string` write zero terminated string (like w + \x00)

<p hidden>w0 w6 wa waf wao wA wb wB wc wd we wf wh wm wo wp wr ws wts ww wx wv wz</p>