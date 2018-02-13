<!-- TITLE: Cf -->

#  `Cf[?][-] [sz] [0|cnt][fmt] [a0 a1...] [@addr]` format memory (see pf?)


```text
Usage: Cf[-] [sz] [fmt..] [@addr]

'sz' indicates the byte size taken up by struct.
'fmt' is a 'pf?' style format string. It controls only the display format.

You may wish to have 'sz' != sizeof(fmt) when you have a large struct
but have only identified specific fields in it. In that case, use 'fmt'
to show the fields you know about (perhaps using 'skip' fields), and 'sz'
to match the total struct size in mem.
```
