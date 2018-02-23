<!-- TITLE: iOS reversing -->

# Debugging
## r2lldb
[r2lldb](/radare-plugins/r2lldb)

# Installation
- [From radare2 git](https://github.com/radare/radare2/blob/master/doc/iphone.md)
- > Dependencies: jail broken iOS device

## Pre built binaries
- [Pre built binaries can be found here](http://radare.mikelloc.com/get/)
## Use Cydia
- > Most likely out of date
	- [Cydia repository](http://cydia.radare.org/)


## Building from Git
- > Dependencies: ios-sdk-gcc
- Clone r2 from git
- Run `sys/ios-cydia.sh`
- Copy over `radare2/sys/cydia/radare2/radare2...dev` to device
- Install with `dpkg -i radare2...deb`
- Add correct entitlements (inside iOS device)
	- `ldid -S radare.xml /usr/bin/radare2`
- [video](https://youtu.be/OlzUdbvDLuA?t=685)
# Resources
- [Documentation from radare2 git](https://github.com/radare/radare2/blob/master/doc/ios.md)
- [Loading iOS binaries](http://radare.today/posts/loading-ios-binaries/)
- [Handling encrypted iOS files](https://youtu.be/OlzUdbvDLuA?t=544)
	- Struct type of encrpyted iOS binaries with `pf`. `pf macho0_cmd_enc=didid cmd cmdsize cryptoff cryptsize cryptid`
	- [Steps to decrypt a binary](https://youtu.be/OlzUdbvDLuA?t=822)
- Use `rabin2 -x [file]` to extract the Mach-O file from the package.

## Plugins
- [r2clutch](https://github.com/as0ler/r2clutch)
	- r2clutch is used to decrypt an iOS binary
	- Dependencies
		- Needs r2 in iOS device
		- Python in iOS device (not tested)
# Videos
[r2clutch r2con 2016](https://www.youtube.com/watch?v=OlzUdbvDLuA)
[How to Start iOS Hacking | Reverse Engineering With Radare2](https://www.youtube.com/watch?v=hy81mnLMvnE)
[Nowsecure top OSS Mobile testing](https://www.brighttalk.com/webcast/15139/304637?utm_campaign=knowledge-feed&utm_source=brighttalk-portal&utm_medium=web)
