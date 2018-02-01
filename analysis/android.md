<!-- TITLE: Android -->

# Tips
## Helpful commands for Android reversing
- `ic` to enumerate classes and methods from a .dex file
- `icq` to enumerate classes
- `iiq` show external methods
- `izq` list all strings contained in the program

## Helpful commands for arm reversing
- `e asm.describe = true`   # show description of each ARM instruction
- `e asm.pseudo = true  `   # show pseudo instruction instead of assembly
- `e asm.emu = true     `   # emulate code using ESIL
- `e asm.emustr = true  `   # show string and method referenced in the emu comments
- `e anal.hasnext=true  `   # assume a new function is found after the last one

## General
- Use `V_` to seach through strings (including classes and methods) in the visual mode HUD mode. 
- r2pm supports installation of dex2jar. dex2jar can be used to convert dex files into jar files. `r2pm -i dex2jar`


# Resources
[Android malware analysis with Radare: Dissecting the Triada Trojan](https://www.nowsecure.com/blog/2016/11/21/android-malware-analysis-radare-triada-trojan/)
[Oneplus backdoor analysis](https://www.nowsecure.com/blog/2017/11/14/oneplus-device-root-exploit-backdoor-engineermode-app-diagnostics-mode/)

## Complimentary tools
[termux](https://termux.com/)
# Installing
## Installing from pre built
- Download the latest from `http://radare.mikelloc.com/get/[version]/[android-arch]`
- Push to android device with `adb push data/ /`
- From `adb shell` launch `/data/data/org.radare.radare2installer/radare2/bin/r2[or any other r2 binaries]`
## Documentation for building
[Documents around installing r2 on android](/home/misc/usage-examples#android)