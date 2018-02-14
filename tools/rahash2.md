<!-- TITLE: rahash2 -->

# rahash2

## Tips
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
			 
## Available Hashes

```
Available Hashes: 
  md5
  sha1
  sha256
  sha384
  sha512
  crc16
  crc32
  md4
  xor
  xorpair
  parity
  entropy
  hamdist
  pcprint
  mod255
  xxhash
  adler32
  luhn
  crc8smbus
  crc15can
  crc16hdlc
  crc16usb
  crc16citt
  crc24
  crc32c
  crc32ecma267

Available Encoders/Decoders: 
  base64
  base91
  punycode

Available Crypto Algos: 
  rc2
  rc4
  rc6
  aes-ecb
  aes-cbc
  ror
  rol
  rot
  blowfish
  cps2
  des-ecb
  xor
  serpent-ecb
```

## rahash2 man page

```
RAHASH2(1)                                   BSD General Commands Manual                                   RAHASH2(1)

NAME
     rahash2 — block based hashing utility

SYNOPSIS
     rahash2 [-BdDehjrkvq] [-a algorithm] [-b size] [-D algo] [-E algo] [-s string] [-i iterations] [-I IV] [-S seed]
             [-f from] [-x hexstr] [-t to] [-c hash] [[file] ...]

DESCRIPTION
     This program is part of the radare project.

     Rahash2 allows you to calculate, check and show the hash values of each block of a target file. The block size
     is 32768 bytes by default. It's allowed to hash from stdin using '-' as a target file. You can compare against a
     known hash and get the result in the exit status.

     You can hash big files by hashing each block and later determine what part of it has been modified. Useful for
     filesystem analysis.

     This command can be used to calculate hashes of a certain part of a file or a command line passed string.

     This is the command used by the 'ph' command of radare.

     -a algo     Select an algorithm for the hashing. Valid values are listed in: rahash2 -L

     -b blocksize
                 Define the block size

     -c hash     Compare the computed hash with this one. Allowed only when a single hash is computed.

     -D algo     Decrypt instead of hash using the given algorithm (base64, base91, rc4, aes, xor, blowfish, rot,
                 rol, ror, rc2, rc6, punycode)

     -e          Use little endian to display checksums

     -E algo     Encrypt instead of hash using the given algorithm (base64, base91, rc4, aes, xor, blowfish, rot,
                 rol, ror, rc2, rc6, punycode)

     -i iters    Apply the hash Iters times to itself+seed

     -I [^]s:string|hexstr
                 Set initialization vector (IV) for the cryptographic functions.

     -j          Show output in JSON (see -r)

     -B          Show per-block hash

     -k          Show result using OpenSSH's VisualHostKey randomart algorithm

     -s string   Hash this string instead of using the 'source' and 'hash-file' arguments.

     -S [^]s:string|hexstr
                 Set seed to hash with, use ^to prefix seed, otherwise its suffixed. If the seed is just a dash '-'
                 it will read from stdin, this is useful to provide huge XOR payloads or other crypto keys bigger
                 than few bytes.

     -f from     Start hashing at given address

     -t to       Stop hashing at given address

     -q          Quiet mode (-qq for even quieter!)

     -r          Show output in radare commands

     -x hexstr   Hash the given hexpair string instead of using the 'source' and 'hash-file' arguments.

     -v          Show version information

     -h          Show usage help message.

DIAGNOSTICS
     The rahash2 utility exits 0 on success, and >0 if an error occurs.

     When -c is used, exit status 0 indicates a match between the expected and computed hashes.

SEE ALSO
     radare2(1), rafind2(1), rahash2(1), rabin2(1), radiff2(1), rasm2(1), ragg2(1), rarun2(1), rax2(1),

AUTHORS
     pancake <pancake@nopcode.org>

                                                     Feb 6, 2015

```
