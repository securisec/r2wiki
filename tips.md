# Tips

## **Unorganized random tips**

- Use `~/.radare2rc` to make any config or cmd run everytime radare2 is loaded.
- To run the same command multiple times, prepend the number before the command. Example: `3dc` will run `dc` three times
- To run radare2 without a binary, use a `-` as the argument instead of a filepath
- You can get any output in `less` format by using `[command] ~..`
- To find crypto keys, use `/Ca` (AES), or `/Cr` (RSA) keys
- Set `e asm.emu =1` to emulate cpu instructions.
- Use `~{}` after any json output to make pretty print. Ex: `pdfj~{}`
- Use `drr` to see what values registers are pointing to. This is similar to the register view in gdb peda.
- Use `pxr` for stack analysis (helpful for pwn challenges)
- Use `~...` for a HUD style navigator. Really handly searching inside functions. Example, search for calls
- Use `afn` to rename functions. In visual mode, use `dr` instead
- In visual mode, pressing the number inside square brackets i.e `[1]` will move seek to that address. This generally applies to calls or jumps
- Set `e asm.describe = true` to have inline description of that each line does. This can be set in the default radare2 config file located at `~/.radare2rc`
- Search hexadecimal of a string by prepending the string with a `\x` . For example, `/ \xELF`
- To find AES or RSA keys in memory, load radare as `sudo radare2 /dev/mem` and then search with `/Ca` or `/Cr`
- Use `drr` for register references like peda
- Use `=H` inside radare2 shell to start and launch r2 webserver.
- Set environment variables as `setenv=foo=bar` in the .rr file and load it along with the binary
- Equivalent of "set-follow-fork-mode" gdb command. First, `dcf` until a fork happens, and then `dp` to see all child processes
- When debugging a binary, use `e dbg.bep=main` or entry to bypass the loader. This can be made persistant in `~/.radare2rc`
- Use the back tick ``` to wrap a command to use as the input to another command. Example 
	```text
	s axt `str.some~[1]`
	```
 . This command will take the address xref to of somestr and seek to that address.
- The `$$` represents here (current seek)
- Press **space bar** to switch between `V` and `VV`
- Use `agv` to open a grapviz flow graph
- Set `?E `fo`` in `~/.radare2rc` to show clippy style fortune messages
- [Floss](https://github.com/fireeye/flare-floss/releases) has a radare2 output using `-r`
- When commenting out a line in `~/.radare2rc` , dont do `#foo` . Use `# foo` . That space is important