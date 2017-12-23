<!-- TITLE: pf Format Characters -->

#  **`pf??`** Format characters


```text
|pf: pf[.k[.f[=v]]|[v]]|[n]|[0|cnt][fmt] [a0 a1 ...]
```

- Format: 
		- `b` byte (unsigned)
		- `B` resolve enum bitfield (see t?)
		- `c` char (signed byte)
		- `d` 0x%%08x hexadecimal value (4 bytes) (see %%i and %%x)
		- `D` disassemble one opcode
		- `e` temporally swap endian
		- `E` resolve enum name (see t?)
		- `f` float value (4 bytes)
		- `i` %%i signed integer value (4 bytes) (see %%d and %%x)
		- `n` next char specifies size of signed value (1, 2, 4 or 8 byte(s))
		- `N` next char specifies size of unsigned value (1, 2, 4 or 8 byte(s))
		- `o` 0x%%08o octal value (4 byte)
		- `p` pointer reference (2, 4 or 8 bytes)
		- `q` quadword (8 bytes)
		- `r` CPU register `pf r (eax)plop`
		- `s` 32bit pointer to string (4 bytes)
		- `S` 64bit pointer to string (8 bytes)
		- `t` UNIX timestamp (4 bytes)
		- `T` show Ten first bytes of buffer
		- `u` uleb128 (variable length)
		- `w` word (2 bytes unsigned short in hex)
		- `x` 0x%%08x hex value and flag (fd @ addr) (see %%d and %%i)
		- `X` show formatted hexpairs
		- `z` \0 terminated string
		- `Z` \0 terminated wide string
		- `?` data structure `pf ? (struct_name)example_name`
		- `*` next char is pointer (honors asm.bits)
		- `+` toggle show flags for each offset
		- `:` skip 4 bytes
		- `.` skip 1 byte