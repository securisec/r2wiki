<!-- TITLE: c -->

#  **`c`** Compare block with given data


```text
Usage: c[?dfx] [argument] # Compare
```


- **`c [string]`** Compare a plain with escaped chars string
- **`c* [string]`** Compare a plain with escaped chars string (output r2 commands)
- **`c4 [value]`** Compare a doubleword from a math expression
- **`c8 [value]`** Compare a quadword from a math expression
- **`cat [file]`** Show contents of file (see pwd, ls)
- **`cc [at] [(at)]`** Compares in two hexdump columns of block size
- **`ccc [at] [(at)]`** Same as above, but only showing different lines
- **`ccd [at] [(at)]`** Compares in two disasm columns of block size
- **`cf [file]`** Compare contents of file at current seek

- [ **`cg[?] [o] [file]`** Graphdiff current file and [file]](/options/c/cg)

- **`cl|cls|clear`** Clear screen, (clear0 to goto 0, 0 only)

- [ **`cu[?] [addr] @at`** Compare memory hexdumps of $$ and dst in unified diff](/options/c/cu)

- **`cud [addr] @at`** Unified diff disasm from $$ and given address
- **`cv[1248] [addr] @at`** Compare 1,2,4,8-byte value

- [ **`cw[?] [us?] [...]`** Compare memory watchers](/options/c/cw)

- **`cx [hexpair]`** Compare hexpair string (use '.' as nibble wildcard)
- **`cx* [hexpair]`** Compare hexpair string (output r2 commands)
- **`cX [addr]`** Like 'cc' but using hexdiff output