<!-- V -->

#  **`V`** Visual mode

> **(V! = panels, VV = fcngraph, VVV = callgraph)** 

> [Visual mode help](/options/capv/visual-mode) 


## **Tips**
  > You can use `h, j, k, l` or `H, G, K, L` to move inside the visual mode, or `TAB` to navigate

  > Use `c` to toggle cursor mode.

  > Use `p` to show different views inside visual mode. The different modes are normal, display offsets, minigraph and summary

  > Use `/` to highlight searches in visual mode

  > In hex view, press `p` to show disassembly. Pressing `c` will enable cursor mode. Use the cursor mode to set breakpoints using `F2` . Can use `B` also to set breakpoints

  > Use `$` to toggle psuedo code inside visual mode

  > In visual mode, pressing the number inside square brackets i.e `[1]` will move seek to that address. This generally applies to calls or jumps. Anything inside square brackets are used for quick navigation, i.e. `[ga]` means press ga to seek to that addressess (in `VV` mode)

  > Seek backwards using `u`

  > Use `.` in visual mode to jump back to where the seek (cursor) is.

  > Use `??` in visual mode to get a HUD style panel (easier for beginners)


## Panels `V!`

  <img src="../../../../../../uploads/cap-v/panels.png" width="50%">

## Hex view `V`

  - [ `V` Help](/options/capv/visual-mode) 

  - After loading hex view, use `p` to see this view

    <img src="../../../../../../uploads/cap-v/hex-view.png" width="50%">

  - Pressing `p` twice in this mode will show the stack and the registers in the same view. This is very helpful during debugging.
  - In this mode, you can navigate and scroll through the stack/registers/assembly by using `c` (cursor) and **TAB**

    <img src="../../../../../../uploads/cap-v/hex-view-cap-p" width="50%>

## `vv`

  <img src="../../../../../../uploads/cap-v/vv.png " width="50%">

- Callgraph `VVV` or `VV` (Can use `-` or `+` to zoom)

   [ `VV` Help](/options/capv/visual-mode) 

  <img src="../../../../../../uploads/cap-v/cap-vvv-png.png " width="50%">
