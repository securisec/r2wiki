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

## pcaps
  - rafind2 -X -s "DOS mode" traffic.pcap
  - rafind2 -Z -s "Subject" smtp.pcap