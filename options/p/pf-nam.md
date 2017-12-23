<!-- TITLE: pf -->

#  **`pf[?][.nam] [fmt]`** print formatted data (pf.name, pf.name $\<expr\>)

## **Tips**
- Tips
  - > To print stacked data types, you can use `pf` . For example, use `pf xxS @ esp` (this will print hex value 64 bit pointer at offset esp)
  - > It is possible to define arrays of structures with `pf` . To do this, prefix the format string with a numeric value. You can also define a name for each field of the structure by appending them as space seperated arguments list. Example `pf 2*xs pointer type @ esp` (radare2 book page 58)
  - > Use `pfi @ offset` to print offset as signed int

---
- **`pf?`** Show this help

- [ **`pf??`** Format characters](/options/p/pf-nam/pf-Format-characters)

- [ **`pf???`** pf usage examples](/options/p/pf-nam/pf-pf-usage)

- **`pf fmt`** Show data using the given format-string. See 'pf??' and 'pf???'.
- **`pf.fmt_name`** Show data using named format
- **`pf.fmt_name.field_name`** Show specific data field using named format
- **`pfj fmt_name|fmt`** Show data using (named) format in JSON
- **`pf* fmt_name|fmt`** Show data using (named) format as r2 flag create commands
- **`pfd.fmt_name`** Show data using named format as graphviz commands
- **`pf.name [0|cnt]fmt`** Define a new named format
  > _Example is `pf.somename i`. The i is for sign integers but can be any combination of format specifiers. This can then be invoked as `pf.somename @ offset`_
- **`pf.`** List all format definitions
- **`pf?fmt_name`** Show the definition of a named format
- **`pfo`** List all format definition files (fdf)
- **`pfo fdf_name`** Load a Format Definition File (fdf)
- **`pf.fmt_name.field_name=33`** Set new value for the specified field in named format
- **`pfv.fmt_name[.field]`** Print value(s) only for named format. Useful for one-liners
- **`pfs fmt_name|fmt`** Print the size of (named) format in bytes