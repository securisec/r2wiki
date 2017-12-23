<!-- TITLE: rarun2 -->

# rarun2

## Help

      Usage: rarun2 -v|-t|script.rr2 [directive ..]
      program=/bin/ls
      arg1=/bin
      # arg2=hello
      # arg3="hello\nworld"
      # arg4=:048490184058104849
      # arg5=:!ragg2 -p n50 -d 10:0x8048123
      # arg6=@arg.txt
      # arg7=@300@ABCD # 300 chars filled with ABCD pattern
      # system=r2 -
      # aslr=no
      setenv=FOO=BAR
      # unsetenv=FOO
      # clearenv=true
      # envfile=environ.txt
      timeout=3
      # timeoutsig=SIGTERM # or 15
      # connect=localhost:8080
      # listen=8080
      # pty=false
      # fork=true
      # bits=32
      # pid=0
      # pidfile=/tmp/foo.pid
      # #sleep=0
      # #maxfd=0
      # #execve=false
      # #maxproc=0
      # #maxstack=0
      # #core=false
      # #stdio=blah.txt
      # #stderr=foo.txt
      # stdout=foo.txt
      # stdin=input.txt # or !program to redirect input to another program
      # input=input.txt
      # chdir=/
      # chroot=/mnt/chroot
      # libpath=$PWD:/tmp/lib
      # r2preload=yes
      # preload=/lib/libfoo.so
      # setuid=2000
      # seteuid=2000
      # setgid=2001
      # setegid=2001
      # nice=5

## Examples of using rarun2 to debug a binary
  - `r2 -d rarun2 program=./<program_name> arg0=foo stdin=./<some_file> setenv=ENV_VAR=<value>`
  - Create a script file (script.rr2) with rarun2 config options

        #!/usr/bin/rarun2
        program=./<program_name>
        arg0=foo
        stdin=./<some_file>
        setenv=ENV_VAR=<value>

    Then run with `r2 -d rarun2 script.rr2`