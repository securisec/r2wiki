<!-- TITLE: wt -->

#  `wt[f][?] file [sz]` write to file (from current seek, blocksize or sz bytes)


```text
Usage: wt[a] file [size] Write 'size' bytes in current block to 'file'
```


- `wta [filename]` append to 'filename'
- `wtf [filename] [size]` write  to file (see also 'wxf' and 'wf?')
	- Use `wtf @@ hit*` to write to disk all files that `/m` found. Sort of similar to binwalk
- `wtf! [filename]` write to file from current address to eof

<p hidden>wta wtf</p>