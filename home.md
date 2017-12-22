# Radare

**Principle author** : Hapsida (@securisec)

This is an ongoing work in progress and reflects various material obtained during stuying how to user r2. This wiki is constantly updated and will hopefully be fully searchable one day. Feel free to tweet to me `@securisec` if there is a tidbit I can include in here.

    All the commands are based (started) with the following Radare version:
    radare2 2.1.0-git 16575 @ linux-x86-64 git.2.0.1-245-g48bfa50
    commit: 48bfa5087bed71be501e4c37933c0fe1298d817e build: 2017-11-14__02:43:49

# Sections

[Options](./Options-c322f9f5-fc3e-426a-b9c8-e718216bdb9b.md)

[Radare2 Python scripting](./Radare2-Python-scripting-f62ea1cf-6b4c-4fd1-bffa-c5628f9b16d7.md)

[Radare2 tools](./Radare2-tools-b38ae017-e1b0-4d72-9bb4-d4aefdbd3f16.md)

[Radare Plugins](./Radare-Plugins-8fc9a9d1-dea8-4417-bae5-c4dccde5d273.md)

[Pwn helper](./Pwn-helper-909a42a7-2ab5-4e39-a9dd-7bc496e7e5a2.md)

[CTF solving using radare2](./CTF-solving-using-radare2-80ddb7c2-1fc6-4e89-aaa7-a1b22a49d942.md)

[Tips](./Tips-203f2ab5-a46d-4737-b8e2-14b89e008ddc.md)

[Code samples](./Code-samples-6fbd05f4-01ee-447d-876c-27ed65f6a9c2.md)

[Debugger help](./Debugger-help-21263424-c22b-4c90-9d9a-20a43436f858.md)

[Analysis Help (go, arm, ios etc)](./Analysis-Help-go-arm-ios-etc-1bac9418-523f-45e9-9376-c469af14959c.md)

# [Books / Resources](http://google.com)

## Books

  [introduction · Radare2 Book](https://radare.gitbooks.io/radare2book/content/)

  [Introduction · Radare2 Explorations](https://monosource.gitbooks.io/radare2-explorations/content/)

   > _Tutorial 3, memory manipulation is really good_ {.is-info}

  [Plugins · Radare2 Book](https://radare.gitbooks.io/radare2book/content/plugins/plugins.html)

## Cheatsheets

  [Radare2 Debugger Complete Cheat Sheet Flashcards | Quizlet](https://quizlet.com/182492323/radare2-debugger-complete-cheat-sheet-flash-cards/)

  [radare/radare2](https://github.com/radare/radare2/blob/master/doc/intro.md)

  [Reference Card · Radare2 Book](https://radare.gitbooks.io/radare2book/content/refcard/intro.html)

## Gui

  [radareorg/cutter](https://github.com/radareorg/cutter)

## Install

  > If you are one a *nix system, install using github.
  {.is-success}

  - Pre packaged binaries

    [Pre-packaged binaries](http://radare.mikelloc.com/get/)

[Resources](./Resources-09912c2c-cfe9-4e26-8f7b-25e7a6268f34.md)

[Videos](./Videos-f6209288-e2bf-4623-ad81-e577e8e71def.md)

# Stuff

## IDA to radare2

  [radare/radare2ida](https://github.com/radare/radare2ida)

   > _You can use `idc2r.py file.idc > file.r2` to convert IDA database to r2 format. This can then be loaded into radare2 using `. file.r2` inside the radare2 shell. Alternate method is to use `.!idc2r.py < file.idc` inside the radare2 shell_ {.is-info}

## Radare2 themes

  See previews of all the [Themes](./themes) 

## **IRC: irc.freenode.net #radare** 

[radare (@radareorg) | Twitter](https://twitter.com/radareorg)

![](https://static.notion-static.com/754c9573-76a3-4f3f-9aa6-f3326ae85b1a/r2_learning_curve.png){.align-center}