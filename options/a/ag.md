<!-- TITLE: ag -->

#  `ag[?] [options]`   output Graphviz code

## Tips
  - Dependencies include `xdot` . To install, `sudo apt install xdot`

---

> To print a grapviz, `use a[options] | xdot -` . Example: `ag $$ | xdot -` . `$$` means here (at current seek). `agv` does the same thing.

- `ag [addr]`   output graphviz code (bb at addr and children)
- `ag-`   Reset the current ASCII art graph (see agn, age, agg?)
- `aga [addr]`   idem, but only addresses
- `agr[j] [addr]`   output graphviz call graph of function

- [ `agg`   display current graph created with agn and age (see also ag-)](/options/a/ag/agg-display)

- `agc[j] [addr]`   output graphviz call graph of function
- `agC[j]`   Same as agc -1. full program callgraph
- `agd [fcn name]`   output graphviz code of diffed function

- [ `age[?] title1 title2`   Add an edge to the current graph](/options/a/ag/age-title1-title2-Add-an-edge-to-the-current-graph-39b047b9-ee67-4f5f-8826-a1cfc9d598e3.md)

- `agf [addr]`   Show ASCII art graph of given function

- [ `agg[?] [kdi*]`   Print graph in ASCII-Art, graphviz, k=v, r2 or visual](/options/a/ag/agg-kdi-Print-graph-in-ASCII-Art-graphviz-k-v-r2-or-visual-23687b92-b3e5-425a-88fb-837418803c81.md)

- `agj [addr]`   idem, but in JSON format
- `agk [addr]`   idem, but in SDB key-value format
- `agl [fcn name]`   output graphviz code using meta-data

- [ `agn[?] title body`   Add a node to the current graph](/options/a/ag/agn-title-body-Add-a-node-to-the-current-graph-3b53b044-148d-43d7-98d1-c4eeee1d4a13.md)

- `ags [addr]`   output simple graphviz call graph of function (only bb offset)
- `agt [addr]`   find paths from current offset to given address
- `agv`   Show function graph in web/png (see graph.web and cmd.graph) or agf for asciiart