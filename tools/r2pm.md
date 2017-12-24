<!-- TITLE: r2pm -->

# r2pm (radare2 package manager)

Radare package manager

## Error: `checking pkg-config flags for r_core... no`
  - `sudo apt install pkg-config` (tested on Ubuntu 16.04)
## Help

      Usage: r2pm [init|update|cmd] [...]
      Commands:
       -i,info show information about a package
       -i,install <pkgname> install package in your home (pkgname=all)
       -gi,global-install <pkg> install package system-wide
       -gu,global-uninstall <pkg> uninstall pkg from systemdir
       -u,uninstall <pkgname> r2pm -u baleful (-uu to force)
       -l,list list installed pkgs
       -r,run [cmd ...args] run shell command with R2PM_BINDIR in PATH
       -s,search [<keyword>] search in database
       -t,test FX,XX,BR BID check in Travis regressions
       -v,version show version
       -h,help show this message
       -H variable show value of given variable
       -c,clean ([git/dir]) clear source cache (GITDIR)
       -ci (pkgname) clean install of given package
       -d,doc [pkgname] show documentation for given package
       -w <pkgname> what/where is installed
       init | update .. initialize/update database
       cd [git/dir] cd into given git (see 'r2pm ls')
       ls ls all cloned git repos in GITDIR
       suicide self remove all (home + system) installations of r2

- `r2pm init` to initialize the package control
- `r2pm update` to update git
- `r2pm -i all` to install all packages
- `r2pm suicide` to self remove r2 from system and home

<p hidden>suicide</p>