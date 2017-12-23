<!-- TITLE: we -->

#  **`we[?] [nNsxX] [arg]`** extend write operations (insert instead of replace)


```text
Usage: write extend
```


- **`wen <num>`** insert num null bytes at current offset
- **`weN <addr> <len>`** insert bytes at address
- **`wes <addr> <dist> <block_size>`** shift a blocksize left or write in the editor
- **`wex <hex_bytes>`** insert bytes at current offset
- **`weX <addr> <hex_bytes>`** insert bytes at address

<p hidden>wen weN wes wex weX</p>