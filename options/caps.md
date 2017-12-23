<!-- TITLE: S -->

#  **`S`** Io section manipulation information


```text
Usage: S[?-.*=adlr] [...]
```


- **`S`** list sections
- **`S paddr va sz [vsz] name rwx`** add new section (if(!vsz)vsz=sz)
- **`S.`** show current section name
- **`S.-*`** remove all sections in current offset
- **`S*`** list sections (in radare commands)
- **`S-[id]`** remove section identified by id
- **`S-.`** remove section at core->offset (can be changed with @)
- **`S=`** list sections (ascii-art bars) (io.va to display paddr or vaddr)
- **`Sa[-] [A] [B] [[off]]`** Specify arch and bits for given section
- **`Sd[a] [file]`** dump current (all) section to a file (see dmd)
- **`Sf [baddr]`** Alias for S 0 0 $s $s foo mrwx
- **`Sj`** list sections in JSON (alias for iSj)
- **`Sl [file]`** load contents of file into current section (see dml)
- **`Sr [name]`** rename section on current seek

- [ **`SR[?]`** Remap sections with different mode of operation](/options/caps/SR)