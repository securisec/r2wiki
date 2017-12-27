<!-- TITLE: Go reversing-->

# Helpers
[zlowram/radare2-scripts](https://github.com/zlowram/radare2-scripts/tree/master/go_helpers)
	> *To run, from inside r2 console, use `#!pipe python ./file.py` or `. ./file.py`* {.is-info}

- _load_pclntab_info.py_
	- Before

					0x00478460 312 11720 fcn.00478460
					0x0047b230 19 512 fcn.0047b230
					0x0047b490 16 410 fcn.0047b490
					0x0047b760 5 177 fcn.0047b760
					0x0047b820 5 125 fcn.0047b820

	- After

					0x0047b8a0 19 947 main.main
					0x0047bc60 3 72 main.mapanic.func1
					0x0047bcb0 7 96 main.init
					0x0047bd10 5 119 type..hash._3_interface___
					0x0047bd90 8 176 type..eq._3_interface___
# Videos
[video](https://www.youtube.com/watch?v=PRLOlY4IKeA){.youtube}