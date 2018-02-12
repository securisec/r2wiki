<!-- TITLE: ! -->

#  `!` Run given command as in system(3)


```text
Usage: !<cmd> Run given command as in system(3)
```

- `!` list all historic commands
- `!ls` execute 'ls' in shell
- `!!` save command history to hist file
- `!!ls~txt` print output of 'ls' and grep for 'txt'
- `.!rabin2 -rpsei ${FILE}` run each output line as a r2 cmd
- `!echo $SIZE` display file size
- `!-` clear history in current session
- `!-*` clear and save empty history log
- `!=!` enable remotecmd mode
- `=!=` disable remotecmd mode

## Environment

```text
| R2_FILE file name
| R2_OFFSET 10base offset 64bit value
| R2_BYTES TODO: variable with bytes in curblock
| R2_XOFFSET same as above, but in 16 base
| R2_BSIZE block size
| R2_ENDIAN 'big' or 'little'
| R2_IOVA is io.va true? virtual addressing (1,0)
| R2_DEBUG debug mode enabled? (1,0)
| R2_BLOCK TODO: dump current block to tmp file
| R2_SIZE file size
| R2_ARCH value of asm.arch
| R2_BITS arch reg size (8, 16, 32, 64)
| RABIN2_LANG assume this lang to demangle
| RABIN2_DEMANGLE demangle or not
| RABIN2_PDBSERVER e pdb.server
```

<p hidden>!ls</p>