<!-- TITLE: ! -->

#  **`!`** Run given command as in system(3)


```text
Usage: !<cmd> Run given command as in system(3)
```

- **`!`** list all historic commands
- **`!ls`** execute 'ls' in shell
- **`!!`** save command history to hist file
- **`!!ls~txt`** print output of 'ls' and grep for 'txt'
- **`.!rabin2 -rpsei ${FILE}`** run each output line as a r2 cmd
- **`!echo $SIZE`** display file size
- **`!-`** clear history in current session
- **`!-*`** clear and save empty history log
- **`!=!`** enable remotecmd mode
- **`=!=`** disable remotecmd mode

[Environment:](./Environment-f9f4c878-c13e-4eca-8490-303264a0d721.md)