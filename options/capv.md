<!-- V -->

#  **`V`** Visual mode

> **(V! = panels, VV = fcngraph, VVV = callgraph)**  {.is-info}

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

[Visual mode help](./Visual-mode-help-644118cc-baed-4188-bae7-c56ef3d64288.md)

- Panels `V!`

  ![](https://static.notion-static.com/c0c6a460c0c34bd1a4e08ff201894559/panels.png)

- Hex view `V`

   [ `V` Help](https://www.notion.so/722c6fa4-64ac-452a-aa17-6c1719836dff) 

  - After loading hex view, use `p` to see this view

    ![](https://static.notion-static.com/30c641b0eae8477980783f73bba72830/Untitled)

  - Pressing `p` twice in this mode will show the stack and the registers in the same view. This is very helpful during debugging.
  - In this mode, you can navigate and scroll through the stack/registers/assembly by using `c` (cursor) and **TAB**

    ![](https://static.notion-static.com/a5dcd953bf7e4909a50c3077970ca4d8/Untitled)

- `vv`

  ![](https://static.notion-static.com/b6dcbb25c7c5479792e0adc2f0c70be5/vv.png)

- Callgraph `VVV` or `VV` (Can use `-` or `+` to zoom)

   [ `VV` Help](https://www.notion.so/ded91547-3ff7-4553-a37d-03bdf4bd63ad) 

  ![](https://static.notion-static.com/430653c848444fa9a63bd38e88dc7b2b/VVV.png)