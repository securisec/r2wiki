# Pwn helper

## ROP
  - Use rarop. See [this section](https://www.notion.so/rarop-find-and-debug-ROP-gadgets-using-radare2-f1a74c9d70b24415b8f8dad7ca27137f#21138fe74fc74470adb5010e8c986e61) for help.

  [Rop'n'roll · The Official Radare Blog](undefined)

---

## Heap
  - `dmh` to see heap memory

---

## Pattern generator / Offset finder
  - `wop` . Example: `wop 100 @ eax`

---

## Pattern searches
  - Use `/p [int]` to search for repeated patterns. The int specifies the length of the pattern. Could be helpful in finding user input accross the binary.
  - Search for asm opcodes by using `/a` . Example `/a jmp esp` .

---

## Online writeups

  [Pwning exploit400 from the Nullcon 2014 CTF with radare2](undefined)

  [pwning with radare2 - crowell's blog](undefined)

  [A journey into Radare 2 - Part 2: Exploitation - Megabeets](undefined)