<!-- TITLE: p= -->

#  **`p=[?][bep] [blks] [len] [blk]`** show entropy/printable chars/chars bars


```text
Usage: p=[=bep?][qj] [nblocks] ([len]) ([offset]) show entropy/printable chars/chars bars
```


- **`p=`** print bytes of current block in bars
- **`p==[..]`** same subcommands as p=, but using flame column graph instead of rows
- **`p=b`** same as above
- **`p=c`** print number of calls per block
- **`p=d`** print different bytes from block
- **`p=e`** print entropy for each filesize/blocksize
  > `p=e` _Entropy computation_
- **`p=F`** print number of 0xFF bytes for each filesize/blocksize
- **`p=i`** print number of invalid instructions per block
- **`p=j`** print number of jumps and conditional jumps in block
- **`p=m`** print number of flags and marks in block
- **`p=p`** print number of printable bytes for each filesize/blocksize
- **`p=s`** print number of syscall and priviledged instructions
- **`p=z`** print number of chars in strings in block
- **`p=0`** print number of 0x00 bytes for each filesize/blocksize

<p hidden>p= p== p=b p=c p=d p=e p=F p=i p=j p=m p=p p=s p=z p=0</p>