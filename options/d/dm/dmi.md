<!-- TITLE: dmi -->

#  `dmi [addr|libname] [symname]` List symbols of target lib


```text
Usage: dmi # List/Load Symbols
```


- `dmi[libname] [symname]` List symbols of target lib
	> Example: `dmi libc puts`
- `dmi*` List symbols of target lib in radare commands
- `dmi.` List closest symbol to the current address
- `dmiv` Show address of given symbol for given lib

<p hidden>dmi dmi* dmi. dmiv</p>