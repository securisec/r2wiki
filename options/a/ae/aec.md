#  `aec[?]`   continue until ^C

- `aec`   Continue until exception
- `aecs`   Continue until syscall
	> Use `aecs [number]` to continue until that syscall number
		- [Linux 64 bit system calls](https://filippo.io/linux-syscall-table/)
		- [Linux 32 bit system calls](https://syscalls.kernelgrok.com/)
- `aecu[addr]`   Continue until address
- `aecue[addr]`   Continue until esil expression

<p hidden>aec aecs aecu aecue</p>