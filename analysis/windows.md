<!-- TITLE: Windows reversing-->

# Installing / Building
### Installing from pre packaged binaries
[Instructions on building for Windows OLD](https://github.com/radare/radare2/blob/master/doc/windows.md)
[These pre packaged binaries/installers are not always up to date](http://radare.mikelloc.com/get/)
## Building
- Requirements
	- Python
	- [Python meson build](https://github.com/mesonbuild/meson)
	- [Ninja](https://ninja-build.org/)

> To compile radare2, simply run `meson.bat`
- `meson.bat -p` outputs a Visual Studio project file

## Config file
- To find the location of the radare2rc config file for windows, run `r2 -hh` and look for the environment variable `RHOMEDIR`

## Using an installer
To get the latest installer, [go to this site](https://ci.appveyor.com/project/radare/radare2-shvdd) or [this site](http://radare.mikelloc.com/get/) and click the appropiate job name (32 vs 64bit) and then click artifacts to download the installer. The installer adds right click context for any file

# DLL support
## dll support using rarun2
> Syntax is `rarun2.exe runlib=[path\to\library] runlib.fcn=[function_name] [arg1=argument1 arg2=argument2...]`.
- Example: `rarun2.exe runlib=C:\Windows\System32\user32.dll runlib.fcn=MessageBoxA arg1=%0 arg2=Body arg3=Title arg4=%1`
- It should be possible to use a rarun2 profile to debug a dll in this manner. 

## dll resources
[Snojan analysis](https://medium.com/@jacob16682/snojan-analysis-bb3982fb1bb9)

# PDB support
> Helpful: `cabextract` in linux

- 🚀 Use `idpi` to show show debug information about a file. [asciinema](https://asciinema.org/a/BOQUwqIJO497zhFDY037uNf6W)
- Use `idpd` to download available files
- 🚀 Use `.idpi*` to populate the flag space `fs`. [asciinema](https://asciinema.org/a/mBKmRaszDXe8C55as7Oo2cVVf)
- `e pdb.server` can be used to configure differnt pdb server. Default is Microsoft. `e pdb.autoload` can be set to 1 to automatically download pdb files if available. 

# Resources
## CTF Windows binaries
[flareon 2015 2nd challenge](https://fevral.github.io/2017/08/13/flareon2015-2.html)

# Windows malware / scripts
- ⭐[r2msdn](https://github.com/securisec/r2msdn)
	- > Used to automatically annotated MSDN function description and args
- [malware_analysis_tools](https://github.com/redmed666/malware_analysis_tools)
# Videos
[video](https://www.youtube.com/watch?v=2gcqLDGnKMc){.youtube}

<p hidden>idp idpd idpi</p>
