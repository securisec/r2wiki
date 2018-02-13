<!-- TITLE: om -->

#  `om[?]` create, list, remove IO maps


```text
Usage: om[-] [arg] # map opened files
```


- `om` list all defined IO maps
- `omq` list all maps and their fds
- `om*` list all maps in r2 commands format
- `om=` list all maps in ascii art
- `omj` list all maps in json format
- `om [fd]` list all defined IO maps for a specific fd
- `om-mapid` remove the map with corresponding id
- `om fd vaddr [size] [paddr] [rwx] [name]` create new io map
- `omm [fd]` create default map for given fd. (omm `oq` )
- `om.` show map, that is mapped to current offset
- `omn mapid [name]` set/delete name for map with mapid
- `omn.([-|name])` show/set/delete name for current map
- `omf [mapid] rwx` change flags/perms for current/given map
- `omfg[+-]rwx` change flags/perms for all maps (global)
- `omb mapid addr` relocate map with corresponding id
- `omb. addr` relocate current map
- `omr mapid newsize` resize map with corresponding id
- `omp mapid` priorize map with corresponding id
- `ompf[fd]` priorize map by fd
- `ompb binid` priorize maps of mapped bin with binid
- `omps sectionid` priorize maps of mapped section with sectionid
- `om*` show r2 commands to restore mapaddr

<p hidden>om omq om* om= omj omm om. omn omn. omf omfg omb omb. omr omp ompf ompb omps om*</p>