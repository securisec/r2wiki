<!-- TITLE: ob -->

#  `ob[?] [lbdos] [...]` list opened binary files backed by fd


```
Usage: ob # List open binary files backed by fd
```


- `ob` List opened binary files and objid
- `ob*` List opened binary files and objid (r2 commands)
- `ob [fd objid]` Switch to open binary file by fd number and objid
- `oba [addr]` Open bin info from the given address
	- The `[addr]` in `oba` is the base address of the binary being analyzed
- `oba [addr] [filename]` Open file and load bin info at given address
- `obb [fd]` Switch to open binfile by fd number
- `obj` List opened binary files and objid (JSON format)
- `obr [baddr]` Rebase current bin object
- `ob- [fd]` Delete binfile by fd
- `obd [objid]` Delete binary file by objid. Do nothing if only one loaded.
- `obo [objid]` Switch to open binary file by objid
- `obq`

<p hidden>ob ob* oba oba obb obj obr ob- obd obo obq</p>