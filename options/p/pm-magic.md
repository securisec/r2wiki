<!-- TITLE: pm -->

#  `pm[?] [magic]` print libmagic data (see pm? and /m?)


```text
|Usage: pm [file|directory]
    | r_magic will use given file/dir as reference
    | output of those magic can contain expressions like:
    | foo@0x40 # use 'foo' magic file on address 0x40
    | @0x40 # use current magic file on address 0x40
    | \n # append newline
    | e dir.magic # defaults to /home/ubuntu/bin/prefix/radare2//share/radare2/2.1.0-git/magic
    | /m # search for magic signatures
```
