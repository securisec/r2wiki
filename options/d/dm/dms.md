<!-- TITLE: dms -->

#  `dms[?] <id> <mapaddr>` Take memory snapshot


```
Usage: dms # Memory map snapshots
```


- `dms` List memory snapshots
- `dmsj` List snapshots in JSON
- `dms*` List snapshots in r2 commands
- `dms addr` Take snapshot with given id of map at address
- `dms-id` Delete memory snapshot
- `dmsA id` Apply memory snapshot
- `dmsC id comment` Add comment for given snapshot
- `dmsd id` Hexdiff given snapshot. See `ccc` .
- `dmsw` Snapshot of the writable maps
- `dmsa` Full snapshot of all `dm` maps
- `dmsf [file] @ addr` Read snapshot from disk
- `dmst [file] @ addr` Dump snapshot to disk

<p hidden>dms dmsj dms* dms- dmsA dmsC dmsd dmsw dmsa dmsf dmst</p>