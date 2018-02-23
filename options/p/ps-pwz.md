<!-- TITLE: ps -->

#  `ps[?][pwz] [len]` print pascal/wide/zero-terminated strings


```
Usage: ps[zpw+] [N]Print String
```


- `ps` print string
  - > _Use `ps @ [register]` to print string representation of addresses pointed to by a register_
- `psb` print strings in current block
- `psi` print string inside curseek
- `psj` print string in JSON format
- `psp` print pascal string
- `pss` print string in screen (wrap width)
- `psu` print utf16 unicode (json)
- `psw` print 16bit wide string
- `psW` print 32bit wide string
- `psx` show string with escaped chars
- `psz` print zero-terminated string
- `ps+` print libc++ std::string (same-endian, ascii, zero-terminated)

<p hidden>ps psb psi psj psp pss psu psw psW psx psz ps+</p>