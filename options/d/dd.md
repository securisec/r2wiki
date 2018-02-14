<!-- TITLE: dd -->

#  `dd[?]` File descriptors (!fd in r1)


```
Usage: dd Descriptors commands
```


- `dd` List file descriptors
- `dd <file>` Open and map that file into the UI
- `dd-<fd>` Close stdout fd
- `dd*` List file descriptors (in radare commands)
- `dds <fd> <off>` Seek given fd)
- `ddd <fd1> <fd2>` Dup2 from fd1 to fd2
- `ddr <fd> <size>` Read N bytes from fd
- `ddw <fd> <hexpairs>` Write N bytes to fd

<p hidden>dd dd* dds ddd ddr ddw</p>