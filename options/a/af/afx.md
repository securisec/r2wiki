<!-- TITLE: afx -->

#  `afx[cCd-] src dst`   add/remove code/Call/data/string reference


```
Usage: afx[-cCd?] [src] [dst] manage function references (see also ar?)
```


- `afxc sym.main+0x38 sym.printf`   add code ref
- `afxC sym.main sym.puts`   add call ref
- `afxd sym.main str.helloworld`   add data ref
- `afx- sym.main str.helloworld`   remove reference

<p hidden>afxc afxC afxd afx afx-</p>