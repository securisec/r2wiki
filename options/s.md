<!-- TITLE: s -->

#  `s` Seek to address (also for '0x', '0x1' == 's 0x1')


```text
Usage: s # Help for the seek commands. See ?$? to see all variables
```


- `s` Print current address
- `s*`   Show seek history
- `s:pad` Print current address with N padded zeros (defaults to 8)
- `s addr` Seek to address
- `s-` Undo seek
- `s-*` Reset undo seek history
- `s- n` Seek n bytes backward
- `s--[n]` Seek blocksize bytes backward (/=n)
- `s+` Redo seek
- `s+ n` Seek n bytes forward
- `s++[n]` Seek blocksize bytes forward (/=n)
- `s[j*=!]` List undo seek history (JSON, =list, *r2, !=names, s==)
	- `sj` to retrive seek history in json format
- `s/ DATA` Search for next occurrence of 'DATA'
  - > `s/` This will also seek to the address of the first match
- `s/x 9091` Search for next occurrence of \x90\x91
- `s.hexoff` Seek honoring a base from core->offset
- `sa [[+-]a] [asz]` Seek asz (or bsize) aligned to addr
- `sb` Seek aligned to bb start
- `sC[?] string` Seek to comment matching given string
- `sf` Seek to next function (f->addr+f->size)
- `sf function` Seek to address of specified function
- `sf.` Seek to the beginning of current function
- `sg/sG` Seek begin (sg) or end (sG) of section or file

- [ `sl[?] [+-]line` Seek to line](/options/s/sl)

- `sn/sp` Seek to next/prev location, as specified by scr.nkey
- `so [N]` Seek to N next opcode(s)
- `sr pc` Seek to register
- `ss` Seek silently (without adding an entry to the seek history)

<p hidden>s- s-- s+ s++ s/ sj s/x sa sb sC sf sg sG sl sn sp so sr ss</p>