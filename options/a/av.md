<!-- TITLE: av -->

# av
```
|Usage: av[?jr*] C++ vtables and RTTI
```
- `av        `  search for vtables in data sections and show results
- `avj       `  like av, but as json
- `av*       `  like av, but as r2 commands
- `avr[@addr]`  try to parse RTTI at vtable addr (see anal.cpp.abi)
- `avra      `  search for vtables and try to parse RTTI at each of them