<!-- TITLE: rax2 -->

# rax2

## Help


```text
Usage: rax2 [options] [expr ...]
  =[base]                      ;  rax2 =10 0x46 -> output in base 10
  int     ->  hex              ;  rax2 10
  hex     ->  int              ;  rax2 0xa
  -int    ->  hex              ;  rax2 -77
  -hex    ->  int              ;  rax2 0xffffffb3
  int     ->  bin              ;  rax2 b30
  int     ->  ternary          ;  rax2 t42
  bin     ->  int              ;  rax2 1010d
  ternary ->  int              ;  rax2 1010dt
  float   ->  hex              ;  rax2 3.33f
  hex     ->  float            ;  rax2 Fx40551ed8
  oct     ->  hex              ;  rax2 35o
  hex     ->  oct              ;  rax2 Ox12 (O is a letter)
  bin     ->  hex              ;  rax2 1100011b
  hex     ->  bin              ;  rax2 Bx63
  ternary ->  hex              ;  rax2 212t
  hex     ->  ternary          ;  rax2 Tx23
  raw     ->  hex              ;  rax2 -S < /binfile
  hex     ->  raw              ;  rax2 -s 414141
  -l                           ;  append newline to output (for -E/-D/-r/..
  -b      bin -> str           ;  rax2 -b 01000101 01110110
  -B      str -> bin           ;  rax2 -B hello
  -d      force integer        ;  rax2 -d 3 -> 3 instead of 0x3
  -e      swap endianness      ;  rax2 -e 0x33
  -D      base64 decode        ;
  -E      base64 encode        ;
  -f      floating point       ;  rax2 -f 6.3+2.1
  -F      stdin slurp code hex ;  rax2 -F < shellcode.c
  -h      help                 ;  rax2 -h
  -k      keep base            ;  rax2 -k 33+3 -> 36
  -K      randomart            ;  rax2 -K 0x34 1020304050
  -L      bin -> hex(bignum)   ;  rax2 -L 111111111 # 0x1ff
  -n      binary number        ;  rax2 -n 0x1234 # 34120000
  -N      binary number        ;  rax2 -N 0x1234 # \x34\x12\x00\x00
  -r      r2 style output      ;  rax2 -r 0x1234
  -s      hexstr -> raw        ;  rax2 -s 43 4a 50
  -S      raw -> hexstr        ;  rax2 -S < /bin/ls > ls.hex
  -t      tstamp -> str        ;  rax2 -t 1234567890
  -x      hash string          ;  rax2 -x linux osx
  -u      units                ;  rax2 -u 389289238 # 317.0M
  -w      signed word          ;  rax2 -w 16 0xffff
  -v      version              ;  rax2 -v
```

## rax2 man page

```text
RAX2(1)                                      BSD General Commands Manual                                      RAX2(1)

NAME
     rax2 — radare base converter

SYNOPSIS
     rax2 [-ebBsSvxkKh] [[expr] ...]

DESCRIPTION
     This command is part of the radare project.

     This command allows you to convert values between positive and negative integer, float, octal, binary and hexa‐
     decimal values.

OPTIONS
     -b          Convert from binary string to character (rax2 -b 01000101)

     -k          Keep the same base as the input data

     -e          Swap endian.

     -F          Read C strings from stdin and output in hexpairs. Useful to load shellcodes

     -l          Append newline to the decoded output for human friendly-ness

     -K          Show randomart key asciiart for values or hexpairs

     -s          Convert from hex string to character (rax2 -s 43 4a 50)

     -S          Convert from character to hex string (rax2 -S C J P)

     -n          Show hexpairs from integer value

     -N          Show hexadecimal C string from integer value

     -u          Convert given value to human readable units format

     -v          Show program version

     -x          Convert a string into a hash

     -h          Show usage help message

USAGE
     Force output mode (numeric base)

       =f    floating point
       =2    binary
       =3    ternary
       =8    octal
       =10   decimal
       =16   hexadecimal

     Available variable types are:

       int   ->  hex    rax2 10
       hex   ->  int    rax2 0xa
       -int  ->  hex    rax2 -77
       -hex  ->  int    rax2 0xffffffb3
       int   ->  bin    rax2 b30
       bin   ->  int    rax2 1010d
       float ->  hex    rax2 3.33f
       hex   ->  float  rax2 Fx40551ed8
       oct   ->  hex    rax2 35o
       hex   ->  oct    rax2 Ox12 (O is a letter)
       bin   ->  hex    rax2 1100011b
       hex   ->  bin    rax2 Bx63

     With no arguments, rax2 reads values from stdin. You can pass one or more values as arguments.

       $ rax2 33 0x41 0101b
       0x21
       65
       0x5

     You can do 'unpack' hexpair encoded strings easily.

       $ rax2 -s 41 42 43
       ABC

     And it supports some math operations.

       $ rax2
       0x5*101b+5
       30

     It is a very useful tool for scripting, so you can read floating point values, or get the integer offset of a
     jump or a stack delta when analyzing programs.

SEE ALSO
     radare2(1), rahash2(1), rafind2(1), rabin2(1), radiff2(1), ragg2(1), rarun2(1), rasm2(1)

AUTHORS
     Written by pancake <pancake@nopcode.org>.

                                                     Jul 28, 2017

```
