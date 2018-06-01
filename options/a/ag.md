<!-- TITLE: ag -->

#  `ag[?] [options]`   output Graphviz code

## Tips
- > Dependencies include `xdot` . To install, `sudo apt install xdot`
- > To print a grapviz, `use a[options] | xdot -` . Example: `ag $$ | xdot -` . `$$` means here (at current seek). `agv` does the same thing.
- > `ag` supports autocompletion
	
---

- [ `agg`   display current graph created with agn and age (see also ag-)](/options/a/ag/agg-display)
- `agf [addr]`   Show ASCII art graph of given function
	- > After setting `scr.html` to true, `agf` can be used to export a visual graph to html.
- `agfl`
- [ `agg[?] [kdi*]`   Print graph in ASCII-Art, graphviz, k=v, r2 or visual](/options/a/ag/agg-kdi)

- Graph commands:
- `agc[format] [fcn addr]`  Function callgraph
- `agf[format] [fcn addr]`  Basic blocks function graph
- `agx[format] [addr] `     Cross references graph
- `agr[format] [fcn addr]`  References graph
- `aga[format] [fcn addr]`  Data references graph
- `agd[format] [fcn addr]`  Diff graph
- `agi[format]`             Imports graph
- `agC[format]`             Global callgraph
- `agR[format]`             Global references graph
- `agA[format]`             Global data references graph
- `agg[format]`             Custom graph
- `ag-`                     Clear the custom graph
- `agn[?] title body`       Add a node to the custom graph
- `age[?] title1 title2`    Add an edge to the custom graph

```
- Output formats:
- <blank>                 Ascii art
- v                       Interactive ascii art
- t                       Tiny ascii art
- d                       Graphviz dot
- j                       json ('J' for formatted disassembly)
- g                       Graph Modelling Language (gml)
- k                       SDB key-value
- *                       r2 commands
- w                       Web/image (see graph.extension and graph.web)
```
<p hidden>ag ag- aga agr agc agC agd age agf agg agj agk agl agn ags agt agv xdot agc agf agx agr aga agd agi agC agR agA agg ag- agn age</p>
