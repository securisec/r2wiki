<!-- TITLE: $ Alias -->
#  `$` Alias


```
Usage: $alias[=cmd] [args...]Alias commands
```

- `$` list all defined aliases
- `$*` same as above, but using r2 commands
	- > Use `$*` to see values of all user defined variables or aliases. 
- `$dis='af;pdf'` create command - analyze to show function <p hidden>$dis</p>
- `$test=#!pipe node /tmp/test.js create command - rlangpipe script`
- `$dis=` undefine alias
- `$dis` execute the previously defined alias
- `$dis?` show commands aliased by 'analyze'
	- > Example `$somevar?` will show the value assigned to somevar variable