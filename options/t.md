<!-- TITLE: t -->

#  `t` Types, noreturn, signatures, C parser and more


```
Usage: t # cparse types commands
```


- `t` List all loaded types
	- > `t` can be used to list types
- `t <type>` Show type in 'pf' syntax
- `t*` List types info in r2 commands
- `t- <name>` Delete types by its name
- `t-*` Remove all types

- [ `ta <type>` Mark immediate as a type offset](/options/t/ta-type)

- `tb <enum> <value>` Show matching enum bitfield for given number

- [ `tc ([cctype])` calling conventions listing and manipulations](/options/t/tc-cctype)

- [ `te[?]` List all loaded enums](/options/t/te-list)
- `td[?] <string>` Load types from string
- `te <enum> <value>` Show name for given enum number
- `tf` List all loaded functions signatures
- `tj` Return as json
- `tk <sdb-query>` Perform sdb query

- [ `tl[?]` Show/Link type to an address](/options/t/tl-show)

- [ `tn[?] [-][addr]` manage noreturn function attributes and marks](/options/t/tn-addr)

- `to -` Open cfg.editor to load types
- `to <path>` Load types from C header file
- `tos <path>` Load types from parsed Sdb database
- `tp <type> = <address>` cast data at \<address\> to \<type\> and print it
	- > `tp` can be useful in printing struct data

- [ `ts[?]` print loaded struct types](/options/t/ts-print)
- `tt           `  List all loaded typedefs
- `tt <typename>`  Show name for given type alias
- `tt?          `  show this help

- `tu[?]` print loaded union types

<p hidden>t- ta tb tc te td tf tk tl tn to tos tp ts tu tt</p>