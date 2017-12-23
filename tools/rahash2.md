<!-- TITLE: rahash2 -->

# rahash2

## **Tips**
  - WARNING - Do not try to use rahash2 on a big file as it attempts to load the entire file in memory first.
  - Use `all` as the hash type to calculate all hash types available
## Help

      Usage: rahash2 [-rBhLkv] [-b S] [-a A] [-c H] [-E A] [-s S] [-f O] [-t O] [file] ...
       -a algo comma separated list of algorithms (default is 'sha256')
       -b bsize specify the size of the block (instead of full file)
       -B show per-block hash
       -c hash compare with this hash
       -e swap endian (use little endian)
       -E algo encrypt. Use -S to set key and -I to set IV
       -D algo decrypt. Use -S to set key and -I to set IV
       -f from start hashing at given address
       -i num repeat hash N iterations
       -I iv use give initialization vector (IV) (hexa or s:string)
       -S seed use given seed (hexa or s:string) use ^ to prefix (key for -E)
       (- will slurp the key from stdin, the @ prefix points to a file
       -k show hash using the openssh's randomkey algorithm
       -q run in quiet mode (-qq to show only the hash)
       -L list all available algorithms (see -a)
       -r output radare commands
       -s string hash this string instead of files
       -t to stop hashing at given address
       -x hexstr hash this hexpair string instead of files
       -v show version information