<!-- TITLE: rabin2 -->

# rabin2

## **Tips**
  - Use `rabin2 -l binary` to list its direct dependencies.
## Help

      Usage: rabin2 [-AcdeEghHiIjlLMqrRsSUvVxzZ] [-@ at] [-a arch] [-b bits] [-B addr]
       [-C F:C:D] [-f str] [-m addr] [-n str] [-N m:M] [-P[-P] pdb]
       [-o str] [-O str] [-k query] [-D lang symname] | file
       -@ [addr] show section, symbol or import at addr
       -A list sub-binaries and their arch-bits pairs
       -a [arch] set arch (x86, arm, .. or <arch>_<bits>)
       -b [bits] set bits (32, 64 ...)
       -B [addr] override base address (pie bins)
       -c list classes
       -cc list classes in header format
       -C [fmt:C:D] create [elf,mach0,pe] with Code and Data hexpairs (see -a)
       -d show debug/dwarf information
       -D lang name demangle symbol name (-D all for bin.demangle=true)
       -e entrypoint
       -ee constructor/destructor entrypoints
       -E globally exportable symbols
       -f [str] select sub-bin named str
       -F [binfmt] force to use that bin plugin (ignore header check)
       -g same as -SMZIHVResizcld (show all info)
       -G [addr] load address . offset to header
       -h this help message
       -H header fields
       -i imports (symbols imported from libraries)
       -I binary info
       -j output in json
       -k [sdb-query] run sdb query. for example: '*'
       -K [algo] calculate checksums (md5, sha1, ..)
       -l linked libraries
       -L [plugin] list supported bin plugins or plugin details
       -m [addr] show source line at addr
       -M main (show address of main symbol)
       -n [str] show section, symbol or import named str
       -N [min:max] force min:max number of chars per string (see -z and -zz)
       -o [str] output file/folder for write operations (out by default)
       -O [str] write/extract operations (-O help)
       -p show physical addresses
       -P show debug/pdb information
       -PP download pdb file for binary
       -q be quiet, just show fewer data
       -qq show less info (no offset/size for -z for ex.)
       -Q show load address used by dlopen (non-aslr libs)
       -r radare output
       -R relocations
       -s symbols
       -S sections
       -u unfiltered (no rename duplicated symbols/sections)
       -U resoUrces
       -v display version and quit
       -V Show binary version information
       -x extract bins contained in file
       -X [fmt] [f] .. package in fat or zip the given files and bins contained in file
       -z strings (from data section)
       -zz strings (from raw bins [e bin.rawstr=1])
       -zzz dump raw strings to stdout (for huge files)
       -Z guess size of binary program