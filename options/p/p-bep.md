<!-- TITLE: p= -->

#  `p=[?][bep] [blks] [len] [blk]` show entropy/printable chars/chars bars


```
Usage: p=[=bep?][qj] [nblocks] ([len]) ([offset]) show entropy/printable chars/chars bars
```


- `e zoom.in`  specify range for zoom
- `p=` 🚀 print bytes of current block in bars [asciinema](https://asciinema.org/a/CEYLf91ddfojcRGFN2yE5b8R8)
- `p=2` short (signed int16) bars, good for waves
- `p==[..]` 🚀 same subcommands as p=, but using flame column graph instead of rows [asciinema](https://asciinema.org/a/tJuwNaafEYTbOZYT23ACWS6wR)
- `p=b` same as above
- `p=c` 🚀 print number of calls per block [asciinema](https://asciinema.org/a/tAzt1FyDyxaq9TlumjtTkJWWU)
- `p=d` 🚀 print different bytes from block [asciinema](https://asciinema.org/a/3vYU6pArHQEx6voq4FlJ9cvYQ)
- `p=e` 🚀 print entropy for each filesize/blocksize [asciinema](https://asciinema.org/a/Ipo7mpG9KvoeEpTOTV0hdjJ8v)
  - > `p=e` _Entropy computation_
- `p=F` 🚀 print number of 0xFF bytes for each filesize/blocksize [asciinema](https://asciinema.org/a/9r073JtRiKJe34R6myRBfbpqr)
- `p=i` 🚀 print number of invalid instructions per block [asciinema](https://asciinema.org/a/43N3DxTuCCLc81stfFhb68zKt)
- `p=j` 🚀 print number of jumps and conditional jumps in block [asciinema](https://asciinema.org/a/EXNFrJ1Zm6aS8wbgqS9SDK95k)
- `p=m` 🚀 print number of flags and marks in block [asciinema](https://asciinema.org/a/jwMhce3gH3GZsVRZYjKk8nU63)
- `p=p` 🚀 print number of printable bytes for each filesize/blocksize [asciinema](https://asciinema.org/a/0MLMZsf3PH1p859NDOHWJawCY)
- `p=s` 🚀 print number of syscall and priviledged instructions [asciinema](https://asciinema.org/a/4im9skg2X6vtuVX2KMdXY5rBe)
- `p=z` 🚀 print number of chars in strings in block [asciinema](https://asciinema.org/a/FVPFAe281MrZ6tZSJkaO2E9ia)
- `p=0` 🚀 print number of 0x00 bytes for each filesize/blocksize [asciinema](https://asciinema.org/a/P3Jg5TFb5rQWexShpouiJffo9)

<p hidden>p= p== p=b p=c p=d p=e p=F p=i p=j p=m p=p p=s p=z p=0</p>