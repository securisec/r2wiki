<!-- TITLE: ( -->

#  `(` Macros

Usage: (foo args,cmd1,cmd2,..)Aliases

## **Tips**
  - Example: `(abc, pd 4, ao)` . In this example, `abc` is the name, and when the macro is called, it will run the `,` seperated commands. The macro can be called with `.(abc)`

---
- **`(foo args,..,..)`** define a macro
- **`(foo args,..,..)()`** define and call a macro
- **`(-foo)`** remove a macro
- **`.(foo)`** to call it
- **`()`** break inside macro
- **`(*`** list all defined macros
- **Argument support:**
  - **`(foo x y, $0 @ $1)`** define fun with args (x - $0, y - $1)
  - **`.(foo 128 0x804800)`** call it with args
- **Iterations:**
  - **`.(foo,() $@)`** define iterator returning iter index
  - **`x @@ .(foo)`** iterate over them