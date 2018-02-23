<!-- TITLE: as -->

#  `as[?] [num]`   analyze syscall using dbg.reg

Usage: as[ljk?] syscall name <-> number utility

- `as` show current syscall and arguments
- `as 4` show syscall 4 based on asm.os and current regs/mem
- `asc[a] 4` dump syscall info in .asm or .h
- `asf [k[=[v]]]` list/set/unset pf function signatures (see fcnsign)
- `asj` list of syscalls in JSON

   - > Dump the whole syscall database

- `asl` list of syscalls by asm.os and asm.arch
- `asl close` returns the syscall number for close
- `asl 4` returns the name of the syscall number 4
- `ask [query]` perform syscall/ queries