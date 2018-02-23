<!-- TITLE: ( -->

#  `(` Macros
```sh
Usage: (foo args,cmd1,cmd2,..)Aliases
```
## Tips
  - > Example: `(abc, pd 4, ao)` . In this example, `abc` is the name, and when the macro is called, it will run the `,` seperated commands. The macro can be called with `.(abc)`

  - > More macro usage examples can be found [here](/home/misc/usage-examples#macros)

 - > ⭐ [Macro chapter from r2 book](https://radare.gitbooks.io/radare2book/content/scripting/macros.html)

- `(foo args,..,..)` define a macro
	- > Example for loop in macro `(loop_macro,f cnt=3,loop:,?e hello `?vi cnt`,f cnt=`?vi cnt-1`,?= cnt,?!(),.loop:)`
- `(foo args,..,..)()` define and call a macro
- `(-foo)` remove a macro
- `.(foo)` to call it
- `()` break inside macro
- `(*` list all defined macros
- Argument support:
  - `(foo x y, $0 @ $1)` define fun with args (x - $0, y - $1)
  - `.(foo 128 0x804800)` call it with args
- Iterations:
  - `.(foo,() $@)` define iterator returning iter index
  - `x @@ .(foo)` iterate over them

## Examples
`(changeStackView , e cmd.stack = pxr 40@r:SP, e dbg.slow=false)` This will change how the stack looks in visual debug mode. [@NistelbergerK](https://twitter.com/NistelbergerK)