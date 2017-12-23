<!-- TITLE: m -->

#  **`m`** Mountpoints commands


```text
Usage: m[-?*dgy] [...] Mountpoints management
```


- **`m`** List all mountpoints in human readable format
- **`m*`** Same as above, but in r2 commands

- [ **`ml`** List filesystem plugins](/options/m/ml)

- **`m /mnt`** Mount fs at /mnt with autodetect fs and current offset
- **`m /mnt ext2 0`** Mount ext2 fs at /mnt with delta 0 on IO
- **`m-/`** Umount given path (/)
- **`md /`** List directory contents for path

- [ **`mf[?] [o|n]`** Search files for given filename or for offset](/options/m/mf)

- **`mg /foo`** Get contents of file/dir dumped to disk (XXX?)
- **`mo /foo/bar`** Open given file into a malloc://
- **`mi /foo/bar`** Get offset and size of given file
- **`mp`** List all supported partition types
- **`mp msdos 0`** Show partitions in msdos format at offset 0
- **`ms /mnt`** Open filesystem prompt at /mnt
  > Shell prompt inside the mounted directory
- **`my`** Yank contents of file into clipboard

<p hidden>m- md mg mo mi mp ms my</p>