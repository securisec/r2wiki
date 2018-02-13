<!-- TITLE: R -->

#  `/R [grepopcode]` search for matching ROP gadgets, semicolon-separated

- `/R [filter-by-string]` Show gadgets
- `/R/ [filter-by-regexp]` Show gadgets [regular expression]
- `/Rl [filter-by-string]` Show gadgets in a linear manner
- `/R/l [filter-by-regexp]` Show gadgets in a linear manner [regular expression]
- `/R/j [filter-by-regexp]` JSON output [regular expression]
- `/Rk [select-by-class]` Query stored ROP gadgets
  - `/Rk [nop|mov|const|arithm|arithm_ct]` Show gadgets
  - `/Rkj` JSON output
  - `/Rkq` List Gadgets offsets