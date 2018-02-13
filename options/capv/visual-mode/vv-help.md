<!-- TITLE: VV Help -->

#  `VV` Help

- ` ` Press `space bar` to switch between V and VV modes
- `:e cmd.gprompt = agft` show tinygraph in one side
- `+/-/0` 	zoom in/out/default
- `;` 	add comment in current basic block
- `.` 	center graph to the current node
- `:cmd` 	run radare command
- `'` 	toggle graph.comments
- `=` 🚀 toggle graph.layout. Enable horizontal view [asciinema](https://asciinema.org/a/6Mvr8akO7Lm4rrvJTEv71ecAT)
- `\"` 	toggle graph.refs
- `/` 	highlight text
- `|` 	set cmd.gprompt
- `_` 	enter hud selector
- `>` 	show function callgraph (see graph.refs)
	> 🚀 Use `>` to see a the call graph [asciinema](https://asciinema.org/a/HUd6rADhomkLMDm1ZMqbOcUbv)
- `<` 	show program callgraph (see graph.refs)
- `Home/End` 	go to the top/bottom of the canvas
- `Page-UP/DOWN` 	scroll canvas up/down
- `C` 	toggle scr.colors
- `d` 	rename function
- `F` 	enter flag selector

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

- `g([A-Za-z]*)` 	follow jmp/call identified by shortcut (like ;[ga])
- `G` 	debug trace callgraph (generated with dtc)
- `hjkl` 	scroll canvas
- `HJKL` 	move node
- `m/M` 	change mouse modes
- `n/N` 	next/previous scr.nkey (function/flag..)
- `o` 	go/seek to given offset
- `p/P` 	rotate graph modes (normal, display offsets, minigraph, summary)
- `q` 	back to Visual mode
- `r` 	refresh graph
- `R` 	randomize colors
- `s/S` 	step / step over
- `tab` 	select next node
- `TAB` 	select previous node
- `t/f` 	follow true/false edges
- `u/U` 	undo/redo seek
- `V` 	toggle basicblock / call graphs
- `w` 	toggle between movements speed 1 and graph.scroll
- `x/X` 	jump to xref/ref
- `y` 	toggle node folding/minification
  > _Fold a block in visual graph mode_
- `Y` 🚀 toggle tiny graph minigraph [asciinema](https://asciinema.org/a/gwGABUr8DMXCZiV3Qzta18DVp)
- `Z` 	follow parent node