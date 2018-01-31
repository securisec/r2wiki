<!-- TITLE: o -->

#  `o` Open file at optional address


```text
Usage: o [com- ] [file] ([offset])
```


- `o` 🚀 list opened files [asciinema](https://asciinema.org/a/XAlBcowKXudg4lI7E5Dr0rfD8)
- `oa[-] [A] [B] [filename]` Specify arch and bits for given file
- `oq` list all open files
- `o*` list opened files in r2 commands
- `o. [len]` open a malloc://[len] copying the bytes from current offset
- `o=` 🚀 list opened files (ascii-art bars) [asciinema](https://asciinema.org/a/Cq5s8dAZiEa9s636trnuFMR5j)

- [ `ob[?] [lbdos] [...]` list opened binary files backed by fd](/options/o/ob)

- `oc [file]` 🚀 open core file, like relaunching r2 [asciinema](https://asciinema.org/a/zSNftbFNgzX6h4sU3TlijkSxf)
- `oi[-|idx]` alias for o, but using index instead of fd

- [ `oj[?]` list opened files in JSON format](/options/o/oj)

- `oL[j]` list all IO plugins registered

- [ `om[?]` create, list, remove IO maps](/options/o/om)

- [`on [file] 0x4000` map raw file at 0x4000 (no r_bin involved)](/options/o/on)

- [ `oo[?]` reopen current file (kill+fork in debugger)](/options/o/oo_question)

- `oo+` reopen current file in read-write
  > _This is a substitute for `-w` as a paramter when opening the file_
- `ood [args]` reopen in debugger mode (with args)

- [ `oo[bnm] [...]` see oo? for help](/options/o/oo)

- `op [fd]` priorize given fd (see also ob)
- `o 4` Switch to open file on fd 4
- `o-1` close file descriptor 1
- `o-*` close all opened files
- `o-!` close all files except the current one
- `o--` close all files, analysis, binfiles, flags, same as !r2 --
- `o [file]` open [file] file in read-only
- `o+ [file]` open file in read-write mode
- `o [file] 0x4000` map file at 0x4000
- `ox fd fdx` exchange the descs of fd and fdx and keep the mapping

<p hidden>oa oq o=ob oc oi oj oL om on oo oo+ ood op ox o-!</p>