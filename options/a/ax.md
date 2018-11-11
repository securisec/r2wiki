<!-- TITLE: ax -->

#  `ax[?]`   manage refs/xrefs (see also afx?)

Usage: ax[?d-l*] # see also 'afx?'

- `ax addr [at]` add code ref pointing to addr (from curseek)
- `axc addr [at]` add code jmp ref // unused?
- `axC addr [at]` add code call ref
- `axg addr` show xrefs graph to reach current function
- `axgj [addr]` show xrefs graph to reach current function in json format
- `axd addr [at]` add data ref
- `axq` list refs in quiet/human-readable format
- `axj` list refs in json format
- `axF [flg-glob]` find data/code references of flags
- `axt [addr]` find data/code references to this address xref to

   - > Example use case is `axt @@ str.*` to look for xrefs to all strings_ 
- `axtg`
- `axf [addr]` find data/code references from this address xref from
- `axff` xrefs from function
- `ax- [at]` clean all refs (or refs from addr)
- `ax` list refs
- `axk [query]` perform sdb query
- `ax*` output radare commands

<p hidden>ax axc axC axg axd axq axj axF axt axf ax- axk ax* axgj</p>