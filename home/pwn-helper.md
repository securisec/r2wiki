<!-- TITLE: Pwn helper -->
# Pwn helper

## ROP
  > The r2pm install seems to be broken. Use this method instead {.is-danger}

- Clone the rarop repository 
	[rarop github](https://github.com/jpenalbae/rarop)
- `npm install`
- Make a sym link `ln -s /path/to/rarop/bin/rarop /usr/local/bin/rarop` 
- Run with `rarop /path/to/binary`

  [Rop'n'roll · The Official Radare Blog](http://radare.today/posts/ropnroll/)

---

## Heap
  - `dmh` to see heap memory

---

## Pattern generator / Offset finder
  - `wop` . Example: `wop 100 @ eax`
  - To find the length of a pattern before overwrite (white overwritten using a debruijin pattern, use `wopO eip`
  - Genereate raw debruijin patterns using `ragg2 -P [length] -r`

---

## Pattern searches
  - Use `/p [int]` to search for repeated patterns. The int specifies the length of the pattern. Could be helpful in finding user input accross the binary.
  - Search for asm opcodes by using `/a` . Example `/a jmp esp` .

---

## Online writeups

  [Pwning exploit400 from the Nullcon 2014 CTF with radare2](https://dustri.org/b/pwning-exploit400-from-the-nullcon-2014-ctf-with-radare2.html)

  [pwning with radare2 - crowell's blog](http://crowell.github.io/blog/2014/11/23/pwning-with-radare2/)

  [A journey into Radare 2 - Part 2: Exploitation - Megabeets](https://www.megabeets.net/a-journey-into-radare-2-part-2/)