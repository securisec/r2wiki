<!-- TITLE: io -->

# io

- **`io.0xff`** Use this value instead of 0xff to fill unallocated areas _Default is 255_
- **`io.aslr`** Disable ASLR for spawn and such _Default is false_
- **`io.autofd`** Change fd when opening a new file _Default is true_
- **`io.buffer`** Load and use buffer cache if enabled _Default is false_
- **`io.buffer.from`** Lower address of buffered cache _Default is 0_
- **`io.buffer.to`** Higher address of buffered cache _Default is 0_
- **`io.cache`** Change both of io.cache.{read,write} _Default is false_
  > _This can be changed if the binary is in read only mode and ESIL or emulation is desired_

  > _This allows writing on memory if the file wasnt opened in write mode_
- **`io.cache.read`** Enable read cache for vaddr (or paddr when io.va=0) _Default is false_
- **`io.cache.write`** Enable write cache for vaddr (or paddr when io.va=0) _Default is false_
- **`io.exec`** See !!r2 -h~-x _Default is true_
- **`io.ff`** Fill invalid buffers with 0xff instead of returning error _Default is true_
- **`io.pcache`** io.cache for p-level _Default is false_
- **`io.pcache.read`** Enable read-cache _Default is false_
- **`io.pcache.write`** Enable write-cache _Default is false_
- **`io.va`** Use virtual address layout _Default is true_

<p hidden>io.0xff io.aslr io.autofd io.buffer io.buffer.from io.buffer.to io.cache io.cache.read io.cache.write io.exec io.ff io.pcache io.pcache.read io.pcache.write io.va</p>