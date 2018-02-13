<!-- TITLE: ec -->

#  `ec [k] [color]` set color for given key (prompt, offset, ...)


```text
Usage ec[s?] [key][[=| ]fg] [bg]
```


- `ec` list all color keys
	> 🚀 [Values that can be modifed using `ec` and theme example can be found here](/options/e/ec/ec-values). Colors can be changed to create custom themes. Custom themes can be placed in `radare2/libr/cons/d/` folder. [asciinema](https://asciinema.org/a/eVDMKMAvyXYJcWwJyym1BlI5O)
	
	> `ec usrcmt color` to change comment color
- `ec*` same as above, but using r2 commands
- `ecd` 🚀 set default palette [asciinema](https://asciinema.org/a/ZAJTa5eO2ppMdqNwluzLXqVJY)
- `ecr` 🚀 set random palette (see also scr.randpal) [asciinema](https://asciinema.org/a/8mHk3kVjzpZ1Ighs9BIiqf5AX)
- `ecs` 🚀 show a colorful palette [asciinema](https://asciinema.org/a/iUiw2j81mdmlaijEpAH4ewOI8)
- `ecj` show palette in JSON
- `ecc [prefix]` show palette in CSS
- `eco dark|white` load white color scheme template
  > _Use eco to see a list of themes_

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

<p hidden>ec ec* ecd ecr ecs ecj ecc eco ecp ecn ecH usrcmt</p>