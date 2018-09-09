<!-- TITLE: v Help -->

#  `V` Help

## Tips
  - > Use `- or +` while in cursor mode to increment of decrement opcode value

---

- ` ` Press `space bar` to switch between V and VV modes
- `?` show this help
- `??` show the user-friendly hud
  - Screenshot

    ![](/uploads/v-help/question-question-hud.png) 

  - > _Makes it really easy to do various tasks in visual mode. This is different from the `_` HUD mode_
- `$` toggle asm.pseudo
- `(` snow in visual mode
- `%` in cursor mode finds matching pair, otherwise toggle autoblocksz
- `@` redraw screen every 1s (multi-user view), in cursor set position
- `!` enter into the visual panels mode
- `_` enter the flag/comment/functions/.. hud (same as VF_)
  - Screenshot

    ![](/uploads/v-help/underscore-hud.png) 

- `=` set cmd.vprompt (top row)
- `|` set cmd.cprompt (right column)
- `.` seek to program counter
  - > _Return back to where EIP or the current seek is_
- `\` toggle visual split mode
- `"` toggle the column mode (uses pC..)
- `/` in cursor mode search in current block
- `:cmd` run radare command
- `;[-]cmt` add/remove comment
- `0` seek to beginning of current function
- `[1-9]` follow jmp/call identified by shortcut (like ;[1])
- `,file` add a link to the text file
- `/*+-[]` change block size, [] = resize hex.cols
- `</>` seek aligned to block size (seek cursor in cursor mode)
- `a` assemble code
- `A` visual Assembler
	- Use `VA` to assemble from asm to hex and so forth
- `b` browse symbols, flags, configurations, classes, ...
	```
	_  hud mode (V_)
	b  blocks
	c  classes
	C  comments
	e  eval var configurations
	f  flags
	F  functions
	h  history
	i  imports
	m  maps
	p  pids/threads
	q  quit
	s  symbols
	t  types
	v  vars
	x  xrefs
	X  refs
	```

- `B` toggle breakpoint
- `c/C` toggle (c)ursor and (C)olors
  - > _Use - or + to increment or decrement opcode value while in cursor c mode_
  - > Can also use `[` or `]` to adjust the comment columns

- [ `d[f?]` define function, data, code, ..](/options/capv/visual-mode/v-help/d)

- `e` edit eval configuration variables
- `E` Color / Theme changer. Use up or down to select what you want to change followed by RGB keys.
  - > `VE` _Theme editor: Use `rRgGbB` keys to the RGB values_
- `f/F` set/unset or browse flags. f- to unset, F to browse, ..
  - Visual flag help

         q - quit menu
         j/k - line down/up keys
         J/K - page down/up keys
         h/b - go back
         C - toggle colors
         l/' ' - accept current selection
         a/d/e - add/delete/edit flag
         +/- - increase/decrease block size
         o - sort flags by offset
         r/R - rename flag / Rename function
         n - sort flags by name
         p/P - rotate print format
         _ - hud for flags and comments
         : - enter command

- `gG` go seek to begin and end of file (0-$s)
- `hjkl` move around (or HJKL) (left-down-up-right)
- `i` insert hex or string (in hexdump) use tab to toggle
- `mK/'K` mark/go to Key (any key)
- `M` walk the mounted filesystems
- `n/N` seek next/prev function/flag/hit (scr.nkey)
  - > _Move down `n` or up `N` to the next function_
- `o` go/seek to given offset
  - > _Go to this offset and change seek to this offset._
- `O` toggle asm.esil
- `p/P` rotate print modes (hex, disasm, debug, words, buf)
- `q` back to radare shell
- `r` refresh screen / in cursor mode browse comments. Toggle between hotkey hints in disasm between data and code
- `R` randomize color palette (ecr)
- `sS` step / step over
- `t` browse types
- `T` enter textlog chat console (TT)
- `uU` undo/redo seek
- `v` visual function/vars code analysis menu
- `V` (V)iew graph using cmd.graph (agv?)
- `VP` `pxr` in visual mode
- `wW` seek cursor to next/prev word
- `xX` show xrefs/refs of current function from/to data/code
  - Screenshot

    ![](/uploads/cap-v/x-xref.png) 

- `yY` copy and paste selection
- `z` fold/unfold comments in disassembly
- `Z` toggle zoom mode
- `Enter` follow address of jump/call
- `F2` toggle breakpoint
- `F4` run to cursor
- `F7` single step
- `F8` step over
- `F9` continue

## Custom visual mode
- Pressing the `=` sign inside visual mode brings up cmd.vprompt. Any command executed in this prompt shows up at the top of the visual mode.
- Pressing the `|` sign inside visual mode brings up cmd.cprompt. Any command executed in this prompt shows up at the right of the visual mode.
	![](/uploads/v-help/custom-visual-mode.png) 
	- > The red boxing is showing the command `pxr @$$!50` while the green box is show the output of `dr`
