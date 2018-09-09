<!-- TITLE: tl -->

#  `tl[?]` Show/Link type to an address

- `tl` list all links in readable format
	- > `tl` can be used to cast the type of an address permanently
- `tl[typename]` link a type to current address.
- `tl[typename] = [address]` link type to given address.
	- `tl` can be used to link both struct and address
- `tls[address]` show link at given address
- `tl-*` delete all links.
- `tl-[address]` delete link at given address.
- `tl*` list all links in radare2 command format
- `tl?` print this help.

<p hidden>tl tls tl- tl*</p>