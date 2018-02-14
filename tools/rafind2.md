<!-- TITLE: rafind2 -->

# rafind2

## Help

      Usage: rafind2 [-mXnzZhv] [-a align] [-b sz] [-f/t from/to] [-[e|s|S] str] [-x hex] file ..
       -a [align] only accept aligned hits
       -b [size] set block size
       -e [regex] search for regex matches (can be used multiple times)
       -f [from] start searching from address 'from'
       -h show this help
       -i identify filetype (r2 -nqcpm file)
       -m magic search, file-type carver
       -M [str] set a binary mask to be applied on keywords
       -n do not stop on read errors
       -r print using radare commands
       -s [str] search for a specific string (can be used multiple times)
       -S [str] search for a specific wide string (can be used multiple times)
       -t [to] stop search at address 'to'
       -v print version and exit
       -x [hex] search for hexpair string (909090) (can be used multiple times)
       -X show hexdump of search results
       -z search for zero-terminated strings
       -Z show string found on each search hit

## rafind2 man page

```
RAFIND2(1)                                   BSD General Commands Manual                                   RAFIND2(1)

NAME
     rafind2 — Advanced commandline hexadecimal editor

SYNOPSIS
     rafind2 [-izZXnrhv] [-b size] [-f from] [-t to] [-[m|s|e] str] [-x hex] file

DESCRIPTION
     rafind2 is a program to find byte patterns into files

     The options are:

     -z          Search for zero-terminated strings

     -a align    Only accept aligned hits

     -s str      Search for a specific string

     -S str      Search for a specific wide string

     -e regex    Search for a regular expression string matches

     -x hex      Search for an hexpair string

     -i          Identify filetype (like file, uses r2 -qcpm)

     -m          Carve for known file-types using the r_magic signatures

     -M mask     Set binary mask to be applied

     -f from     Specify the source adddress

     -t to       Specify the target adddress

     -X          Display hexdump of search results

     -Z          Display zero-terminated strings results

     -n          Do not stop the search when a read error occurs

     -r          Show output in radare commands

     -b size     Define block size

     -h          Show help message

     -v          Print version and exit

SEE ALSO
     radare2(1), rahash2(1), rabin2(1), radiff2(1), rasm2(1), ragg2(1), rarun2(1), rax2(1),

AUTHORS
     pancake <pancake@nopcode.org>

                                                     Oct 19, 2015

```

## pcaps
  - rafind2 -X -s "DOS mode" traffic.pcap
  - rafind2 -Z -s "Subject" smtp.pcap