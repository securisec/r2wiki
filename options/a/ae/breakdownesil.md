<!-- TITLE: breakdown esil -->

# Breakdown of ESIL

## What A, R, W, N means

- `A` denotes all registers
- `R` denotes registers being read
- `W` denotes registers being written to
- `N` denotes registers not being used
- Example:

      [0x08048460]> aea
      A: esp eip edx # all registers being used
      R: esp eip edx # registers being read
      W: esp eip # registers being written to
      N: edx # registers not being used
      L0: 0xfffffffc

---

## Resources

[ESIL · Radare2 Explorations](https://monosource.gitbooks.io/radare2-explorations/content/tut3/tut3_-_esil.html)