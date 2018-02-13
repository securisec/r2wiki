<!-- TITLE: y -->

#  `y` Yank/paste bytes from/to memory


```text
Usage: y[ptxy] [len] [[@]addr] # See wd? for memcpy, same as 'yf'.
```


- `y` show yank buffer information (srcoff len bytes)
- `y 16` copy 16 bytes into clipboard
- `y 16 0x200` copy 16 bytes into clipboard from 0x200
- `y 16 @ 0x200` copy 16 bytes into clipboard from 0x200
- `yz` copy up to blocksize zero terminated string bytes into clipboard
- `yz 16` copy up to 16 zero terminated string bytes into clipboard
- `yz @ 0x200` copy up to blocksize zero terminated string bytes into clipboard from 0x200
- `yz 16 @ 0x200` copy up to 16 zero terminated string bytes into clipboard from 0x200
- `yp` print contents of clipboard
- `yx` print contents of clipboard in hexadecimal
- `ys` print contents of clipboard as string
- `yt 64 0x200` copy 64 bytes from current seek to 0x200
- `ytf file` dump the clipboard to given file
- `yf 64 0x200` file copy 64 bytes from 0x200 from file (opens w/ io), use -1 for all bytes
- `yfa file copy` copy all bytes from file (opens w/ io)
- `yy 0x3344` paste clipboard

<p hidden>yz yp yx ys yt ytf yf yfa yy</p>