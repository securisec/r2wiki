<!-- TITLE: autocomplete -->

# `!!!` User defined autocomplete

```
Usage: !!![-*][cmd] [arg|$type...] # user-defined autocompletion for commands
```

- `!!!         `  list all autocompletions
- `!!!:` Register new autocomplete logic
- `!!!?        `  show this help
- `!!!-*       `  remove all user-defined autocompletions
- `!!!-\*      `  remove autocompletions starting by backslash (glob expression)
- `!!!-foo     `  remove autocompletion named 'foo'
- `!!!foo      `  add 'foo' for autocompletion
- `!!!bar $flag`  add 'bar' for autocompletion with $flag as argument

```
|Types:
| $dflt     default autocomplete flag
| $flag     shows known flag hints
| $flsp     shows known flag-spaces hints
| $zign     shows known zignatures hints
| $eval     shows known evals hints
| $prjt     shows known projects hints
| $brkp     shows known breakpoints hints
| $file     hints file paths
| $thme     shows known themes hints
| $optn     allows the selection for multiple options
```