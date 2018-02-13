<!-- TITLE: wo -->

#  `wo[?] hex` write in block with operation. 'wo?' fmi


```text
Usage: wo[asmdxoArl24] [hexpairs] @ addr[!bsize]
```


- `wo[24aAdlmorwx]` without hexpair values, clipboard is used
- `wo2 [val]` 2= 2 byte endian swap
- `wo4 [val]` 4= 4 byte endian swap
- `woa [val]` += addition (f.ex: woa 0102)
- `woA [val]` &= and
- `wod [val]` /= divide
- `woD[algo] [key] [IV]` decrypt current block with given algo and key
- `woe [from to] [step] [wsz=1] ..` create sequence
  > _Example: `woe 42 3 @ edi!32` This will write a pattern from 42, increment by 3, onto edi. The `!` means size. So what offset to write till_
- `woE [algo] [key] [IV]` encrypt current block with given algo and key
- `wol [val]` <<= shift left
- `wom [val]` *= multiply
- `woo [val]` |= or
- [`wop[DO] [arg]` De Bruijn Patterns](/options/w/wo-hex-write/wop)
- `wor [val]` >>= shift right
- `woR` random bytes (alias for 'wr $b')
- `wos [val]` -= substraction
- `wow [val]` == write looped value (alias for 'wb')
- `wox [val]` ^= xor (f.ex: wox 0x90)
  > _This can be used to xor using registers. Example: `wox `p8 32 @ edi` @ eax!32`. This command will take 32 bytes in hex from edi and then xor eax till 32 bytes_

  [Memory Manipulation · Radare2 Explorations](https://monosource.gitbooks.io/radare2-explorations/content/tut2/tut2_-_mem_manip.html)
	
	<p hidden>wo wo2 wo4 woa woA wod woD woe woE wol wom woo wop wor woR wos wow wox</p>