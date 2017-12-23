<!-- TITLE: v Help -->

#  `V` Help

## **Tips**
  > Use `- or +` while in cursor mode to increment of decrement opcode value

---

- ` ` Press `space bar` to switch between V and VV modes
- **`?`** show this help
- **`??`** show the user-friendly hud
  - Screenshot

    ![Question Question Hud](/uploads/v-help/question-question-hud.png "Question Question Hud")

  - _Makes it really easy to do various tasks in visual mode. This is different from the _ _`_`_ _ HUD mode_
- **`$`** toggle asm.pseudo
- **`%`** in cursor mode finds matching pair, otherwise toggle autoblocksz
- **`@`** redraw screen every 1s (multi-user view), in cursor set position
- **`!`** enter into the visual panels mode
- **`_`** enter the flag/comment/functions/.. hud (same as VF_)
  - Screenshot

    ![](https://static.notion-static.com/76b45d95-4b6d-4c29-9aa3-d4274a2ad787/Untitled)

- **`=`** set cmd.vprompt (top row)
- **`|`** set cmd.cprompt (right column)
- **`.`** seek to program counter
  - _Return back to where EIP or the current seek is_
- **`\`** toggle visual split mode
- **`"`** toggle the column mode (uses pC..)
- **`/`** in cursor mode search in current block
- **`:cmd`** run radare command
- **`;[-]cmt`** add/remove comment
- **`0`** seek to beginning of current function
- **`[1-9]`** follow jmp/call identified by shortcut (like ;[1])
- **`,file`** add a link to the text file
- **`/*+-[]`** change block size, [] = resize hex.cols
- **`</>`** seek aligned to block size (seek cursor in cursor mode)
- **`a`** assemble code
- `A` visual Assembler
- **`b`** browse symbols, flags, configurations, classes, ...
- **`B`** toggle breakpoint
- **`c/C`** toggle (c)ursor and (C)olors
  - _Use - or + to increment or decrement opcode value while in cursor c mode_

[ **`d[f?]`** define function, data, code, ..](./d-f-define-function-data-code-2246d84e-0170-46e0-82b4-6f401a8374b2.md)

- **`e`** edit eval configuration variables
- `E` Color / Theme changer. Use up or down to select what you want to change followed by RGB keys.
  - _Use _ _`rRgGbB`_ _ keys to the RGB values_
- **`f/F`** set/unset or browse flags. f- to unset, F to browse, ..
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

- **`gG`** go seek to begin and end of file (0-$s)
- **`hjkl`** move around (or HJKL) (left-down-up-right)
- **`i`** insert hex or string (in hexdump) use tab to toggle
- **`mK/'K`** mark/go to Key (any key)
- **`M`** walk the mounted filesystems
- **`n/N`** seek next/prev function/flag/hit (scr.nkey)
  - _Move down _ _`n`_ _ or up _ _`N`_ _ to the next function_
- **`o`** go/seek to given offset
  - _Go to this offset and change seek to this offset._
- **`O`** toggle asm.esil
- **`p/P`** rotate print modes (hex, disasm, debug, words, buf)
- **`q`** back to radare shell
- **`r`** refresh screen / in cursor mode browse comments
- **`R`** randomize color palette (ecr)
- **`sS`** step / step over
- **`t`** browse types
- **`T`** enter textlog chat console (TT)
- **`uU`** undo/redo seek
- **`v`** visual function/vars code analysis menu
- **`V`** (V)iew graph using cmd.graph (agv?)
- **`wW`** seek cursor to next/prev word
- **`xX`** show xrefs/refs of current function from/to data/code
  - Screenshot

    ![](https://static.notion-static.com/f3cc0ee1-a8d6-47f5-b88e-50d7038de495/Untitled)

- **`yY`** copy and paste selection
- **`z`** fold/unfold comments in disassembly
- **`Z`** toggle zoom mode
- **`Enter`** follow address of jump/call
- **`F2`** toggle breakpoint
- **`F4`** run to cursor
- **`F7`** single step
- **`F8`** step over
- **`F9`** continue