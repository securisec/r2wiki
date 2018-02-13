<!-- TITLE: radiff2 -->

# radiff2

## Tips
  - After installing xdot ( `sudo apt install xdot` ), you can graph the difference between two binaries. Syntax is, `radiff2 -g function_name binary1 binary | xdot -`
    - Yellow indicates some offsets doesnt match, grey is perfect match and red shows a strong difference (radare2 book page 148)
## Help

      Usage: radiff2 [-abcCdjrspOxuUvV] [-A[A]] [-g sym] [-t %] [file] [file]
       -a [arch] specify architecture plugin to use (x86, arm, ..)
       -A [-A] run aaa or aaaa after loading each binary (see -C)
       -b [bits] specify register size for arch (16 (thumb), 32, 64, ..)
       -c count of changes
       -C graphdiff code (columns: off-A, match-ratio, off-B) (see -A)
       -d use delta diffing
       -D show disasm instead of hexpairs
       -e [k=v] set eval config var value for all RCore instances
       -g [sym|off1,off2] graph diff of given symbol, or between two offsets
       -G [cmd] run an r2 command on every RCore instance created
       -i diff imports of target files (see -u, -U and -z)
       -j output in json format
       -n print bare addresses only (diff.bare=1)
       -O code diffing with opcode bytes only
       -p use physical addressing (io.va=0)
       -q quiet mode (disable colors, reduce output)
       -r output in radare commands
       -s compute edit distance (no substitution, Eugene W. Myers' O(ND) diff algorithm)
       -ss compute Levenshtein edit distance (substitution is allowed, O(N^2))
       -S [name] sort code diff (name, namelen, addr, size, type, dist) (only for -C or -g)
       -t [0-100] set threshold for code diff (default is 70%)
       -x show two column hexdump diffing
       -u unified output (---+++)
       -U unified output using system 'diff'
       -v show version information
       -V be verbose (current only for -s)
       -z diff on extracted strings
			 
## radiff2 man page

```text
RADIFF2(1)                                   BSD General Commands Manual                                   RADIFF2(1)

NAME
     RADIFF2 — unified binary diffing utility

SYNOPSIS
     radiff2 [-AabcCdDhOrspxvz] [-t 0-100] [-g sym] [-S algo] file1 file2

DESCRIPTION
     radiff2 implements many binary diffing algorithms for data and code.

     -A          Analyze binary after loading it with RCore (see -C) and use -AA to run aaaa instead of aaa.

     -a          Specify architecture (x86, arm, ..)

     -b          Select register size bits for given arch

     -B          Binary output (GDIFF format)

     -c          Count number of differences.

     -e -[k=v]   Specify eval config vars for all RCore instances created.

     -C          Code diffing using graphdiff algorithm. Output columns are: file-a-address, percentage of most simi‐
                 lar function in B file | file-b-address. (Use with -A to analyze the binaries to find more func‐
                 tions)

     -d          Use delta diffing (slower).

     -D          Show disasm instead of hexpairs (honors -a arch and -b bits)

     -g sym | off1,off2
                 Graph diff output of given symbol, or between two functions, at given offsets: one for each binary.

     -h          Show usage help message.

     -i          Compare the list of imports

     -n          Suppress address names (show only addresses) when code diffing.

     -O          Do code diffing with all bytes instead of just the fixed opcode bytes

     -p          Use physical addressing (io.va=0)

     -q          Quiet mode: disable colors and reduce output

     -r          Output in radare commands as a binary patch.

     -x          Show two column hexdump diffing.

     -s          Calculate text distance from two files.

     -ss         Same as before but using the Levenstein algorithm (faster but sometimes buggy)

     -S [name, namelen, dist, size, ...]
                 Specify which column of the code diffing algo use for diffing

     -t 0-100    Choose matching threshold for binary code diffing

     -u          Unified diff output

     -U          Unified diff output using system´s diff program

     -v          Show version information.

     -V          Be verbose sometimes

     -z          Perform diff on extracted strings

SEE ALSO
     radare2(1), rafind2(1), rahash2(1), rabin2(1), rasm2(1), ragg2(1), rarun2(1), rax2(1),

AUTHORS
     pancake <pancake@nopcode.org>

                                                     Feb 10, 2018

```


[Binary diffing · The Official Radare Blog](http://radare.today/posts/binary-diffing/)