<!-- TITLE: Java -->
# Java

```
Usage: java [cmd] [arg..] Suite of java commands, java help for more info
```

- `help                            `  displays this message
- `set_flags [addr cmf <value>]    `  set the access flags attributes for a field or method
- `prototypes <jaicmf>             `  show in JSON, or All,Imports,Class,Methods,Fields
- `resolve_cp [<stecadg> idx]      `  cp type or value @ idx. Summary,Type,b64Encode,Const,Addr,Dump,Gsumarize
- `calc_flags <lcfm> [visib.]      `  value from access flags: ListAll, flags, Class, Field, Method
- `flags_str_at <cfm> [addr]       `  string value from access flags @ addr: Class, Field, Method
- `flags_str [<cfm> <access>]      `  string value for the flags number: Class, Field, Method
- `m_info [<p,c,s idx> | <n idx>]  `  method information at index (c:method+ord, s:metadata)
- `f_info [<p,c,s idx> | #idx]     `  field information at index (c:field+ord, s:metadata)
- `find_cp_const [a|#idx]          `  find references to constant CP Object in code: AllReferences
- `find_cp_value [<silfd> V]       `  find references to CP constants by value
- `replace_cp_value [<idx> V]      `  replace CP constants with value if the no resizing is required
- `replace_classname_value <c> <nc>`  rename class name
- `reload_bin addr [size]          `  reload and reanalyze the Java class file starting at address
- `summary                         `  print summary information for the current java class file
- `lcr [addr]                      `  list all references to fields and methods in code sections
- `exc [<addr>]                    `  list all exceptions to fields and methods in code sections
- `yc_w_refs [name] [start] [count]`  yara code bytes extraction with a name starting at \<start\> to \<count\>
- `i_mref C M S                    `  add Method to Class with given method signature
- `calc_sz <addr>                  `  calculate class file size at location
- `is_valid <addr> <sz>            `  check buffer to see if it is a valid class file

<p hidden>prototypes set_flags java lcr exc</p>