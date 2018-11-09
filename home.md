<!-- TITLE: r2wiki --> 
# Radare2 wiki
> This is an ongoing work in progress and reflects various material obtained while stuying how to use radare2. This wiki is constantly updated. Feel free to tweet to me [![Twitter URL](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/securisec) if there is a tidbit I can include in here. 

<center><img src="/uploads/r-2-logo-3.png" class="center"></center>


```
All the commands are based (started) with the following Radare version:
radare2 2.1.0-git 16575 @ linux-x86-64 git.2.0.1-245-g48bfa50
commit: 48bfa5087bed71be501e4c37933c0fe1298d817e build: 2017-11-14__02:43:49
Visual cues:
🚀 Means there is an asciinema
⭐ Great command to remember
❓ Means unverified or no information
```

## SecurisecCTF
SecurisecCTF is looking for new members! We are an open to all [Slack](http://invite.securisec.com) community focused on all aspects of information security, and CTF team! Anyone with any skill level is welcome to join. Our goal is to teach/learn from each other. #ctf #infosec [http://www.securisec.com](http://www.securisec.com) **This is not a radare2 group, or is not affiliated with radare2 in anyway** We do promote healthy discussions on reverse enginnering!

## Local web app
  - **Using wiki.js** > To get a local copy of this wiki check out [github](https://github.com/securisec/radare2_wiki)
  - **Using mkdocs** (Is slightly behind the wiki.js implementation)
		- `pip install mkdocs`
		- `git clone https://github.com/securisec/r2wiki-rtd.git`
		- `cd r2wiki-rtd`
		- `mkdocs serve`


## r2wiki.py
  - > ⭐ [Radare2 wiki can also be used right from the r2 shell. See directions here](./home/r2wiki-python)
# Sections

## Console options 😓
[Radare2 console options :heart_eyes:](./home/options)

## Valid architectures and cpu's
[Valid arch's and cpu's](./home/valid-arch-cpu)

## Radare2 Python scripting 🐍
[Radare2 Python scripting 🐍](./home/radare2-python-scripting)

## Radare2 tools ⚙️
[Radare2 tools](./home/radare2-tools)


## Radare Plugins
[Radare Plugins](./home/radare-plugins)


## Pwn helper
[Pwn helper](./home/pwn-helper)


## CTF solving / Blogs
[CTF solving using radare2 / Blogs](./home/ctf-solving-using-radare2)


## Tips
[Tips](./home/tips)


## Code samples
[Code samples](./home/code-samples)


## Debugger help
[Debugger help](./home/debugger-help)


# Analyzing different architectures / platforms
## Android
[Android reversing](./analysis/android)

## ARM
[ARM reversing](./analysis/arm)

## AVR
[AVR reversing](./analysis/avr)

## Go reversing
[Go reversing](./analysis/go)

## iOS 
[iOS reversing](./analysis/ios)

## Macho
[Macho reversing](./analysis/macho)

## Mips
[Mips reversing](./analysis/mips)
## Misc
[Misc reversing](./analysis/misc)

## Windows
[Windows reversing](./analysis/windows)

# Books / Resources

## Books

  [introduction · Radare2 Book](https://radare.gitbooks.io/radare2book/content/)

  [Introduction · Radare2 Explorations](https://monosource.gitbooks.io/radare2-explorations/content/)

   - > _Tutorial 3, memory manipulation is really good_

  [Plugins · Radare2 Book](https://radare.gitbooks.io/radare2book/content/plugins/plugins.html)

## Cheatsheets
  [Local copy of cheatsheet (obtained from radare2)](/home/misc/cheatsheet)

  [Radare2 Debugger Complete Cheat Sheet Flashcards | Quizlet](https://quizlet.com/182492323/radare2-debugger-complete-cheat-sheet-flash-cards/)

  [radare/radare2](https://github.com/radare/radare2/blob/master/doc/intro.md)

  [Reference Card · Radare2 Book](https://radare.gitbooks.io/radare2book/content/refcard/intro.html)

## Gui

  [Cutter](/home/cutter)

## Install

  - > If you are one a *nix system, install using github.

  - Pre packaged binaries for windows and other archs. 

    [Pre-packaged binaries](http://radare.mikelloc.com/get/)

## Resources
[Resources](/home/resources)

## Usage examples
[Usage examples directly from radare2 git](/home/misc/usage-examples)

## Plugin creation
[Help regarding plugin creation](https://radare.gitbooks.io/radare2book/content/plugins/plugins.html)

## Downloads
[Radare2 can be downloaded from here](http://radare.org/r/down.html)

## 📼 Videos
[Videos](/home/videos)

# Misc_help

## radare twitter feeds
[Twitter feed](./home/twitter-feed)

## IDA to radare2

  - [radare/radare2ida](https://github.com/radare/radare2ida)

   - _To convert IDA pro .idc or .idb files to be used in radare2, You can use `idc2r.py file.idc > file.r2` to convert IDA database to r2 format. This can then be loaded into radare2 using `. file.r2` inside the radare2 shell. Alternate method is to use `.!idc2r.py < file.idc` inside the radare2 shell_
		- > 🚀 IDA pro .idb files can be converted using `idb2r2.py` [asciinema](https://asciinema.org/a/kTKHNVUa3ocnGhNYCv73Xh4Uk)
			 - Dependencies: idb `pip install python-idb`
- [Latest version of idb2r2.py](https://github.com/radare/radare2ida/blob/master/ida2r2/idb2r2.py)

## Radare2 themes

- > See previews of all the [Themes](./home/themes) 

- > [Theme modification options](/options/e/ec)

## Misc r2 helpers
[Misc r2 helpers](/home/misc_helpers)
	

## IRC: irc.freenode.net #radare 

[radare (@radareorg) | Twitter](https://twitter.com/radareorg)

