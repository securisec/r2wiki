<!-- TITLE: b -->

#  **`b`** Display or change the block size


```text
Usage: b[f] [arg]
    Get/Set block size
```


- **`b`** display current block size
	> Change the block size with `b <block-size>`. In visual mode you can also enter radare2 command pressing the `:` key (like vi does)
- **`b 33`** set block size to 33
- **`b+3`** increase blocksize by 3
- **`b-16`** decrease blocksize by 16
- **`b eip+4`** numeric argument can be an expression
- **`bf foo`** set block size to flag size
- **`bm 1M`** set max block size

<p hidden>b b- b+ bf bm</p>