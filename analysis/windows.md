<!-- TITLE: Windows reversing-->

# Windows support / reversing
## Installing / Building
### Installing from pre packaged binaries
[These pre packaged binaries/installers are not always up to date](http://radare.mikelloc.com/get/)
### Building
- Requirements
	- Python
	- [Python meson build](https://github.com/mesonbuild/meson)
	- [Ninja](https://ninja-build.org/)

> To compile radare2, simply run `meson.bat` {.is-info}
- `meson.bat -p` outputs a Visual Studio project file

## DLL support
### dll support using rarun2
> Syntax is `rarun2.exe runlib=[path\to\library] runlib.fcn=[function_name] [arg1=argument1 arg2=argument2...]`. {.is-info}
- Example: `rarun2.exe runlib=C:\Windows\System32\user32.dll runlib.fcn=MessageBoxA arg1=%0 arg2=Body arg3=Title arg4=%1`

## PDB support
> Dependencies: `cabextract` in linux

- Use `idp` to show show debug information about a file.
- Use `idpd` to download available files
- `e pdb.server` can be used to configure differnt pdb server. Default is Microsoft. `e pdb.autoload` can be set to 1 to automatically download pdb files if available. 

## Videos
[video](https://www.youtube.com/watch?v=2gcqLDGnKMc){.youtube}