<!-- TITLE: pf Usage Examples -->

#  `pf???` pf usage examples


```text
|pf: pf[.k[.f[=v]]|[v]]|[n]|[0|cnt][fmt] [a0 a1 ...]
```

- Examples: 
- pf 3xi foo bar 3-array of struct, each with named fields: 'foo' as hex, and 'bar' as int
- pf B (BitFldType)arg_name` bitfield type
- pf E (EnumType)arg_name` enum type
- pf.obj xxdz prev next size name Define the obj format as xxdz
- pf obj=xxdz prev next size name Same as above
- pf iwq foo bar troll Print the iwq format with foo, bar, troll as the respective names for the fields
- pf 0iwq foo bar troll Same as above, but considered as a union (all fields at offset 0)
- pf.plop ? (troll)mystruct Use structure troll previously defined
- pf 10xiz pointer length string Print a size 10 array of the xiz struct with its field names
- pf {integer}? (bifc) Print integer times the following format (bifc)
- pf [4]w[7]i Print an array of 4 words and then an array of 7 integers
- pf ic...?i foo bar "(pf xw yo foo)troll" yo Print nested anonymous structres
- pfn2 print signed short (2 bytes) value. Use N insted of n for printing unsigned values