<!-- TITLE: px -->

#  `px[?][owq] [len]` hexdump of N bytes (o=octal, w=32bit, q=64bit)


```
Usage: px[0afoswqWqQ][f] # Print heXadecimal
```


## Tips
  - > Use `px` to print memory. Example: `px 8 @ esp+4`

---

- `px` ⭐ show hexdump
  - Screenshot

    ![](/uploads/small-p/px.png)

- `px/` same as x/ in gdb (help x)
- `px0` 8bit hexpair list of bytes until zero byte
- `pxa` show annotated hexdump
  - Screenshot

    ![](/uploads/small-p/pxa.png)

- `pxA` show op analysis color map
- `pxb` dump bits in hexdump form
- `pxc` show hexdump with comments
- `pxd[124]` signed integer dump (1 byte, 2 and 4)
- `pxe` 🚀 emoji hexdump! :) [asciinema](https://asciinema.org/a/g15mRdZIIhC6Zj3vNbp0flwiX)
- `pxf` show hexdump of current function
- `pxh` show hexadecimal half-words dump (16bit)
- `pxH` same as above, but one per line
- `pxi` HexII compact binary representation
- `pxl` display N lines (rows) of hexdump
- `pxo` show octal dump
- `pxq` show hexadecimal quad-words dump (64bit)
- `pxQ` same as above, but one per line
- `pxr[j]` show words with references to flags and code
  > _Alternatively, consider using `afvd`_
  > _`pxr @ esp` stack analysis. This is also memory telescoping_
  - Screenshot

     Green/Blue is executable, Red is data White is value?

    ![](/uploads/small-p/pxr.png)

- `pxs` show hexadecimal in sparse mode
- `pxt[*.] [origin]` show delta pointer table in r2 commands
- `pxw` show hexadecimal words dump (32bit)
  - Screenshot

    ![](/uploads/small-p/pxw.png)

- `pxW` same as above, but one per line
  - Screenshot

    ![](/uploads/small-p/px-cap-w.png)

- `pxx` show N bytes of hex-less hexdump
- `pxX` show N words of hex-less hexdump


<p hidden>px px0 pxa pxA pxb pxc pxd pxe pxf pxh pxH pxi pxl pxo pxq pxQ pxr pxs pxt pxw pxW pxx pxX</p>
