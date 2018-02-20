<!-- TITLE: p -->
<!-- SUBTITLE: All printing functions are handled by p and its sub options -->

#  `p` Print current block with format and length


```
Usage: p[=68abcdDfiImrstuxz] [arg|len] [@addr]
```


- [ `p-[?][jh] [mode]` bar|json|histogram blocks (mode: e?search.in)](/options/p/p-jh)

- [ `p=[?][bep] [blks] [len] [blk]` show entropy/printable chars/chars bars](/options/p/p-bep)

- `p2 [len]` 8x8 2bpp-tiles
- `p3 [file]` 🚀 print stereogram (3D) [asciinema](https://asciinema.org/a/tMwTJ5McX5vVsSwH21gBDXNTp)
- `p6[de] [len]` base64 decode/encode
- `p8[?][j] [len]` 🚀 8bit hexpair list of bytes [asciinema](https://asciinema.org/a/NiBOmL4HjzsMgYlIMiZxHAwGv)

- [ `pa[edD] [arg]` pa:assemble pa[dD]:disasm or pae: esil from hexpairs](/options/p/pa-ed)
	- > 🚀use `pa` to assemble instructions to opcodes. [asciinema](https://asciinema.org/a/pg4JyPZ4Tx1l2v2nVzKusAeVA)

- `pA[n_ops]` show n_ops address and type
- `p[b|B|xb] [len] ([skip])` bindump N bits skipping M
- `pb[?] [n]` bitstream of N bits
- `pB[?] [n]` bitstream of N bytes

- [ `pc[?][p] [len]` output C (or python) format](/options/p/pc-p)

- `pC[d] [rows]` print disassembly in columns (see hex.cols and pdi)

- [ `pd[?] [sz] [a] [b]` disassemble N opcodes (pd) or N bytes (pD)](/options/p/pd-sz)

- [ `pf[?][.nam] [fmt]` print formatted data (pf.name, pf.name $<expr>)](/options/p/pf-nam)

- [ `ph[?][=|hash] ([len])` calculate hash for a block](/options/p/ph-hash)

- [ `p[iI][df] [len]` print N ops/bytes (f=func) (see pi? and pdi)](/options/p/p-ii)
	> 🚀 Use `pi` to print opcodes only [asciinema](https://asciinema.org/a/Ygnzj7RSt7JJ3orx8DvonLpIW)

- [ `pj[?] [len]` print as indented JSON](/options/p/pj-len)

- [ `p[kK] [len]` print key in randomart (K is for mosaic)](/options/p/p-k_capk)

- [ `pm[?] [magic]` print libmagic data (see pm? and /m?)](/options/p/pm-magic)

- `pq[?][iz] [len]` print QR code with the first Nbytes of the current block

- [ `pr[?][glx] [len]` print N raw bytes (in lines or hexblocks, 'g'unzip)](/options/p/pr-glx)

- [ `ps[?][pwz] [len]` print pascal/wide/zero-terminated strings](/options/p/ps-pwz)

- [ `pt[?][dn] [len]` print different timestamps](/options/p/pt-dn)

- [ `pu[?][w] [len]` print N url encoded bytes (w=wide)](/options/p/pu-w-len)

- [ `pv[?][jh] [mode]` show variable/pointer/value in memory](/options/p/pv-jh-mode)

- `pwd` display current working directory

- [ `px[?][owq] [len]` hexdump of N bytes (o=octal, w=32bit, q=64bit)](/options/p/px-owq)

- [ `pz[?] [len]` print zoom view (see pz? for help)](/options/p/pz-len-print-zoom)

<p hidden>p2 p3 p6 p8 pA pb pB pC pd pf ph pi pj pk pK pm pq pr ps pt pu pv pwd px pz</p>