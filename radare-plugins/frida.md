<!-- TITLE: r2frida -->
# r2frida
> [nowsecure/r2frida](https://github.com/nowsecure/r2frida) {.is-info}

## Tips
> Use the following syntax to trace. Example: `\dtf write iZi` (this was tested against node. Write is the symbol being hooked)

## Frida commands
[Frida Commands](/plugins/Frida-Commands)

## Videos
[r2con2017 - r2frida /by @mrmacete](https://www.youtube.com/watch?list=PLjIhlLNy_Y9Oe-nfcPEpaki0_En5dhQ5S&time_continue=15&v=URyd4bcV-Ik){.youtube}

## Load a binary
### Attach to a running process
#### On the host
- r2 frida://Twitter
- r2 frida://\<pid\>

#### On the device
- r2 frida://\<device_id\>Twitter
- r2 frida://\<device_id\>\<pid\>

### Spawn a process
#### On the host
- r2 frida:///bin/ls
- r2 "frida:///bin/ls -la" _supply arguments_

#### On a device
- r2 frida://\<device_id\>//your.package.name