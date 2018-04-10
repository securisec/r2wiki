<!-- TITLE: cu -->

#  `cu[?] [addr] @at` Compare memory hexdumps of $$ and dst in unified diff


```
Usage: cu [offset]# Creates a unified hex patch
```


- `cu $$+1 > p` Compare current seek and +1
- `cu1 $$+1 > p`  Compare bytes from current seek and +1
- `cu2 $$+1 > p`  Compare words (half, 16bit) from current seek and +1
- `cu4 $$+1 > p`  Compare dwords from current seek and +1
- `cu8 $$+1 > p`  Compare qwords from current seek and +1
- `cud $$+1 > p` Compare disasm current seek and +1
- `wu p` Apply unified hex patch

<p hidden>cu cud wu</p>