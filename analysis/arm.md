<!-- TITLE: Arm -->

> Work in progress {.is-danger}
# Tips
- `e asm.bits=16`  # set thumb2 mode
- `e asm.bits=32`  # set ARM mode
- `e asm.describe = true`   # show description of each ARM instruction
- `e asm.pseudo = true  `   # show pseudo instruction instead of assembly
- `e asm.emu = true     `   # emulate code using ESIL
- `e asm.emustr = true  `   # show string and method referenced in the emu comments
- `e anal.hasnext=true  `   # assume a new function is found after the last one
- `e dbg.dpsize = 2` # set to 2 for arm debugging. Default is 1

# Environment setup (tested on Ubuntu 16.04)
## Install qemu, gdb and its dependencies
	```sh
	##### Update #####
	sudo apt update -y

	##### Install Qemu #####
	sudo apt -y install qemu

	##### Install gdb-multiarch #####
	sudo apt -y install gdb-multiarch

	##### Install ARM Libs #####
	sudo apt -y install 'binfmt*'
	sudo apt -y install libc6-armhf-armel-cross
	sudo apt -y install gcc-arm-linux-gnueabihf
	sudo mkdir -p /etc/qemu-binfmt
	sudo ln -s /usr/arm-linux-gnueabihf /etc/qemu-binfmt/arm
	sudo mkdir -p /lib/arm-linux-gnueabihf/
	sudo ln -s /usr/arm-linux-gnueabihf/lib/libc.so.6 /lib/arm-linux-gnueabihf/libc.so.6
	sudo ln -s /usr/arm-linux-gnueabihf/lib/ld-linux-armhf.so.3 /lib/ld-linux-armhf.so.3
	```

## Debug a binary
- Load the binary with `qemu-arm -g [port] ./[binary]`
- `r2 -d gdb://localhost:1234`
# Videos
[video](https://www.youtube.com/watch?v=oXSx0Qo2Upk){.youtube}