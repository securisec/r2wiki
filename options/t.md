<!-- TITLE: t -->

#  `t` Types, noreturn, signatures, C parser and more


```
Usage: t # cparse types commands
```

- > `t` commands support autocompletion

- `t                        `  List all loaded types
    - > `t` can be used to list types
- `tj                       `  List all loaded types as json
- `t <type>                 `  Show type in 'pf' syntax
- `t*                       `  List types info in r2 commands
- `t- <name>                `  Delete types by its name
- `t-*                      `  Remove all types
- `ta <type>                `  Mark immediate as a type offset
- `tc ([cctype])            `  calling conventions listing and manipulations
- `te[?]                    `  List all loaded enums
- `td[?] <string>           `  Load types from string
- `tf                       `  List all loaded functions signatures
- `tk <sdb-query>           `  Perform sdb query
- `tl[?]                    `  Show/Link type to an address
- `tn[?] [-][addr]          `  manage noreturn function attributes and marks
- `to -                     `  Open cfg.editor to load types
- `to <path>                `  Load types from C header file
- `tos <path>               `  Load types from parsed Sdb database
- `tp  <type> [addr|varname]`  cast data at \<address\> to \<type\> and print it
    - > `tp` can be useful in printing struct data
- `tpx <type> <hexpairs>    `  Show value for type with specified byte sequence
- `ts[?]                    `  print loaded struct types
- `tu[?]                    `  print loaded union types
- `tt[?]                    `  List all loaded typedefs

<p hidden>t- ta tb tc te td tf tk tl tn to tos tp ts tu tt</p>