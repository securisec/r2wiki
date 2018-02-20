<!-- TITLE: scr -->

# scr

- `scr.atport` V@ starts a background http server and spawns an r2 -C _Default is false_
- `scr.breaklines` Break lines in Visual instead of truncating them _Default is false_
- `scr.breakword` Emulate console break (^C) when a word is printed (useful for pD)
- `scr.color` 🚀 Enable colors _Default is true_ [asciinema](https://asciinema.org/a/c3NvOKBSO5UMpyuRNaVDxvEUx)
- `scr.color.bytes` Colorize bytes that represent the opcodes of the instruction _Default is true_
- `scr.color.grep` 🚀 Enable colors when using ~grep _Default is false_ [asciinema](https://asciinema.org/a/qh30rqONvLV2WDLRmuZjwnDNm)
- `scr.color.ops` 🚀 Colorize numbers and registers in opcodes _Default is true_ [asciinema](https://asciinema.org/a/6AZ7o9CrIUhRKZos5TopluNR4)
- `scr.columns` Force console column count (width) _Default is 0_
- `scr.echo` Show rcons output in realtime to stderr and buffer _Default is false_
- `scr.feedback` Set visual feedback level (1=arrow on jump, 2=every key (useful for videos)) _Default is 1_
	- > 🚀 Set `scr.feedback` to 2 to see what button was pressed / key presses in visual mode. _does slow down the screen a bit_ [asciinema](https://asciinema.org/a/Jep3mJKIWTAWwldZ4Nwct3UAc)
- `scr.fgets` Use fgets() instead of dietline for prompt input _Default is false_
- `scr.fix.columns` Workaround for Prompt iOS SSH client _Default is 0_
- `scr.fix.rows` Workaround for Linux TTY _Default is 0_
- `scr.flush` Force flush to console in realtime (breaks scripting) _Default is false_
- `scr.fps` Show FPS in Visual _Default is false_
- `scr.highlight` Highlight that word at RCons level
	- > 🚀Use `scr.highlight` to highlight anything in the disassembly. [asciinema](https://asciinema.org/a/xFrDUHJYcdt6w53jpC1IKCmhN)
- `scr.histsave` Always save history on exit _Default is true_
- `scr.html` Disassembly uses HTML syntax _Default is false_
	- > `scr.html` Enabling this will output any command in html format. Useful when working with a web ui in radare2.
		![](/uploads/small-e/scr-html.png)
- `scr.interactive` Start in interactive mode _Default is true_
- `scr.linesleep` Flush sleeping some ms in every line _Default is 0_
- `scr.nkey` Select visual seek mode (affects n/N visual commands) _Default is flag_
- `scr.null` Show no output _Default is false_
- `scr.pager` Select pager program (when output overflows the window)
	- > 🚀 `scr.pager` can be configured to address output overflow. Example, `scr.pager = less -R` [asciinema](https://asciinema.org/a/A1JPpRTjLOhKbJeVAHtrGxy3J)
- `scr.pagesize` Flush in pages when scr.linesleep is != 0 _Default is 1_
- `scr.pipecolor` Enable colors when using pipes _Default is false_
- `scr.prompt` Show user prompt (used by r2 -q) _Default is true_
- `scr.promptfile` Show user prompt file (used by r2 -q) _Default is false_
- `scr.promptflag` Show flag name in the prompt _Default is false_
- `scr.promptsect` Show section name in the prompt _Default is false_
- `scr.rainbow` Shows rainbow colors depending of address _Default is false_
  - > 🚀 `scr.rainbow` Changes the color of the offset based on the value of the offset. Allows one to easily remember where they were or functions by color. [asciinema](https://asciinema.org/a/isswUcNtyFP4pFujVlZXMpz9Z)
    ![](/uploads/small-e/rainbow.png)

- `scr.randpal` Random color palete or just get the next one from 'eco' _Default is false_
- `scr.responsive` Auto-adjust Visual depending on screen (e.g. unset asm.bytes) _Default is false_
- `scr.rgbcolor` Use RGB colors (not available on Windows) _Default is true_
- `scr.rows` Force console row count (height) (duplicate?) _Default is 0_
- `scr.seek` Seek to the specified address on startup
	- > Use `sec.seek = main` to automatically seek to main at startup
- `scr.tee` Pipe output to file of this name
	- > 🚀 Similar to the tee command in linux `scr.tee` can be used to write all outputs from r2 to a file. [asciinema](https://asciinema.org/a/ouDj8D7Yaf8De6Zg80dfzbBqV)
- `scr.truecolor` Manage color palette (0 _Default is false_
- `scr.tts` Use tts if available by a command (see ic) _Default is false_
- `scr.utf8` 🚀 Show UTF-8 characters instead of ANSI _Default is false_ [asciinema](https://asciinema.org/a/mC6rNURBpd0cbOyivtT2qUUvY)
- `scr.utf8.curvy` Show curved UTF-8 corners (requires scr.utf8) _Default is false_
- `scr.wheel` Mouse wheel in Visual; temporaryly disable/reenable by right click/Enter) _Default is true_
- `scr.wheelnkey` Use sn/sp and scr.nkey on wheel instead of scroll _Default is false_
- `scr.wheelspeed` Mouse wheel speed _Default is 4_
- `scr.zoneflags` Show zoneflags in visual mode before the title (see fz?) _Default is true_

<p hidden>scr.atport scr.breaklines scr.breakword scr.color scr.color.bytes scr.color.ops scr.columns scr.echo scr.feedback scr.fgets scr.fix.columns scr.fix.rows scr.flush scr.fps scr.highlight scr.histsave scr.html scr.interactive scr.linesleep scr.nkey scr.null scr.pager scr.pagesize scr.pipecolor scr.prompt scr.promptfile scr.promptflag scr.promptsect scr.rainbow scr.randpal scr.responsive scr.rgbcolor scr.rows scr.seek scr.tee scr.truecolor scr.tts scr.utf8 scr.utf8.curvy scr.wheel scr.wheelnkey scr.wheelspeed scr.zoneflags</p>
