<!-- TITLE: / Search -->

#  `/` Search for bytes, regexps, patterns, ..


```text
Usage: /[!bf] [arg]Search stuff (see 'e??search' for options)
Use io.va for searching in non virtual addressing spaces
```


## **Tips**
  - To search for hexadecimal representation of a string, prepend the string with a `\x` . For example, `/ \xELF` will search for the hexadecimal represenation of ELF
- `/ foo\x00` 🚀 search for string 'foo\0' [asciinema](https://asciinema.org/a/Ecgm3K7peRKclEFWGM9fZyGrj)
- `/j foo\x00` 🚀 search for string 'foo\0' (json output) [asciinema](https://asciinema.org/a/UeE0hZZxMWzni2Fgq2Mc4xIJ5)
- `/! ff` search for first occurrence not matching, command modifier
- `/!x 00` inverse hexa search (find first byte != 0x00)
- `/+ /bin/sh` 🚀 construct the string with chunks [asciinema](https://asciinema.org/a/BPv5byYzyLrDoO2FxE1XR8tkX)
- `//` repeat last search
- `/a jmp eax` assemble opcode and search its bytes
  - > 🚀 Example: `/a jmp eax` [asciinema](https://asciinema.org/a/r9lxscaovPgJ2nS4d7AVnr0ne)

- `/A jmp` 🚀 find analyzed instructions of this type _(/A? for help)_ [asciinema](https://asciinema.org/a/QEjFcFC3eBjWRlUy2RseQigom)
- `/b` search backwards, command modifier, followed by other command
- `/B` search recognized RBin headers

- [ `/c jmp [esp]` search for asm code matching the given string](search/c)

- `/ce rsp,rbp` search for esil expressions matching

- [ `/C[ar]` search for crypto materials](search/capc)

- `/d 101112` search for a deltified sequence of bytes
- `/e /E.F/i` search/match regular expression
- `/E esil-expr` offset matching given esil expressions %%= here
- `/f` search forwards, command modifier, followed by other command
- `/F file [off] [sz]` search contents of file with offset and size
- `/h[t] [hash] [len]` find block matching this hash. See /#?
- `/i foo` 🚀 search for string 'foo' ignoring case [asciinema](https://asciinema.org/a/JbReEd7wnDvUIHexYr97UX5BZ)
- `/m magicfile` search for matching magic file (use blocksize)
  - > 🚀 Use this to search for magic headers inside the binary. Similar to foremost. Example (pcap): [asciinema](https://asciinema.org/a/gYd0YHsXdGx2xxgjTQh9FfMWa)

	- > Use `/m` to look for magic signatures at every offset. This can be defined with `search.in`. `/m` can be used to identify files in memory as an example.
- `/me` Doesnt really do anything 😕
- `/M` search for known filesystems and mount them automatically
- `/o [n]` show offset of n instructions backward
- `/p patternsize` 🚀 search for pattern of given size [asciinema](https://asciinema.org/a/rNuauFEXAHI11e9f6E5ByZpcS)
- `/P patternsize` 🚀 search similar blocks [asciinema](https://asciinema.org/a/8Pofps1JKB7gSSeuUdLBrfK3U)

- [ `/r[erwx][?] sym.printf` analyze opcode reference an offset (/re for esil)](search/r)

- [ `/R [grepopcode]` search for matching ROP gadgets, semicolon-separated](search/cap_r)

- `/s` search for all syscalls in a region (EXPERIMENTAL)
- `/v[1248] value` look for an `cfg.bigendian` 32bit value
- `/V[1248] min max` look for an `cfg.bigendian` 32bit value in range
- `/w foo` search for wide string 'f\0o\0o\0'
- `/wi foo` search for wide string ignoring case 'f\0o\0o\0'

- [ `/x ff..33` search for hex string ignoring some nibbles](search/x)

- `/z min max` search for strings of given size