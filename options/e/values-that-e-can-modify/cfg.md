<!-- TITLE: cfg -->

# cfg

- `cfg.bigendian` Use little (false) or big (true) endianness _Default is false_
- `cfg.debug` Debugger mode _Default is false_
- `cfg.editor` Select default editor program _Default is vi_
  - > _Change this to your favorite editor using `e cfg.editor=editor` . Editor could be nano, subl (sublime command line) etc_
- `cfg.fortunes` If enabled show tips at start _Default is true_
- `cfg.fortunes.clippy` Use ?E instead of ?e _Default is false_

  - Custom clippy message

   - > _Can have some fun with this by setting this on ~/.radare2rc. Example: `?E your_message_here`_ 

      
```text
┌─[~][]
      └─▪ radare2 -
       .--. .-----------.
       | _| | |
       | O O < securisec |
       | | | | |
       || | / `-----------'
       |`-'|
       `---'
       -- Change the registers of the child process in this way: 'dr eax=0x333'
      [0x00000000]>
```


- `cfg.fortunes.tts` Speak out the fortune _Default is false_
- `cfg.fortunes.type` Type of fortunes to show (tips, fun, nsfw, creepy) _Default is tips,fun_
- `cfg.hashlimit` If the file is bigger than hashlimit, do not compute hashes _Default is 0x00a00000_
- `cfg.log` Log changes using the T api needed for realtime syncing _Default is false_
- `cfg.newtab` Show descriptions in command completion _Default is false_
	> `cfg.newtab` Tab autocomplete commands.
- `cfg.plugins` Load plugins at startup _Default is true_
- `cfg.prefixdump` Filename prefix for automated dumps _Default is dump_
- `cfg.sandbox` Sandbox mode disables systems and open on upper directories _Default is false_
- `cfg.user` Set current username/pid _Default is pid2978_
- `cfg.wseek` Seek after write _Default is false_


<p hidden>cfg.bigendian cfg.debug cfg.editor cfg.fortunes cfg.fortunes.clippy cfg.fortunes.tts cfg.fortunes.type <p hidden>cfg.hashlimit cfg.log cfg.newtab cfg.plugins cfg.prefixdump cfg.sandbox cfg.user cfg.wseek complete autocomplete</p>