<!-- TITLE: ~ Grep -->

#  `~` Grep


```text
Usage: [command]~[modifier][word,word][endmodifier][[column]][:line]
modifier:
```


- **Tips**
  - `..` Internal less
  - `[commandj]~{}` json indentation
  - `...` HUD style navigation. really nice!
  - Multiple grep patterns can be set by seperating them with a `,` . Example: `i~canary,nx,pic`
- HUD style views / grepping

  Use [somecommand] plus `~...` for HUD style naviation and searching. Example screenshot shows HUD style grepping for mov operands

  - Screenshot

    ![Grep Hud](/uploads/grep-hud.png "Grep Hud"){.pagelogo}

- **`&`** all words must match to grep the line
- **`$[n]`** sort numerically / alphabetically the Nth column
- **`$!`** sort in inverse order
- **`+`** case insensitive grep (grep -i)
- **`^`** words must be placed at the beginning of line
- **`!`** negate grep

   _grep -v_ 

- **`?`** count number of matching lines
- **`?.`** count number chars
- **`??`** show this help message
- **`:[s]-[e]`** show lines s-e
- **`..`** internal 'less'

   _Example: _ _`pdf ~..`_ _ _ 

- **`...`** internal 'hud' (like V_)
  - Screenshot

    ![](https://static.notion-static.com/30522cb0-5953-48ea-b16e-7ef88084d0d0/Untitled)

   _This is take any commands output and overlay a HUD on top of it for string type searching. Example: _ _`pdf ~...`_ _ and then search for call_ 

- **`{}`** json indentation

   _Example: _ _`iij ~{}`_ _ for pretty printing json output. Can be combine with .. for less_ 

- **`{path}`** json grep

   _The path is a json key. If the json output is an array, then use [array position]key. If the keys are nested, then use key.secondkey etc. Example _ _`ij~{bin.pic}`_ _ _ 

- **`{}..`** less json indentation
- `**endmodifier**` ** **
  - **`$`** words must be placed at the end of line
- `**column:**` ** **
  - **`[n]`** show only column n
  - **`[n-m]`** show column n to m
  - **`[n-]`** show all columns starting from column n
  - **`[i,j,k]`** show the columns i, j and k
- `**examples:**` ** **
  - **`i~:0`** show first line of 'i' output
  - **`i~:-2`** show first three lines of 'i' output
  - **`pd~mov`** disasm and grep for mov
  - **`pi~[0]`** show only opcode
  - **`i~0x400$`** show lines ending with 0x400