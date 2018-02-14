<!-- TITLE: e -->

#  `e` List/get/set config evaluable vars


```
Usage: e [var[=value]]Evaluable vars
```


- > 🚀 [Values that `e` can modify](/options/e/Values-that-e-can-modify) [asciinema](https://asciinema.org/a/AEden7PwhG0w3gcgvhB5qnEg7) 

- > Use `Ve` to enter Visual mode to modify `e` values, or use `e??[key name]` to get a description. To get valid values, use `=?`. Example `e dbg.bep =?`

- `e?asm.bytes` show description
- `e??` list config vars with description
- `e a` get value of var 'a'
- `e a=b` set var 'a' the 'b' value
- `e var=?` print all valid values of var
- `e var=??` print all valid values of var with description
- `e-` reset config vars
- `e*` dump config vars in r commands
- `e!a` invert the boolean value of 'a' var

- [ `ec [k] [color]` set color for given key (prompt, offset, ...)](/options/e/ec)

- `eevar` open editor to change the value of var
- `ej` list config vars in JSON
- `env [k[=v]]` get/set environment variable
- `er [key]` set config key as readonly. no way back
- `es [space]` list all eval spaces [or keys]
- `et [key]` show type of given config variable
- `ev [key]` list config vars in verbose format
- `evj [key]` list config vars in verbose format in JSON

<p hidden>e!a eevar ej env er es et ev evj</p>
