<!-- TITLE: r2pm -->

# r2pm (radare2 package manager)

Radare package manager

## Error: `checking pkg-config flags for r_core... no`
  - `sudo apt install pkg-config` (tested on Ubuntu 16.04)

## Packages
[Packages and package help can be found here](/home/radare-plugins)
## Help


```text
 -i,info                     show information about a package
 -i,install <pkgname>        install package in your home (pkgname=all)
 -gi,global-install <pkg>    install package system-wide
 -gu,global-uninstall <pkg>  uninstall pkg from systemdir
 -u,uninstall <pkgname>      r2pm -u baleful (-uu to force)
 -l,list                     list installed pkgs
 -r,run [cmd ...args]        run shell command with R2PM_BINDIR in PATH
 -s,search [<keyword>]       search in database
 -t,test FX,XX,BR BID        check in Travis regressions
 -v,version                  show version
 -h,help                     show this message
 -H variable                 show value of given variable
 -c,clean ([git/dir])        clear source cache (GITDIR)
 -ci (pkgname)               clean install of given package
 -cp                         clean the user's home plugin directory
 -d,doc [pkgname]            show documentation for given package
 -w <pkgname>                what/where is installed
 init | update ..            initialize/update database
 cd [git/dir]                cd into given git (see 'r2pm ls')
 ls                          ls all cloned git repos in GITDIR
 suicide                     self remove all (home + system) installations of r2
```


- `r2pm init` to initialize the package control
- `r2pm update` to update git
- `r2pm -i all` to install all packages
- `r2pm suicide` to self remove r2 from system and home

## r2pm man page

```text
R2PM(1)                                      BSD General Commands Manual                                      R2PM(1)

NAME
     R2PM — radare2 package manager

SYNOPSIS
     r2pm [init|update|cmd] [...]

DESCRIPTION
     Allows to install, update, uninstall and discover plugins and tools that can be used with radare2.

     -a, repo    Adds an external r2pm repository, no arguments to -a will list all the registered repos, use '-a -
                 repo' to unregister/remove those repos.

     -i, info    Show information about repository and installed packages

     -i, install pkgname
                 Install a package

     -gi, global-install pkgname
                 Install a package in the system directory

     -t, test [OK|FX|BR|XX] [build-id]
                 Show last build + testsuite run from travis, greps for errors

     -u, uninstall pkgname
                 Uninstall a package

     -gu, global-install pkgname
                 Uninstall a package from the system directory

     -l, list    List installed packages

     -s, search keyword
                 Search in database for packages matching keyword

     -r, run command ...args
                 Run command with R2PM_BINDIR in PATH

     -v, version
                 Show version information

     -h, help    Show usage help message

     -c, clean   Clean the source cache

     -w, when    Show when a package was installed or exit 1 if pkg does not exist

EXAMPLES
     Initialize and update the package database

       $ r2pm init
       $ r2pm update

     Install a package

       $ r2pm install yara3

     Uninstall a package

       $ r2pm uninstall yara3

     Search a package

       $ r2pm search yara

     List available packages

       $ r2pm -s

SEE ALSO
     radare2(1)

                                                     Jun 7, 2016

```


<p hidden>suicide</p>