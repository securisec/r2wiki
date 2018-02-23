<!-- TITLE: db -->

#  `db[?]` Breakpoints commands


```
Usage: db # Breakpoints commands
```


- `db` List breakpoints
- `db sym.main` Add breakpoint into sym.main
- `db <addr>` Add breakpoint
- `db -<addr>` Remove breakpoint
- `db-` 🚀 Can be used with tab autocompletion to show and delete / remove breakpoints [asciinema](https://asciinema.org/a/FnpOhoNIXJ5d4dAAaQ9Vgg3OW)
- `db.` Show breakpoint info in current offset
- `dbj` List breakpoints in JSON format
- `dbc <addr> <cmd>` Run command when breakpoint is hit
  - > Use this to run a command everytime a breakpoint hits. Example: `db sym.imp.strcmp; dbc sym.imp.strcmp drr` . This till print out the registers everytime the debugger breaks at strcmp
  - Screenshot

    ![](/uploads/small-d/dbc.png)

- `dbC <addr> <cmd>` Run command when breakpoint is hit, but continue until condition on command returns zero
	- > `dbC` If the command returns a value different from zero, execution continue, otherwise, execution is stopped at the breakpoint
- `dbd <addr>` Disable breakpoint. Supports autocomplete
- `dbe <addr>` Enable breakpoint. Supports autocomplete
- `dbs <addr>` Toggle breakpoint. Supports autocomplete
- `dbf` Put a breakpoint into every no-return function
- `dbt[?]` Display backtrace based on dbg.btdepth and dbg.btalgo
- `dbt*` Display backtrace in flags
- `dbt=` Display backtrace in one line (see dbt=s and dbt=b for sp or bp)
- `dbtj` Display backtrace in JSON
- `dbta` Display ascii-art representation of the stack backtrace
- `dbtv` Display backtrace with local vars if any
- `dbte <addr>` Enable Breakpoint Trace
- `dbtd <addr>` Disable Breakpoint Trace
- `dbts <addr>` Swap Breakpoint Trace
- `dbm <module> <offset>` Add a breakpoint at an offset from a module's base
- `dbn [<name>]` Show or set name for current breakpoint
- `dbi` List breakpoint indexes
- `dbic <index> <cmd>` Run command at breakpoint index
	- > `dbi` and `dbic` can be used to run a command once a break point hits similar to `db` and `dbc`
- `dbie <index>` Enable breakpoint by index
- `dbid <index>` Disable breakpoint by index
- `dbis <index>` Swap Nth breakpoint
- `dbite <index>` Enable breakpoint Trace by index
- `dbitd <index>` Disable breakpoint Trace by index
- `dbits <index>` Swap Nth breakpoint trace
- `dbh x86` Set/list breakpoint plugin handlers
- `dbh- <name>` Remove breakpoint plugin handler
- `dbw <addr> <rw>` Add watchpoint
- `drx number addr len rwx` Modify hardware breakpoint
- `drx-number` Clear hardware breakpoint

<p hidden>db dbj dbc dbC dbd dbe dbs dbf dbt dbt* dbt=dbtj dbta dbtv dbte dbtd dbts dbm dbn dbi dbic dbie dbid dbis dbite dbitd dbits dbh dbh- dbw drx</p>
