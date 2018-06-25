<!-- TITLE: ec -->

#  `ec [k] [color]` set color for given key (prompt, offset, ...)


```
Usage ec[s?] [key][[=| ]fg] [bg]
```


- `ec` list all color keys
	- > 🚀 [Values that can be modifed using `ec` and theme example can be found here](/options/e/ec/ec-values). Colors can be changed to create custom themes. Custom themes can be placed in `radare2/libr/cons/d/` folder. [asciinema](https://asciinema.org/a/eVDMKMAvyXYJcWwJyym1BlI5O)
	
	- > `ec usrcmt color` to change comment color
- `ec*` same as above, but using r2 commands
- `ecd` 🚀 set default palette [asciinema](https://asciinema.org/a/ZAJTa5eO2ppMdqNwluzLXqVJY)
- `ecr` 🚀 set random palette (see also scr.randpal) [asciinema](https://asciinema.org/a/8mHk3kVjzpZ1Ighs9BIiqf5AX)
- `ecs` 🚀 show a colorful palette [asciinema](https://asciinema.org/a/iUiw2j81mdmlaijEpAH4ewOI8)
- `ecj` show palette in JSON
- `ecc [prefix]` show palette in CSS
- `eco dark|white` load white color scheme template
  - > _Use eco to see a list of themes_

    - [Themes](/home/themes)

- `ecp` 🚀 load previous color theme [asciinema](https://asciinema.org/a/L3Dy3KOAuPpXJr7PrqYqOj0oq)
- `ecn` 🚀 load next color theme [asciinema](https://asciinema.org/a/L3Dy3KOAuPpXJr7PrqYqOj0oq)

- [ `ecH[?]` highlight word or instruction](/options/e/ec/ec_cap_h)

- `ec prompt red` 🚀 change color of prompt [asciinema](https://asciinema.org/a/mYzg8U4nuoX4oyQw6rVlndW8v)
- `ec prompt red blue` 🚀 change color and background of prompt [asciinema](https://asciinema.org/a/mYzg8U4nuoX4oyQw6rVlndW8v)
- `colors:` rgb:000, red, green, blue, ...
- `e scr.rgbcolor=1|0` for 256 color cube (boolean)
- `e scr.truecolor=1|0` for 256 _256_ 256 colors (boolean)
- `$DATADIR/radare2/cons` ~/.config/radare2/cons ./


## Theme modification values
```text
ec ai.exec 
ec ai.read 
ec ai.write 
ec args 
ec b0x00              # 00 bytes
ec b0x7f 
ec b0xff              # ff bytes
ec bin                # operations like xor
ec btext              # text section opcode? first byte of opcode
ec call               # call instructions
ec cjmp               # je, jg, etc
ec cmp                # cmp instructions
ec comment            # r2 renerated comments
ec creg               # modified registries
ec flag               # flags. usually apprears above the current seek
ec fline              # function line. the boundary of a function
ec flow               # lines that show jump destinations
ec flow2 
ec fname              # function name
ec graph.box          # unselected boxes in visual graph mode
ec graph.box2         # currently selected box in visual graph mode
ec graph.box3 
ec graph.box4 
ec graph.current 
ec graph.false        # false line on visual graph mode
ec graph.true         # true line on visual graph mode
ec graph.trufae       # lines in graph that does not have true or false
ec help               # color of help explanation text
ec input 
ec jmp                # jmp instructions
ec label 
ec linehl             # highlight color when using asm.highlight
ec math               # math instructions like sub, add
ec mov                # mov instructions
ec nop                # nop instructions
ec num                # numbers
ec offset             # offset in visual mode
ec other 
ec pop                # pop instructions
ec prompt             # color for main r2 prompt
ec push               # push instructions
ec reg                # register names
ec ret                # ret opcode
ec swi 
ec trap                  
ec usrcmt            # user comment

```

<p hidden>ec ec* ecd ecr ecs ecj ecc eco ecp ecn ecH usrcmt</p>